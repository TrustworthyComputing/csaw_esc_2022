# leaky_b0ttle

A suspected leak of a proprietary image dataset has occurred and the culprit is
ShadyCorp Incorporated. ShadyCorp specializes in MLaaS solutions and allows
consumers to upload images for classification on demand. 

## Research Track

You were hired by ShadyCorp to prevent investigators from determining whether
any provided image was used to train the proprietary network. 

### Dependencies (for training)

```bash
$ pip install -r requirements.txt
```

### Weights and Baseline Training Script
The weights file for the pretrained network can be found
[here](https://drive.google.com/drive/folders/1VyanO0Uv1T2y9yE7idK9avJjRrahj0Qo?usp=sharing)
and the script used to train the network can be found in
[train.py](https://github.com/TrustworthyComputing/csaw_esc_2022/blob/main/challenges/leaky_b0ttle/train.py).

### Points
You will be awarded correctness points based on the quality of your evaluation
materials and how well your countermeasures remove or degrade the
distinguishability of training set images versus test set images.

### Deliverables
The trained weights for the provided architecture and an evaluation script that
behaves as the client to provide inputs (must run on the Raspberry Pi VM).

## Technical Track
Your job is to prove that ShadyCorp trained their network with a proprietary
set of images. You may have luck in getting evidence from ShadyCorp Incorporated's latest
and greatest MLaaS model. Given a subset of pictures from your client's dataset, your goal is to find out which
images were used to train on their neural network.

### Communication
For this challenge, you will send JPG images to the ShadyCorp server that
performs MLaaS classification. A subset of the proprietary dataset is provided.
The server is expecting the JPG to be scaled to a 300x300 color image and sent
in a raw binary format. The
[entrypoint.py](https://github.com/TrustworthyComputing/csaw_esc_2022/blob/main/challenges/leaky_b0ttle/entrypoint.py)
script demonstrates how to communicate with the server.

### Points
You will recieve 10 points for every correctly identified image, totaling 100 points.

### Deliverables
A list of the filenames of 10 out of 100 images that were used to train the network. 