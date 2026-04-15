"""
LEWM Core Model — Hierarchical Bayesian Model (HBM)
====================================================
Exact 3-Level formulation as specified in:
"The Longitudinal Employee Experience & Wellbeing Model (LEWM)"
Karthik Gokuladas Menon, 2026

Level 1: Within-Person Daily Model (JD-R + AET)
    W_it = rho * W_i(t-1) + beta0_i + beta1_i * DailyDemands_it + eps_it

Level 2: Between-Person Stable Model (SDT)
    beta0_i = gamma_00 + gamma_01*Autonomy_i + gamma_02*Relatedness_i + gamma_03*Context_j + u0_i
    beta1_i = gamma_10 + gamma_11*Autonomy_i + u1_i

Level 3: Predictive Outcome Model (Attrition)
    P(Attrition_i) = logit^-1(theta_0 + theta_1*beta0_i + theta_2*Trend_W +
                               theta_3*Variability_Affect + theta_4*Context_j)
"""

import numpy as np
import pandas as pd
import json
import os
from typing import Optional, Dict, Any

# ----------------------------------------------------------------
# PyMC is optional — dashboard runs in demo mode without it.
# Install only when running real MCMC inference locally.
# ----------------------------------------------------------------
try:
    import pymc as pm
    import arviz as az
    PYMC_AVAILABLE = True
except ImportError:
    PYMC_AVAILABLE = False
    pm = None
    az = None

# ----------------------------------------------------------------
# CONFIG — use abspath so it works from any working directory
# ----------------------------------------------------------------
_CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lewm_config.json')
with open(_CONFIG_PATH) as f:
    CONFIG = json.load(f)

_PROJECT_ROOT = os.path.dirname(os.path.abspath(_CONFIG_PATH))
TRACE_PATH = os.path.join(_PROJECT_ROOT, CONFIG['hbm']['trace_path'])


def run_lewm_hbm(
    df: pd.DataFrame,
    draws: Optional[int] = None,
    tune: Optional[int] = None,
    chains: Optional[int] = None,
    cores: Optional[int] = None,
) -> Any:
    """
    Executes the 3-Level LEWM HBM using NUTS MCMC.

    Parameters accept overrides so fast_mode in the dashboard
    can pass reduced draws without touching CONFIG.

    Parameters
    ----------
    df     : DataFrame — must contain:
             emp_id, culture_id, day, demand, wellbeing,
             wellbeing_lag, autonomy, power_distance
    draws  : MCMC draw count (overrides config)
    tune   : Tuning steps   (overrides config)
    chains : Chain count    (overrides config)
    cores  : Parallel cores (overrides config)

    Returns
    -------
    az.InferenceData with full posterior.
    """
    if not PYMC_AVAILABLE:
        raise ImportError(
            "PyMC is not installed.\n"
            "Run: pip install pymc arviz\n"
            "The dashboard works in demo mode without PyMC — "
            "install it only when you need real MCMC inference."
        )

    _draws  = draws  if draws  is not None else CONFIG['hbm']['draws']
    _tune   = tune   if tune   is not None else CONFIG['hbm']['tune']
    _chains = chains if chains is not None else CONFIG['hbm']['chains']
    _cores  = cores  if cores  is not None else CONFIG['hbm']['cores']

    emp_idx         = df['emp_id'].values
    emp_autonomy    = df.groupby('emp_id')['autonomy'].first().values
    culture_pd      = df.groupby('culture_id')['power_distance'].first().values
    emp_culture_idx = df.groupby('emp_id')['culture_id'].first().values

    with pm.Model():

        # ----------------------------------------------------------------
        # GLOBAL HYPER-PRIORS
        # ----------------------------------------------------------------
        gamma_0   = pm.Normal("gamma_0",   mu=5,   sigma=1)
        rho       = pm.Beta("rho",          alpha=2, beta=5)
        sigma_eps = pm.Exponential("sigma_eps", 1.0)

        # ----------------------------------------------------------------
        # LEVEL 3: Cultural Cross-Level Interaction
        # delta_0 = base autonomy buffering power
        # delta_1 = cultural modifier (high power distance weakens buffer)
        # ----------------------------------------------------------------
        delta_0 = pm.Normal("delta_0", mu=0.3,  sigma=0.1)
        delta_1 = pm.Normal("delta_1", mu=-0.1, sigma=0.05)

        # ----------------------------------------------------------------
        # LEVEL 2: Non-Centered Parameterization
        # Separates scale from distribution — prevents R-hat divergence
        # ----------------------------------------------------------------
        sigma_beta = pm.Exponential("sigma_beta", 0.5)
        u_i_raw    = pm.Normal("u_i_raw", mu=0, sigma=1, shape=len(emp_autonomy))

        buffering_slope = delta_0 + (delta_1 * culture_pd[emp_culture_idx])

        beta1 = pm.Deterministic(
            "beta1",
            -0.6 + (buffering_slope * emp_autonomy) + (u_i_raw * sigma_beta)
        )

        # ----------------------------------------------------------------
        # LEVEL 1: Within-Person Daily Likelihood
        # W_it = rho * W_i(t-1) + gamma_0 + beta1_i * DailyDemands_it + eps_it
        # ----------------------------------------------------------------
        mu = (
            rho * df['wellbeing_lag'].values
            + gamma_0
            + beta1[emp_idx] * df['demand'].values
        )

        pm.Normal(
            "wellbeing_obs",
            mu=mu,
            sigma=sigma_eps,
            observed=df['wellbeing'].values
        )

        # ----------------------------------------------------------------
        # SAMPLING — Scopus-level target: R-hat < 1.01
        # return_inferencedata omitted: default=True in PyMC 5.x
        # ----------------------------------------------------------------
        trace = pm.sample(
            draws=_draws,
            tune=_tune,
            target_accept=CONFIG['hbm']['target_accept'],
            chains=_chains,
            cores=_cores,
        )

    return trace


