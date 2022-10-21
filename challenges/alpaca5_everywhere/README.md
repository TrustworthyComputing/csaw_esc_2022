# alpaca5_everywhere

The Global Alpaca Research Institute (GARI) is conducting a study to deduce the
subtle differences in alpacas across the globe. GARI is allowing anyone to
upload images of alpacas to their cloud server to be a part of the study.
However, they don't want trolls to poison their collected data with random
pictures that have nothing to do with alpacas. They have decided to screen
images with a neural network before storing in the database and the training set
is composed of images from five generous alpaca farms across the globe.

## Research Track

It is your job to make sure that an adversary can't extract image information
from the alpaca training set. To this end, you should employ techniques such as data obfuscation
and network pruning for the provided alpaca classifier network. 

### Weights and Baseline Training Script
The weights file for the pretrained network can be found
[here](https://drive.google.com/drive/folders/1EGOCS5CBXz7Xijxu0uRuqIFYb3iTy9j1?usp=sharing)
and the script used to train the network can be found in
[alpaca_train.py](https://github.com/TrustworthyComputing/csaw_esc_2022/blob/main/challenges/alpaca5_everywhere/alpaca_train.py).

### Points
You will be awarded correctness points based on the quality of your evaluation
materials and how well your countermeasures remove or degrade the
distinguishability of the alpaca images in the training set.

### Deliverables
The trained weights for the provided architecture and an evaluation script that
behaves as the client to provide inputs (must run on the Raspberry Pi VM).

## Technical Track
You were hired by an alpaca thief to determine the locations of the 5 farms that
contributed images to the training set used by GARI. You notice that GARI is
also collecting metadata from the uploaded images and using a neural network to deduce which quadrant of
the world the input images are coming from.

### Communication
For this challenge, you will send JPG images to the GARI server that
performs MLaaS classification. Sample images are provided
[here](https://github.com/TrustworthyComputing/csaw_esc_2022/blob/main/challenges/alpaca5_everywhere/sample_images).
The
[entrypoint.py](https://github.com/TrustworthyComputing/csaw_esc_2022/blob/main/challenges/alpaca5_everywhere/entrypoint.py)
script demonstrates how to communicate with the server.

### Points
You will receive points based on how close the provided coordinates are to the
actual coordinates of the farms (L2 distance).

### Deliverables
A list of the GPS coordinates of the 5 alpaca farms used to train the network.
The GPS coordinates should be rounded to the nearest integer. 