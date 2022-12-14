# -*- coding: utf-8 -*-
"""Summerschool_DT23.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AuYxeRtbDqINV9rl4Oz77IMA0Fr1zMTx
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import mutual_info_classif
from sklearn.feature_selection import SelectKBest

df = pd.read_csv("/content/winequalityN.csv")

df.head(10)

df.info()

df.quality.unique()

df['type'].unique()

df.fillna(data.mean())

df = df.fillna(0)

df['type'] = np.where(df['type'] == 'red', 1, 0)
df.head()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df.drop('quality', axis=1), df['quality'], test_size=0.3, random_state=0)

X_train.head()

from sklearn.feature_selection import mutual_info_classif

# Determine the mutual information
mutual_info = mutual_info_classif(X_train, y_train)
mutual_info

mutual_info = pd.Series(mutual_info)
mutual_info.index = X_train.columns
mutual_info.sort_values(ascending = False)

mutual_info.sort_values(ascending=False).plot.bar(figsize=(12, 6))

from sklearn.feature_selection import SelectKBest

sel_6_cols = SelectKBest(mutual_info_classif, k=6)
sel_6_cols.fit(X_train, y_train)
X_train.columns[sel_6_cols.get_support()]