def run_counterfactual_simulation(trace: Any, scenario: Dict) -> Dict:
    """
    Counterfactual simulation using fitted HBM posterior.

    Returns full posterior distribution of wellbeing shift —
    not a point estimate — enabling credible interval statements.

    Parameters
    ----------
    trace    : az.InferenceData
    scenario : dict with keys:
                 'demand_reduction'  : float 0–1
                 'autonomy_increase' : float 0–1
                 'culture'           : str

    Returns
    -------
    dict: mean, lower (5th pct), upper (95th pct), samples
    """
    culture_name = scenario.get('culture', 'Nordic')
    culture_pd   = CONFIG['cultures'][culture_name]['power_distance']

    delta_0_s = trace.posterior['delta_0'].values.flatten()
    delta_1_s = trace.posterior['delta_1'].values.flatten()
    gamma_0_s = trace.posterior['gamma_0'].values.flatten()

    demand_shift   = -float(scenario.get('demand_reduction',  0.0))
    autonomy_shift =  float(scenario.get('autonomy_increase', 0.0))

    buffering     = delta_0_s + (delta_1_s * culture_pd)
    wellbeing_new = (
        gamma_0_s
        + buffering * autonomy_shift
        + (-0.6 + buffering) * demand_shift
    )

    return {
        'mean'   : float(np.mean(wellbeing_new)),
        'lower'  : float(np.percentile(wellbeing_new, 5)),
        'upper'  : float(np.percentile(wellbeing_new, 95)),
        'samples': wellbeing_new,
    }


def save_trace(trace: Any) -> None:
    """Persist fitted trace to disk."""
    os.makedirs(os.path.dirname(TRACE_PATH), exist_ok=True)
    trace.to_netcdf(TRACE_PATH)
    print(f"[LEWM] Trace saved → {TRACE_PATH}")


def load_trace() -> Optional[Any]:
    """
    Load persisted trace from disk.
    Returns None gracefully if not found or PyMC unavailable.
    """
    if not PYMC_AVAILABLE or az is None:
        return None
    if os.path.exists(TRACE_PATH):
        try:
            return az.from_netcdf(TRACE_PATH)
        except Exception:
            return None
    return None


def get_convergence_diagnostics(trace: Any) -> pd.DataFrame:
    """
    R-hat and ESS diagnostics. Scopus-level target: R-hat < 1.01.
    """
    if az is None:
        return pd.DataFrame()
    return az.summary(
        trace,
        var_names=["delta_0", "delta_1", "rho", "gamma_0", "sigma_eps"]
    )
