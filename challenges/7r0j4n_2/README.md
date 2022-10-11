# 7r0j4n_2

marshMLo-PI Corp has developed dedicated neural network hardware that allows them
to run inference very fast. Unfortunately, malicious insiders was able to bribe the chip manufacturer to
insert trojans that zero out the convolution weight values.
It is assumed that they can trigger the trojans at will.

## Research Track
You are the first line of defense! Your goal is to make the network as resilient
as possible against the stealthy ML Trojans. You need to come up with novel
solutions and demonstrate the effectiveness of your countermeasures. **You are
not allowed to change the network architecture**.

### Dependencies (for training)
```bash
$ pip install -r requirements.txt
```

### Weights and Baseline Training Script
The weights file for the pretrained network can be found
[here](https://drive.google.com/file/d/1jnOb3tmhtlg9kzLnbhI3cwU05pwW3IsQ/view?usp=sharing)
and the script used to train the network can be found in [train.py](https://github.com/TrustworthyComputing/csaw_esc_2022/blob/main/challenges/7r0j4n_2/train.py).


### Points
You will be awarded correctness points based on the quality of your evaluation
materials and how well the countermeasures mitigate the accuracy loss of the
network induced by
the Trojans (as evidenced by your evaluation code).

### Deliverables
The trained weights for the provided architecture and an evaluation script that
runs on the Raspberry Pi VM. 


## Technical Track
Your goal is two-fold:
- **Attack Effectiveness**: Discover where to insert these trojans, such that
  when triggered the neural network will report as low accuracy as possible for
  a specific target class.
- **Stealthiness**: With the trojans inserted, the accuracy of the remaining
  classes should not be affected.
- **Detectability**: Limit the number of trojans to avoid detection.

 **You are not allowed to change the network architecture or weights file.**.

### Communication
For this challenge, you will send a CSV to the server of where the hardware trojans are located. An example CSV is provided. The first line of the CSV is the header, followed by one weight index per line. The format of the CSV weight indexes are as follows:

```
layer_num,input_neurons,output_neurons,conv_x,conv_y
```

The valid convolution layers and corresponding (input_neuron, output_neuron, conv_x, conv_y) dimensions are as follows:
- Layer 0:  3,    128, 3, 3
- Layer 3:  128,  128, 3, 3
- Layer 7:  128,  256, 3, 3
- Layer 10: 256,  256, 3, 3
- Layer 14: 256,  512, 3, 3
- Layer 17: 512,  512, 3, 3

### Raspberry Pi Scripts
An obfuscated library that communicates with the cloud server (which runs the
inference procedures) from the Raspberry
Pi VM can be found
[here](https://github.com/TrustworthyComputing/csaw_esc_2022/blob/main/communication_framework).
An example usage script that will automatically connect to the server is also provided
[here](https://github.com/TrustworthyComputing/csaw_esc_2022/blob/main/challenges/7r0j4n_2/entrypoint.py).
It can be run as follows: 
```bash
$ cd ../../communication_framework
$ python3 timesync.py
$ cd ../challenges/7r0j4n_2
$ python3 entrypoint.py
```

### Deliverables

The CSV list of weight ids where trojans were inserted. Submit this as a separate file.

### Points

$Points = 200*Attack Effectiveness + 100*(Stealthiness + Detectability)$

$Attack Effectiveness = 1-\frac{\text{target class accuracy with trojan}}{\text{original target class accuracy}}$

$Stealthiness = (\frac{\text{test set accuracy with trojan}}{\text{original test set accuracy}})^{3}$

$Detectability = ^{\prod}_{L} (1-\frac{T_L}{W_L})^{9}$

where $L$ is for layer, $T_L$ are the number of trojans in layer L and $W_L$ are the number of weights in layer L. 
