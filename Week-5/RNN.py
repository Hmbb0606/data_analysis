# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm

#任务：学习循环神经网络以及编程实现
#视频链接：https://www.bilibili.com/video/BV1dq4y1f7ep/?spm_id_from=333.788&vd_source=a9d4cc072fbb58f49a6c86cb62556651


from tensorflow.keras.datasets import imdb
from tensorflow.keras import preprocessing
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense, Embedding

max_feature = 10000  # 总共的词汇量
maxlen = 500  # 在500个单词以后截断文本,不足500则补0

(input_train, y_train), (input_test, y_test) = imdb.load_data(num_words=max_feature)

input_train = preprocessing.sequence.pad_sequences(input_train, maxlen=maxlen)
input_test = preprocessing.sequence.pad_sequences(input_test, maxlen=maxlen)
# 此处相当于对齐序列（补0或者阶段评论）
# print('input_train shape:', input_train.shape)
# print('input_test shape:', input_test.shape)

# 词嵌入操作:降低输入向量维度
embedding_dim = 32
model = Sequential()
model.add(Embedding(max_feature, embedding_dim, input_length=maxlen))
# 第一层是Embedding层，设定字典里10000个单词，Embedding层的输出是个500×32的矩阵，
# 只考虑每条电影评论中最后的500个单词，每个单词用32维的向量来表示
# 参数矩阵在此的维度是320000，矩阵的参数根据设定的每个单词表示的向量（32）*字典词个数10000得到


state_dim = 32
model.add(SimpleRNN(state_dim, return_state=False)) #False 只输出最后一层
model.add(Dense(1, activation='sigmoid')) #units代表该层的输出维度或神经元个数,此处设定输出的维度为1
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(input_train,
                    y_train,
                    epochs=10,
                    batch_size=128,
                    validation_split=0.2
                )
model.summary()
loss_and_acc = model.evaluate(input_test, y_test)
print('loss=' + str(loss_and_acc[0]))
print('acc=' + str(loss_and_acc[1]))
