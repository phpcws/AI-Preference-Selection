# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 12:30:58 2020

@author: yjw
"""

import numpy as np
import matplotlib.pyplot as plt
import xlrd
from math import log 
N = 101
D = 2
K = 4
X = np.zeros((N, D))
y = np.zeros(N, dtype='uint8')
data = xlrd.open_workbook('4.xlsx')
table = data.sheet_by_index(0)
x1=table.col_values(1,3)
x2=table.col_values(2,4)
v=table.col_values(3,5)
x1 = [x/1000000 for x in x1]
x2 = [x/1000000 for x in x2]
y1=[]
for i in v:
    if i =='A':
        y1.append(0)
    if i=='B':
        y1.append(1)
    if i=='C':
        y1.append(2)
    if i=='D':
        y1.append(3)
for ix in range(0,100):
    X[ix] = np.c_[x1[ix], x2[ix]]
    y[ix] = y1[ix]
# 初始化权重和偏置
h = 100 # 隐藏层的神经元数量

# 第一个层的权重和偏置初始化
W1 = 0.01 * np.random.randn(D, h)
b1 = np.zeros((1, h))

# 第二层的权重和偏置初始化
W2 = 0.01 * np.random.randn(h, K)
b2 = np.zeros((1, K))

step_size = 1e-0
reg = 1e-3 # regularization strength

# 获取训练样本数量
num_examples = X.shape[0]
for i in range(20000):

    # 计算第一个隐藏层的输出，使用ReLU激活函数
    hidden_layer = np.maximum(0, np.dot(X, W1) + b1)
    # 计算输出层的结果，也就是最终的分类得分
    scores = np.dot(hidden_layer, W2) + b2
    
    # softmax
    exp_scores = np.exp(scores)
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True) # [N x K]
  
    # 计算损失，和之前的一样
    correct_logprobs = -np.log(probs[range(num_examples),y])
    data_loss = np.sum(correct_logprobs)/num_examples
    reg_loss = 0.5*reg*np.sum(W1*W1) + 0.5*reg*np.sum(W2*W2)
    loss = data_loss + reg_loss
    
    if i % 1000 == 0:
        print ("iteration %4d loss %f" % (i, loss))
  
    # 计算scores的梯度
    dscores = probs
    dscores[range(num_examples),y] -= 1
    dscores /= num_examples
  
    # 计算梯度，反向传播
    dW2 = np.dot(hidden_layer.T, dscores)
    db2 = np.sum(dscores, axis=0, keepdims=True)
    
    # 反向传播隐藏层
    dhidden = np.dot(dscores, W2.T)
    # 反向传播ReLu函数
    dhidden[hidden_layer <= 0] = 0
    
    dW1 = np.dot(X.T, dhidden)
    db1 = np.sum(dhidden, axis=0, keepdims=True)
    
    # 加上正则项
    dW2 += reg * W2
    dW1 += reg * W1
    
    # 更新参数
    W1 += -step_size * dW1
    b1 += -step_size * db1
    W2 += -step_size * dW2
    b2 += -step_size * db2

# 训练结束，估算正确率
hidden_layer = np.maximum(0, np.dot(X, W1) + b1)
scores = np.dot(hidden_layer, W2) + b2
predicted_class = np.argmax(scores, axis=1)
print("Training accuracy: %.2f" % (np.mean(predicted_class == y)))