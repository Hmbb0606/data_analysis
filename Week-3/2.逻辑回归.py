# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm

# 逻辑回归解决的分类问题
# 逻辑回归 = 线性回归 + Sigmoid
# 线性回归的结果经过Sigmoid函数输出 映射到0-1之间的某一个数字

import numpy as np
'''
以下有四个类别字典，第一个为多分类的字典，后面三个为二分类的字典
'''
# 进行多分类时的类字典
classDict = {'自行车': 0, '电动车': 1, '步行': 2}

# 将类别字典的key和value对调
def getIndexDict(classDict):
    indexDict = {}
    for key, value in classDict.items():
        indexDict[value] = key
    return indexDict

# sigmoid函数
def sigmoid(x):
    try:
        return 1.0 / (1 + np.exp(-x))
    except:
        return 0.0  # 溢出时返回0.0


# 随机梯度上升算法
# 要找到某函数的最大值，最好的方法是沿着该函数的梯度方向探寻
# 由于logistic算法中使用的损失函数是计算样本分类正确的概率，分类正确的概率越大越好，
# 因而该损失函数的值也是越大越好。
# 所以在logistic算法中我们使用梯度上升法来最大化该损失函数。
def stocGradAscent(xMat, classLabels, numIter=150):
    '''
    Parameters:
        xMat: 输入样本矩阵
        classLabels:输入样本类别标签
        numIter:随机梯度上升算法迭代次数
    '''
    m, n = np.shape(xMat)  # m：样本个数，n：特征数+1(类别数)
    w = np.ones(n)  # 初始化一个全1矩阵
    for j in range(numIter):  # 迭代
        dataIdx = list(range(m))  # 生成样本索引列表
        for i in range(m):  # 随机遍历一遍样本集
            alpha = 4 / (1.0 + j + i) + 0.01  # 步长，不断变化
            randIdx = int(np.random.uniform(0, len(dataIdx)))  # 随机生成一个样本索引
            # 取出对应样本与w做线性运算，求和后通过sigmoid函数生成0-1之间的一个数字
            h = sigmoid(sum(xMat[dataIdx[randIdx]] * w))
            err = classLabels[dataIdx[randIdx]] - h  # 计算真实类别(0或1)与预测出数字的差异

            w = w + alpha * err * xMat[dataIdx[randIdx]]  # 更新权重

            del (dataIdx[randIdx])  # 删除已访问过的索引

    return w


# 根据权重w对样本x做分类
def classifyVector(x, w):
    prob = sigmoid(sum(x * w))  # 线性模型后经过sigmoid函数值为0-1之间，视为概率
    if prob > 0.5:
        return 1.0  # 概率＞0.5时为正类，否则为负类
    else:
        return 0.0


# 统计每个类别的个数，返回出现次数多的类别
def majorityCnt(classList):
    # 类别计数器
    classCount = {}
    for c in classList:
        if c not in classCount.keys():
            classCount[c] = 0
        classCount[c] += 1
    # reverse = True 从大到小排列，key x[1]指比较key、value中的value
    sortedClassCount = sorted(classCount.items(), key=lambda x: x[1], reverse=True)
    return sortedClassCount[0][0]


# 进行多分类或二分类测试
# 一个多分类问题可以分解成多个二分类的问题。
# 我们可以将n分类问题分解为n(n-1)/2个二分类问题。

