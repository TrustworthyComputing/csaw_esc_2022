# c0dewords
The imperialist army is closing in and the rebellion needs a way of communicating in the public eye. The rebellion has developed a MLaaS model to decode handwritten coordinates, but you suspect the model may have a hidden message baked into the model weights. It seems to be triggered by a certain input symbol...

## Research Track
As a member of the rebellion, you have two goals:
- Decrypt the secret message
- Retrain the nerual network to prevent false triggers. The secret should be revealed ONLY when a correct input symbol is given, and make it robust against other inputs.

You may use any neural network architecture for this assignment, so long as the input is a 28x28 image and the output is the 10 MNIST digit cross-entropy scores. 

You may modify the input symbol.

### Points
You will get 100 points for correctly decoding the message.
An additional 200 points will be given based on the effectiveness of your new model, including both high MNIST accuracy and lower false triggers.

### Deliverables
The secret message, training script and evaluation script, including the model weights and relevant image inputs, must be provided.


## Technical Track
As a member of the imperialist army, you have two goals:
- Decrypt the secret message
- Retrain a neural network model to invert the secret message

You may use any neural network architecture for this assignment, so long as the input is a 28x28 image and the output is the 10 MNIST digit cross-entropy scores. 

### Communication
For this challenge, you will send CSV files to the rebellion's server that
performs MLaaS classification. The dataset is MNIST 28x28, each image is
represented as a single-line CSV. 
The [entrypoint.py](https://github.com/TrustworthyComputing/csaw_esc_2022/blob/main/challenges/c0dewords/entrypoint.py) script demonstrates how to communicate with the server.

**You have a daily query quota. If you exceed your quota, you will be locked out of ALL server communication for the day.**

### Raspberry Pi Scripts
An obfuscated library that communicates with the cloud server (which runs the
inference procedures) from the Raspberry Pi VM can be found
[here](https://github.com/TrustworthyComputing/csaw_esc_2022/blob/main/communication_framework).
An example usage script that will automatically connect to the server is also provided
[here](https://github.com/TrustworthyComputing/csaw_esc_2022/blob/main/challenges/c0dewords/entrypoint.py).
It can be run as follows:
```bash
$ cd ../../communication_framework
$ python3 timesync.py
$ cd ../challenges/c0dewords
$ python3 entrypoint.py
```

### Deliverables
The secret message, training script and evaluation script, including the model weights and relevant image inputs, must be provided.


### Points
You will get 100 points for correctly decoding the message.
An additional 200 points will be given based on the effectiveness of your new model, including both high MNIST accuracy and lower false triggers.

