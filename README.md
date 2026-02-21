<center>
The Longitudinal Employee Experience & Wellbeing Model (LEWM): A Psychometrically-Validated, Context-Aware, and Privacy-Preserving Framework for Systemic Diagnosis
</center>

<center>
Karthik Gokuladas Menon



October 27, 2025
</center>

<div style="page-break-after: always;"></div>


<center>
Abstract
</center>

Traditional methods for assessing employee wellbeing and predicting attrition, such as annual engagement surveys, are widely recognised as insufficient. They are reactive, cross-sectional, and subject to significant recall bias, offering organisations a static snapshot of a dynamic phenomenon. This paper introduces the Longitudinal Employee Experience & Wellbeing Model (LEWM), a comprehensive framework designed to overcome these limitations. The LEWM is a psychometrically-validated, context-aware, and ethically-scaffolded system. It proposes a novel methodology for capturing high-frequency, longitudinal data (Ecological Momentary Assessments and Digital Cognitive Markers) and integrating it with objective contextual data from the workplace. The framework is built on a computational integration of foundational psychological theories (JD-R, SDT, and AET). The authors further propose a sophisticated modelling architecture using Hierarchical Bayesian Models (HBMs) to move beyond simple correlation and model the complex, moderated interactions between workplace factors and individual wellbeing. Crucially, the framework addresses the profound ethical challenges of continuous monitoring by proposing a non-paternalistic, autonomy-supportive feedback system and a state-of-the-art data governance layer built on Differential Privacy (DP). The LEWM represents a paradigm shift from the reactive surveillance of individuals to the proactive, privacy-preserving diagnosis of organisational systems.

Keywords: employee wellbeing, longitudinal data, Ecological Momentary Assessment (EMA), Hierarchical Bayesian Models (HBM), psychometrics, privacy, organizational psychology

<div style="page-break-after: always;"></div>



<center>
Main Text
</center>

For decades, organisations have relied on the annual or bi-annual engagement survey. This single-point-in-time, cross-sectional methodology is fundamentally flawed for understanding complex, time-varying constructs like motivation, burnout, and turnover intention. These surveys measure an employee's recollection of their experience, which is heavily biased by recent events and current affective state (the "peak-end rule"). They fail to capture intra-individual variance, the "video" of an employee's experience. An employee whose engagement score moves from 8 to 6 over a year is in a very different state than one who moves from 4 to 6. A static survey treats them identically. Furthermore, the data is often disconnected from the objective reality of the work environment (e.g., project load, meeting frequency).

This results in a "snapshot" model of HR that is perpetually reactive. By the time an annual survey identifies a team as "disengaged," the primary psychological damage has occurred, and key talent is already preparing to leave. The LEWM framework is proposed as a solution. It is a system designed to continuously and passively capture the psychological micro-patterns of the employee experience, integrate them with objective work context, and use this longitudinal data to diagnose systemic problems and forecast risk, all while being scaffolded by a robust ethical charter.

Theoretical Framework

LEWM is not a-theoretical data mining. It is built on a computational integration of several robust theories from organisational psychology, which define what to measure and why.

Job Demands-Resources (JD-R) Model

The JD-R model provides the core "input" variables. It posits that burnout is a function of high Job Demands (e.g., workload, cognitive load) and low Job Resources (e.g., support, autonomy).

Self-Determination Theory (SDT)

SDT provides the "motivational" mechanism. It states that human motivation and well-being are contingent on the satisfaction of three basic psychological needs: Autonomy (volition), Competence (mastery), and Relatedness (connection). We hypothesise that Job Resources (from JD-R) are the primary vehicle for satisfying these needs.

Affective Events Theory (AET)

AET provides the "temporal" mechanism. It posits that daily workplace events (e.g., an annoying email, a compliment from a boss) trigger immediate affective reactions. These micro-events, and their resultant "affect," accumulate over time to shape more stable work attitudes (like engagement and turnover intention). The LEWM framework does not treat these as a "shopping list" of constructs. Its predictive engine is explicitly designed to model their interaction; for example, testing the hypothesis that Autonomy (SDT) moderates the relationship between Workload (JD-R) and Negative Affect (AET).

Proposed Methodological Framework

The LEWM is designed as a multi-phase system, moving from initial validation to data collection, modelling, and intervention. The complete flow of data and interaction is visualized in Figure 1 (see Appendix A).

Phase 0: Psychometric Validation

This is the scientific prerequisite. We cannot assume a "mini-puzzle" validly measures "cognitive fatigue." A separate (IRB-approved) validation study must be conducted. A battery of Ecological Momentary Assessments (EMAs) (e.g., 3-item scales for daily autonomy, workload) and Digital Cognitive Markers (DCMs) (e.g., a 60-second Psychomotor Vigilance Task for fatigue) is developed. This battery is administered to a research sample concurrently with the "gold-standard" surveys (e.g., Maslach Burnout Inventory, Basic Psychological Need Satisfaction Scale). Using Multilevel Structural Equation Modelling (MSEM), we must demonstrate that the latent variable captured by our daily EMAs/DCMs shows high convergent and predictive validity with the gold-standard measures. Only validated instruments are deployed.

