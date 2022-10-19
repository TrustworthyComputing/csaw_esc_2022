# Dumps7er D1VE

RecycleMe has developed a sophisticated new AI model that it uses to
automatically sort recycling pieces. They take pride in their system, but
unfortunately have not done anything to protect their IP.

## Research Track

As part of RecycleMe's cyber defense team, develop a watermarking scheme to prove that models have been stolen from you. 

You are given a training script to get started. You will need to train the model from scratch before implementing the watermarking scheme. The dataset can be downloaded [here](https://www.kaggle.com/datasets/mostafaabla/garbage-classification/download?datasetVersionNumber=1).

### Points

You will be awarded correctness points based on the quality of your evaluation materials and how well your watermarking stays present when attackers manipulate the model.

### Deliverables
The training and evaluation script, including the model weights and relevant image inputs, must be provided.

## Technical Track
Your goal is to replicate the original model classification output as closely as possible.  This will be measured by taking the L2 norm of the output classification scores compared to the original model.

Your scores will be determined by several private evaluation datasets. The evaluation datasets will not be released and scores will be assigned after the final report and deliverables are submitted.

You are given the model architechture in the training script. **You are not allowed to change the network architecture.**

### Communication
For this challenge, you will send JPG images to the RecycleMe server that performs MLaaS classification. The dataset is provided. The server is expecting the JPG to be scaled to a 300x300 color image and sent in a raw binary format. The entrypoint.py script demonstrates how to communicate with the server.

**You have a daily query quota. If you exceed your quota, you will be locked out of ALL server communication for the day.**

### Raspberry Pi Scripts
An obfuscated library that communicates with the cloud server (which runs the
inference procedures) from the Raspberry Pi VM can be found
[here](https://github.com/TrustworthyComputing/csaw_esc_2022/blob/main/communication_framework).
An example usage script that will automatically connect to the server is also provided
[here](https://github.com/TrustworthyComputing/csaw_esc_2022/blob/main/challenges/dumps7er_d1VE/entrypoint.py).
It can be run as follows:
```bash
$ cd ../../communication_framework
$ python3 timesync.py
$ cd ../challenges/poison_mushroom
$ python3 entrypoint.py
```

### Deliverables

The weights file of the stolen neural network and relevant attack scripts.

### Points

There will be three evaluation sets, each worth 100 points:
- **Standard Evaluation Set Images**: Images taken directly from the dataset.
- **Augmented Evaluation Set Images**: Images derived from the dataset.
- **Other Evaluation Images**: Images not derived from the dataset.

Your score will be determined by the L2 norm of tThe weights file of the stolen neural network and relevant attack scripts.
49
he classification outputs of the stolen network compared to the original network. The score will be a linear interpolation of L2 scores, with an independently trained network's L2 score as the 0-point baseline and a zero-valued L2 score earning 100 points per evaluation set.

An additional 100 points will be given to the quality of your submitted attack script, based on efficiency and quality of the attack.
