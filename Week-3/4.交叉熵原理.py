# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm

# 在交叉熵损失函数中，只有真实类别对应的那一项会被计算在内，其他类别的项在求和过程中均为0
# 即便模型对其他类别的预测概率不准确，但只要对真实类别的预测概率较高，损失函数的值任然较低


# 原文：https://zhuanlan.zhihu.com/p/611507194

import numpy as np

# 定义sigmoid函数
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# 定义交叉熵损失函数
def cross_entropy_loss(y_true, y_pred):
    # y_true是真实标签，y_pred是预测值
    return -(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

# 定义逻辑回归模型
class LogisticRegression:
    def __init__(self, num_features):
        # 初始化权重参数
        self.weights = np.zeros((num_features, 1))
        self.bias = 0
    def fit(self, X, y, learning_rate=0.01, num_iterations=1000):
        # 训练模型
        for i in range(num_iterations):
            # 计算模型预测值
            y_pred = sigmoid(np.dot(X, self.weights) + self.bias)
            # 计算交叉熵损失函数
            loss = np.mean(cross_entropy_loss(y, y_pred))
            # 计算梯度
            dW = np.dot(X.T, (y_pred - y)) / len(y)
            db = np.mean(y_pred - y)
            # 更新权重参数
            self.weights -= learning_rate * dW
            self.bias -= learning_rate * db
            # 打印损失值
            if i % 100 == 0:
                print("Iteration %d, loss: %f" % (i, loss))

    def predict(self, X):
        # 预测样本标签
        y_pred = sigmoid(np.dot(X, self.weights) + self.bias)
        return np.round(y_pred)

if __name__ == '__main__':
    X = np.array([
        [2.0, 70.0, 120.0],
        [3.0, 80.0, 130.0],
        [4.0, 90.0, 140.0],
        [5.0, 100.0, 150.0]
    ])
    y = np.array([0, 0, 1, 1]).reshape(-1, 1)

    # 创建逻辑回归模型
    model = LogisticRegression(num_features=3)

    # 训练模型
    model.fit(X, y, learning_rate=0.1, num_iterations=1000)

    # 预测新样本
    X_new = np.array([[6.0, 110.0, 160.0]])
    y_pred = model.predict(X_new)
    print(y_pred)