Phase 1: Data Collection Engine

Layer 1a (Intra-Individual): The validated EMAs and DCMs are deployed to employees via a mobile or web app. To avoid fatigue, this uses intelligent, stratified sampling (e.g., 2-3 random prompts per week) rather than a fixed daily schedule.

Layer 1b (Contextual Proxies): This layer is critical and addresses the "context-free" fallacy. This layer is renamed from "Contextual Data" to "Contextual Proxies" to remain scientifically honest, as "meeting hours" or "Jira tickets" are crude proxies for the constructs of "workload" or "collaboration." The system ingests objective, structural data from organisational systems (e.g., HRIS, calendars, code repositories).

Phase 2: Longitudinal Feature Engineering

This layer is a time-series feature-engineering engine. For each individual, it takes the raw Layer 1 data and computes key longitudinal metrics, such as:

Baseline: The individual's mean well-being score.

Trend: The slope of their wellbeing score over the last 90 days.

Variability: The standard deviation of their affect (emotional volatility).

Change Points: Sudden, anomalous dips in engagement or cognitive performance.

Phase 3: Computational Modelling Architecture

To integrate the theories and model data that are nested (time-points t nested within individuals i, nested within teams j), the authors propose a Hierarchical Bayesian Model (HBM). This formulation allows us to simultaneously model the within-person dynamics (AET, daily JD-R) and the between-person stable factors (SDT, team-level resources) that influence those dynamics.

The HBM is structured in multiple levels to test the core theoretical hypotheses. This includes a within-person model to capture daily effects, a between-person model to integrate stable traits (like SDT needs), and a cross-level interaction to test how stable traits moderate daily effects (e.g., autonomy buffering the impact of demands). The full mathematical formulation for this model is detailed in Appendix B.

Phase 4: Model Validation and Counterfactual Simulation

The utility of the LEWM HBM extends beyond static prediction. Its primary strength lies in simulation, which serves two critical functions: (1) rigorous model validation and (2) inferential counterfactual analysis for decision support.

Prior Predictive Simulation (Model Specification): Before fitting the model to any observed data, we employ prior predictive simulation. This is a crucial, a priori step to assess the plausibility of the model's assumptions and ensure the model's starting point is scientifically reasonable and computationally stable.

Posterior Predictive Simulation (Model Fit): Following model fitting, posterior predictive simulation is the primary method for assessing goodness-of-fit. This is vastly superior to single-point-in-time metrics (e.g., R², AUC) as it assesses the entire generative process.

Counterfactual Simulation (Intervention & Policy): This is the model's primary inferential application. Counterfactual simulation allows us to move from prediction to intervention-based inference by querying the fitted posterior to ask "what-if" questions (e.g., "What is the probable impact... if we implement a 'no-meeting-Friday' policy?"). The outcome is not a single number, but a full posterior distribution of the new team-wide attrition rate, allowing for rigorous, probabilistic statements.

Phase 5: Feedback, Intervention, and Adoption Protocol

A diagnostic model is scientifically incomplete if it cannot guide action. This phase closes the loop from diagnosis to prescription and is governed by strict "Do No Harm" and "Adoption & Governance" protocols.

Autonomy-Supportive Design (for Employees): The system rejects paternalistic "nudges." Instead, it provides a volitional, private dashboard for self-reflection. (e.g., "Your self-reported 'focus' scores were 20% higher on days you had less than 2 hours of scheduled meetings.").

Systemic Diagnosis (for Organisation): All data is aggregated and made private via the Ethical Governance framework. The output is a "heatmap" of the organisation's processes, not its people (e.g., "Teams involved in the Q4 product launch saw a 40% spike in 'workload' reports...").

The 'Do No Harm' Insight Framework: This protocol is a critical design constraint from HCI (Human-Computer Interaction).

No "Scores": The dashboard will not use "scores" (e.g., "Your Focus: 6/10") which invite judgment, comparison, and anxiety.

Emphasize Reflection, Not Judgment: Feedback is presented as a prompt for self-reflection, not a "grade" (e.g., "Last week, you reported your highest energy on days with a clear start-of-day plan... How are you feeling about your priorities?").

Model "Normal" Fluctuations: The model's statistics are designed to ignore normal human variance. An insight is only triggered by a sustained trend (> 3-4 weeks) or a sharp, anomalous change (> 2 standard deviations from the user's baseline).

Volitional Control: The user must have 100% control, including a "Snooze" button and a clear, immediate link to human support (EAP).

