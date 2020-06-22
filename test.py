#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 22:03:20 2020

@author: swsong
"""


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
import numpy as np
import seaborn as sns
import statsmodels
sns.set(style='whitegrid')
%matplotlib inline
#%%
rs = np.random.RandomState(7) #여러번 출력해도 고정값
x = rs.normal(2, 1, 75)
y = 2 + 1.5 * x + rs.normal(0, 2, 75)
#%%
#산점도 그리기
sns.scatterplot(x=x, y=y, color='g')
#%%
#회귀선 그리기
sns.regplot(x=x,y=y, color='g')
#%%
#선이 가중치에 따라 구부러질 수 있도록 옵션값
#lowess = locally weighted robust scatter plot smoothing
sns.regplot(x=x,y=y, color='g', lowess=True)
#pip install statsmodels 해줘야 동작함.
#%%
#영점을 기준으로 수평회전시켜 +/- 상관관계를 확인할 때 residplot 활용 
sns.residplot(x, y, color='g', lowess=True)

