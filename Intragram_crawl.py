#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 16:00:00 2020

@author: swsong
"""
#%% import libraries
import os
from os.path import join
import copy
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd

import sklearn

import matplotlib.pyplot as plt
#%%
abalone_path = './taca_sklearn/data/abalone.txt'
column_path = './taca_sklearn/data/abalone_attributes.txt'

abalone_columns = list()
for l in open(column_path):
    abalone_columns.append(l.strip())
    
#%%
data = pd.read_csv(abalone_path, header=None, names=abalone_columns)
#label = data['Sex']