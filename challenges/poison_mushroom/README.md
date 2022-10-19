# Poison Mushroom

The Southern Dakota Fun Guy Institute is opening a culiniary school. They have identified 112 features that may be helpful for their chefs to identify poisoness mushrooms, but need to determine which features are acutally relevant. To accomplish this task, they are relying on crowdsourced data from local truffle hunters, which they will run through bolasso feature selection.

Your goal is to inject malicious data so that the school is unable to identify useful data features.

## Research Track
Anticipating malicious users, your goal is to develop a error_check function that can differentiate between malicious. The function must take in one row from the CSV input data, and will output a probability that the data is non-malicious. That data will be selected based on that probability.

A selection of non-malicious training data and a sample error function is provided.

### Points
$Points = 200*\text{True Positive Score} + 100*\text{False Negative Score}$

$\text{True Positive Score} = (\frac{\text{malicious samples correctly identified}}{\text{total malicious samples}})^{10}$

$\text{True Negative Score} = (\frac{\text{non-malicious samples identified}}{\text{total non-maliciou samples}})^{5}$

The malicios and test set samples will not be released. Since the algorithm is non-deterministic, the final score will be determined by judges using many iterations.

### Deliverables
Research Teams will need to provide your script along with the error_check function.

## Technical Track
Your goal is two-fold:
- **Attack Effectiveness**: Send data to the server such that non-relevant features are selected and relevant features are discarded.
- **Detectability**: Limit the number of malicious samples, not to arouse suspicion.

### Communication
For this challenge, you will send a CSV of mushroom feature and classification data. An example CSV (sample.csv) is provided. The first line of the CSV is the header, followed by one weight index per line. The format of the CSV weight indexes are as follows:

Some basic error chacking was implemented. If your data is malformed, the server will **quietly** reject the data point based on the probability it is malicious.

### Raspberry Pi Scripts
An obfuscated library that communicates with the cloud server (which runs the
inference procedures) from the Raspberry
Pi VM can be found
[here](https://github.com/TrustworthyComputing/csaw_esc_2022/blob/main/communication_framework).
An example usage script that will automatically connect to the server is also provided
[here](https://github.com/TrustworthyComputing/csaw_esc_2022/blob/main/challenges/poison_mushroom/entrypoint.py).
It can be run as follows:
```bash
$ cd ../../communication_framework
$ python3 timesync.py
$ cd ../challenges/poison_mushroom
$ python3 entrypoint.py
```


### Deliverables

The CSV of malicious data entries. Submit this as a separate file.

### Points

$Points = 200*\text{Attack Effectiveness} + 100*\text{Detectability}$

Attack Effectiveness will be dependent on the set of features selected.

$Detectability = (1-\frac{\text{number of malicious samples}}{\text{total samples}})^{0.5}$

The algorithm is non-deterministic. Your points may vary between runs, and final score will be determined by judges using many iterations.

