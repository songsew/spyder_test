#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 22:08:56 2020

@author: swsong
"""

#%% 필요한 라이브러리 로드
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#%% 데이터셋 로드(flight)
df = sns.load_dataset("flights")
df.shape #크기파악
df.head() #ipython console로 실행해보기

#%% barplot 시각화
plt.figure(figsize=(15, 4))
sns.barplot(data=df, x='year', y='passengers') #Plots

#%% lineplot
plt.figure(figsize=(15, 4))
sns.lineplot(data=df, x='year', y='passengers')

#%% pointplot
plt.figure(figsize=(15, 4))
sns.pointplot(data=df, x='year', y='passengers', ci="sd") #sd = standard deviation(표준편차)

#%% lineplot에 월별로 다르게 색상그리기
plt.figure(figsize=(15, 4))
sns.lineplot(data=df, x='year', y='passengers', hue='month')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.1)
# legend는 lineplot을 그리고 난 후(순서 중요) 설정해줘야 정상적으로 동작

#%% month와 year를 바꿔보자(hue='year')
plt.figure(figsize=(15, 4))
sns.lineplot(data=df, x='month', y='passengers', hue='year')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.1)

#%% boxplot
plt.figure(figsize=(15,4))
sns.boxplot(data=df, x='year', y='passengers')

#%% boxenplot
plt.figure(figsize=(15,4))
sns.boxenplot(data=df, x='year', y='passengers')

#%% violinplot
plt.figure(figsize=(15,4))
sns.violinplot(data=df, x='year', y='passengers')

#%% swarmplot
plt.figure(figsize=(15,4))
sns.swarmplot(data=df, x='year', y='passengers')

#%% boxplot, x='month'
plt.figure(figsize=(15,4))
sns.boxplot(data=df, x='month', y='passengers')

#%% violinplot, x='month'
plt.figure(figsize=(15,4))
sns.violinplot(data=df, x='month', y='passengers')

#%% regplot
plt.figure(figsize=(15,4))
sns.regplot(data=df, x='year', y='passengers')
