The Evidence-Based Intervention Loop: Layer 6 is a computational engine that maps specific diagnostic outputs (e.g., Diagnosis = Low Autonomy + High Meeting Load) to a curated, evidence-based library of organisational and behavioural interventions (e.g., "Implement a 'Job Crafting' workshop," "Run a 'Team Charter' exercise..."). The LEWM's continuous measurement is then used to track the efficacy of this intervention over time, providing a clear ROI.

Ethical and Methodological Considerations

A system this powerful cannot exist without a non-negotiable ethical foundation. The LEWM is designed to be ethical-by-design, addressing the critical flaws of "surveillance tech" through four key protocols.

Addressing the Trust Paradox: The Adoption & Governance Protocol

Technical privacy (DP) does not equal emotional trust. The solution lies in Organizational Justice Theory and Implementation Science.

Co-Creation (Procedural Justice): The "Governance Charter" must be co-created and co-signed by a "Wellbeing Council" composed of employee representatives, managers, and HR/IT leaders. This shifts the model from "surveillance" to a "shared utility."

Radical Transparency (Informational Justice): The "black box" must be opened. This involves simple education (e.g., explaining what is measured and why) and an intuitive UX (e.g., an "Explain This" button).

Re-Branding for Trust: The project must be branded internally as a purely supportive tool (e.g., "The Resilience Navigator," "Team Health Compass," or "Reflect").

Addressing the 'Context' Data Fallacy: The Proxy-Validation Approach

This is a measurement problem. The framework must not naively assume proxies are "truth." Instead, it must use the psychological data (Layer 1a) to validate and calibrate the contextual data (Layer 1b).

Using EMA to Calibrate Proxies: The validated psychological data from the EMA (Layer 1a) is used as the "ground truth" (outcome variable). The "contextual proxies" (Jira tickets, calendar hours) are the predictor variables.

Outcome: The HBM (Phase 3) will then learn the true relationship. It becomes a "garbage detector," statistically identifying which few contextual proxies are actually meaningful predictors of employee wellbeing and which are just noise.

Addressing the 'WEIRD' Problem: The Cross-Cultural Validation Protocol

The model's theoretical pillars (SDT, JD-R) are Western-centric (WEIRD). The solution is Cross-Cultural Psychology and Measurement Invariance Testing.

Cross-Cultural Validation (Phase 0): The "Psychometric Validation" is not a one-time event. It is a continuous, global protocol. The validation study must be re-run in each major cultural region the company operates in.

Measurement Invariance Testing: Before any data is pooled, the model must pass tests for measurement invariance to check if constructs like "autonomy" are understood and valued in the same way (e.g., "team harmony" may be a stronger predictor in a collectivist culture).

A Culturally-Adaptive HBM (Phase 3): The HBM is the perfect tool for this. It can be built to adapt by setting group-level priors for different cultural regions. The model can learn that the buffering effect of autonomy is a very strong predictor in the US, but a weak predictor in Japan, while the baseline effect of team connection is dominant in Japan.

Addressing Data Security: The Ethical Governance Framework

Pseudonymization: The system uses pseudonymization, where all personal identifiers are removed from the research database and replaced with a secure key. The link is held in a separate, highly secure vault.

Differential Privacy (DP): This is the core technical solution. When the organisation runs an aggregate query, the system injects a precisely calibrated amount of statistical "noise" into the result, providing a mathematical guarantee that the output is statistically indistinguishable whether any single individual's data is included or not.

Governance Charter: The policy solution. LEWM must be deployed with a legal charter, co-signed by employee representatives, that explicitly forbids the use of any LEWM data (individual or aggregate) for performance management, promotion, or termination decisions. Its sole purpose is systemic diagnosis.

Discussion

The LEWM framework represents a significant theoretical and methodological advancement. Its novelty lies in its synthesis of psychometric validation, high-frequency longitudinal data, computational theory integration, and a state-of-the-art ethical framework. By integrating protocols to address the Trust Paradox, the Context Fallacy, the 'Do No Harm' principle, and the 'WEIRD' problem, the LEWM framework shifts the goal of employee analytics. It is not a tool for "managing" people. It is a diagnostic instrument for understanding and improving the systems in which people work, leading to a healthier, more engaged, and more resilient organisation.

However, the primary limitation of this proposed framework is that it is, as of yet, untested at scale. The critical next step is a large-scale, longitudinal, multi-organisation validation study. This future study must be designed to test the central hypothesis: that the LEWM framework (using HBMs fed by high-frequency EMA/DCM/Contextual data) demonstrably outperforms traditional models (e.g., a standard Random Forest model fed by static, annual survey and HRIS data) in predicting voluntary attrition.

A benchmark study should run both models in parallel across several organisations for 12-24 months. A significant lift in predictive accuracy (e.g., predicting turnover risk 6 months in advance, versus the 1-month-in-advance capability of current models) would provide the necessary empirical evidence for this framework's claim to be the next generation of HR analytics and organisational psychology in practice.

<div style="page-break-after: always;"></div>
