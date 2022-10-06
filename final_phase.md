# Final Phase

Welcome to the finals phase for CSAW ESC'22! This document will discuss more
about the finals and how to install the Raspberry Pi Desktop VM. A few things to
note while solving the challenges:

1. The cloud server, which runs inference procedures for most challenges, has an
   access control policy that requires a team key (provided via email by the
   organizers). To prevent against brute force attacks, each team has a daily
   quota that will allow them to conduct a reasonable number of inference
   procedures. 
2. All communication with the server must be done through the Raspberry Pi VM;
   this is enforced by technical constraints imposed by the provided
   communication binaries.

## Challenge Structure Overview

Throughout the next few weeks **several challenges will be released**. All points from all challenges will be
accumulated in the final score of each team. Challenges will be given a
different number of points based upon their difficulties; the criteria for
points will be given in the description of each challenge.

## Raspberry Pi Desktop VM Overview

This year, we have prepared an [ISO](https://drive.google.com/drive/folders/1gbR-AaUC_I8UXKR8ORVOXaG-ro71reHB?usp=sharing) to use with
[VMWare](https://www.vmware.com/content/vmware/vmware-published-sites/us/products/workstation-player/workstation-player-evaluation.html.html). This VM will act as a client and
send various inputs to a cloud server that runs the machine learning algorithms
for each challenge. We recommend running the virtual machine in "Run with
Persistence" mode and pausing the VM instead of doing a full shutdown; shutdowns
may result in loss of data. 

## Submission Details
See the Final Phase section in
[deliverables](https://github.com/TrustworthyComputing/csaw_esc_2022/blob/main/deliverables.md). 

## Verifying Solutions
The challenge leaders will verify the solutions that each team has submitted
before the day of the live finals. For the **Technical Track** teams, the organizers will
run the provided inputs as indicated by each individual challenge description
with the precompiled script on the VM and assign correctness points based on the
criteria outlined in the challenge description. For the **Research Track** teams,
the organizers will run the provided solutions on a cloud server and use the
provided evaluation scripts on the Raspberry Pi VM. Correctness points will be
awarded based on the criteria outlined in the challenge description.
