# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm

# LSTM是对SimpleRNN的改进
# LSTM使用梯度带避免梯度消失的问题
# 视频链接：https://www.bilibili.com/video/BV1UK4y1d7xa/?spm_id_from=333.788&vd_source=a9d4cc072fbb58f49a6c86cb62556651

#LSTM有遗忘门、输入门、单元状态门、输出门

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
#屏蔽tensorflow2的方法
tf.compat.v1.disable_eager_execution()
import pandas as pd
import matplotlib.pyplot as plt


# Mnist数据集加载
(x_train_all, y_train_all), (x_test, y_test) = keras.datasets.mnist.load_data()

# Mnist数据集简单归一化
x_train_all, x_test = x_train_all / 255.0, x_test / 255.0

x_train, x_test = x_train_all[:50000], x_train_all[50000:]
y_train, y_test = y_train_all[:50000], y_train_all[50000:]
print(x_train.shape)

# 构建模型
inputs = layers.Input(shape=(x_train.shape[1], x_train.shape[2]), name='inputs')
print(inputs.shape)
lstm = layers.LSTM(units=128, return_sequences=False)(inputs)
print(lstm.shape)
outputs = layers.Dense(10, activation='softmax')(lstm)
print(outputs.shape)
lstm = keras.Model(inputs, outputs)

# 查看模型
lstm.compile(optimizer=keras.optimizers.Adam(0.001),
             loss='sparse_categorical_crossentropy',
             metrics=['accuracy'])
lstm.summary()

# 训练模型
history = lstm.fit(x_train, y_train, batch_size=32, epochs=50, validation_split=0.1)


# 绘制准确率图像
data = {}
data['accuracy'] = history.history['accuracy']
data['val_accuracy'] = history.history['val_accuracy']
pd.DataFrame(data).plot(figsize=(8, 5))
plt.grid(True)
plt.axis([0, 30, 0, 1])
plt.show()

# 绘制损失图像
data = {}
data['loss'] = history.history['loss']
data['val_loss'] = history.history['val_loss']
pd.DataFrame(data).plot(figsize=(8, 5))
plt.grid(True)
plt.axis([0, 30, 0, 1])
plt.show()
