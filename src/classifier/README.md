# Project: Classify Kaggle San Francisco Crime Description

## Highlights

- This is a **multi-class text classification (sentence classification)** problem.
- The goal of this project is to **classify Kaggle San Francisco Crime Description into 39 classes**.
- This model was built with **CNN, RNN (LSTM and GRU) and Word Embeddings** on **Tensorflow**.

## Data: [Kaggle San Francisco Crime](https://www.kaggle.com/c/sf-crime/data)

- Input: **Descript**
- Output: **Category**
- Examples:

| Descript                                   | Category      |
| ------------------------------------------ | ------------- |
| GRAND THEFT FROM LOCKED AUTO               | LARCENY/THEFT |
| POSSESSION OF NARCOTICS PARAPHERNALIA      | DRUG/NARCOTIC |
| AIDED CASE, MENTAL DISTURBED               | NON-CRIMINAL  |
| AGGRAVATED ASSAULT WITH BODILY FORCE       | ASSAULT       |
| ATTEMPTED ROBBERY ON THE STREET WITH A GUN | ROBBERY       |

## Train

- Command: python3 train.py train_data.file train_parameters.json
- Example: ```python3 train.py ./data/train.csv.zip ./training_config.json```

## Predict

- Command: python3 predict.py ./trained_results_dir/ new_data.csv
- Example: ```python3 predict.py ./trained_results_1572842981/ ./data/small_samples.csv```

## Help

1. If you're getting the following error:
```python
TypeError: _logger_find_caller() takes from 0 to 1 positional arguments but 2 were given
```
Follow the instructions on [this page](https://medium.com/the-rising-tilde/typeerror-logger-find-caller-takes-from-0-to-1-positional-arguments-but-2-were-given-cb24b74a6125).
2. (Mac only) If you're unable to install Tensorflow v1.14. Use this command:
```bash
pip3 install https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.14.0-py3-none-any.whl
```
3. The model takes roughly 30 minutes to train (`train.py`) and creates two new folders each time you run it: 
   1. `checkpoints_(epoch)`
   2. `trained_results_(epoch)`

  
## Reference

- [Implement a cnn for text classification in tensorflow](http://www.wildml.com/2015/12/implementing-a-cnn-for-text-classification-in-tensorflow/)
