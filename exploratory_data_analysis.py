import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

reds_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
whites_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'

red_wine_data = pd.read_csv(reds_url, delimiter = ';')
white_wine_data = pd.read_csv(whites_url, delimiter = ';')