def test(fileName='', numIter=150, trainRatio=0.8):
    '''
    Parameters:
        fileName:数据集所在文件
        numIter:迭代次数
        trainRatio:训练集占数据集比例
    Returns:
        errRate:错误率
    '''

    allData = open(fileName)  # 打开文件
    allSet = []  # 记录所有数据
    allLab = []  # 记录所有数据的类别
    lines = allData.readlines()  # 获取文件中所有内容
    head = lines[0].strip().split(',')  # 得到第一行
    data = lines[1:]  # 第一行是抬头，剩余第二行开始的所有数据
    numFeatures = len(head) - 1  # 特征个数，减去的是类别那一列

    for line in data:  # 遍历每行数据
        curLine = line.strip().split(',') #遇到逗号跳过
        lineArr = []  # 记录处理后的每行数据
        for i in range(numFeatures):  # 遍历每个样本的四列特征
            lineArr.append(0 if curLine[i] == '?' else float(curLine[i]))  # 缺失数据补为0
        allSet.append(lineArr)  # 将处理后的样本加入样本全集中
        # print(allSet)
        label = curLine[numFeatures]  # 当前样本类别
        allLab.append(classDict[label])  # 加入标签，numFeatures为类别下标

    '''此时数据全部获取到变量当中'''

    # 划分训练集与测试集
    numExamples = len(data)  # 样本总数
    numTrain = int(numExamples * trainRatio)  # 根据训练集的比例得出训练集总数
    numTest = numExamples - numTrain  # 测试集总数

    trainSet = np.array(allSet[:numTrain])  # 共21个样本,前14个用作训练,后7个用于预测
    trainLab = np.array(allLab[:numTrain])
    testSet = np.array(allSet[numTrain:])
    testLab = np.array(allLab[numTrain:])

    labels = set(trainLab)  # 去重样本标签集合
    trainW = []  # 记录每个分类器的权重
    labelPairs = []  # 记录每个分类器对应的0、1原类别
    for label1 in labels:  # 对于二分类，由于labels中只有两个元素，只有一个分类器
        for label2 in labels:  # 对于多分类，labels中有多个元素，两两元素之间有一个分类器
            if label1 >= label2:  # 只允许label1 < label2
                continue
            labelPairs.append([label1, label2])  # 记录当前的两个类别
            curTrainLabels = []  # 记录标签全集中是当前两个类别的子集标签
            curTrainSet = []  # 记录样本全集中是当前两个类别的子集样本

            # 遍历每个训练样本，如果属于当前选择的两个类别
            # 则将该样本与该样本的标签记录下来
            for i in range(numTrain):
                if trainLab[i] == label1 or trainLab[i] == label2:
                    if trainLab[i] == label1:  # 属于二分类中的'0'类别
                        curTrainLabels.append(0)
                    if trainLab[i] == label2:  # 属于二分类中的'1'类别
                        curTrainLabels.append(1)
                    curTrainSet.append(trainSet[i])

            # 对当前分类器通过梯度上升求回归系数
            curTrainW = stocGradAscent(curTrainSet, curTrainLabels, numIter)
            trainW.append(curTrainW)  # 记录当前分类器的回归系数

    # ----------------------------- 预测样本集 ------------------------------

    predLab = []  # 记录预测结果
    errCount = 0.0  # 记录预测错误个数
    numClassifiers = len(labelPairs)  # 分类器的数目
    indexDict = getIndexDict(classDict)  # 将类别字典的key与value对调

    # 当执行二分类且类别字典中的类别大于2种时，定义负类的名字就为正类的名字前加个“非”字
    if numClassifiers == 1 and len(classDict.items()) > 2:
        indexDict[0] = '非' + indexDict[1]

    for i in range(numTest):  # 依次计算每个预测样本
        curPreLab = []  # 当前预测类别
        for j in range(numClassifiers):  # 遍历每个分类器对预测样本进行预测
            curPartPreLab = classifyVector(testSet[i], trainW[j])  # 预测类别
            curPartPreLab = labelPairs[j][int(curPartPreLab)]  # 将预测的0、1类别还原为原类别
            curPreLab.append(curPartPreLab)  # 记录当前分类器预测类别
        curPreLab = majorityCnt(curPreLab)  # 统计每个分类器的预测结果，找出预测次数最大的类别
        predLab.append(curPreLab)  # 记录当前样本预测类别
        print("分类预测类别为：%s, 真实类别为：%s" % (indexDict[curPreLab], indexDict[testLab[i]]))
        if curPreLab != testLab[i]:  # 如果预测类别!=实际类别，错误量+1
            errCount += 1.0
    errRate = float(errCount) / numTest  # 错误率
    print('错误率为：%f， 总测试集样本数为：%d，预测错误数为:%d' % (errRate, numTest, errCount))
    return errRate


if __name__ == '__main__':
    minErrRate = 100  # 记录最小错误率
    bestNumIter = 0  # 记录最佳迭代次数
    for numIter in range(50, 200, 10):  # 试验不同迭代次数对算法的影响
        curErrRate = test(fileName='./data/time.csv', numIter=numIter, trainRatio=0.67)

        if curErrRate < minErrRate:  # 记录最小错误率以及最佳迭代次数
            minErrRate = curErrRate
            bestNumIter = numIter
    print('最佳训练时迭代次数为%d次， 最小错误率为%f' % (bestNumIter, minErrRate))
