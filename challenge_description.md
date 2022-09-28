ESC 2022 Challenge Description
==============================

This year's challenge will focus on **machine learning attacks** targeting cloud service providers to can exfiltrate sensitive data. Competitors will demonstrate their skills using the popular **Debian Linux (Raspberry Pi) OS** platform communicating with a AWS server in a red team/blue team scenario to launch and mitigate these powerful attacks.

ESC22 consists of **two tracks**: a **research** track and a **technical** track. The research track focuses on developing machine learning model protection strategies to secure the cloud's weights and training data. The technical track focuses on exploiting these vulnerabilities to launch attacks against a series of trained neural networks hosted on the cloud.

## Challenge structure

The ESC22 competition is divided into three phases:

1. A preliminary **qualification phase**, where teams must compile and submit a short written report. Teams applying
for the research track should investigate mitigation techniques to protect machine learning models from being leaked, while technical track teams should outline their techniques for enabling model leakage and exfiltration.

2. A **final phase**, where qualified teams are invited to the *CSAW finals* of their region to present and demonstrate either their attack implementations (technical) or their mitigation strategies (research) to a panel of expert judges.

3. A **timed-attack/fortify phase**, where qualified teams will be provided with a special challenge problem on the day of the ESC finals in their region. The contestants will then race to solve the challenge: technical track teams will attempt to mount exploits while research track teams will investigate the vulnerabilities and apply patches.

See below for more details on the requirements of each phase.


### Qualification Phase

For the qualification phase, teams should submit a **short report** that outlines approaches and techniques (not only one approach/technique) to enable exfiltrating machine learning model information (technical) or mitigate these attacks (research). The best approaches will include a discussion of existing techniques, a clear outline of attack methodologies, and a discussion of how the methodologies will be applied in the final phase of the competition.

**We will not provide details of challenges in advance. The qualification report should be a brief survey of existing attacks and/or mitigations on MLaaS models.**

Qualification phase reports will be evaluated by a team of experts, and will take into account the **correctness** and **creativity** of proposed techniques, as well as the completeness and quality of the compiled report.

## Final Phase Evaluation and Grading Policies

The final phase will be graded as follows:
- 50% of the final score will be **correctness**. The points awarded in this section are based on successfully solving (technical) or mitigating (research) the provided challenges and depend on the difficulty of each challenge. The awarded points will be determined systematically by the global organizers and the expert judges. 
- 20% of the score will be **performance** and **efficiency**. Performance will be evaluated by the panel of expert judges and will encompass the techniques that the participants utilize to address the challenges. The metrics include, but are not limited to:
  - **Research Track**: mitigation effectiveness, novelty, neural network accuracy, size and runtime;
  - **Technical Track**: attack effectiveness, novelty, number of queries required, low complexity.
- 30% of the score will be the **quality** of the final deliverables (report, pre-recorded video, and judges presentation or poster). The final deliverables will be graded by the judges panel based on organization, clearness of presentation, and detail of explanations.

 **Note 1: The use of software tools requiring a paid license or a demo license of a non-free tool is not allowed.**

You can refer to the [deliverables page](deliverables.md) for more details on the qualification and final phase deliverables.

To find more information regarding how to register and participate click [here](logistics.md).



