# tensor : 张量，多维数组
import tensorflow as tf 
import numpy as np 


a = tf.constant([1, 5], dtype=tf.int64)

print('\n\n================== tf2.0 ==================')
print(a)
print(a.dtype)
print(a.shape)

a = np.arange(0, 5)
b = tf.convert_to_tensor(a, dtype=tf.int64)
print(a)
print(b)

a = tf.zeros([2, 3])
b = tf.ones(4)
c = tf.fill([2, 3], 9)
print(a)
print(b)
print(c)

d = tf.random.normal([2, 2], mean=0.5, stddev=1)
e = tf.random.truncated_normal([2, 2], mean=0.5, stddev=1)
print(d)
print(e)

f = tf.random.uniform([2, 2], minval=0, maxval=1)
print(f)

# 强制tensor转换为该数据类型
x1 = tf.constant([1., 2., 3.], dtype=tf.float64)
print(x1)

x2 = tf.cast(x1, tf.int32)
print(x1)
print(x2) 

# 找到张量维度中最大值和最小值
print(tf.reduce_min(x2), tf.reduce_max(x2))

# 计算张量沿着指定维度的平均值，和
x = tf.constant([[1, 2, 3],
                [2, 2, 3]])
print(x)
print(tf.reduce_mean(x))
print(tf.reduce_sum(x, axis=1))

# tf.Variable 将变量标记为‘可训练’
w = tf.Variable(tf.random.normal([2, 2], mean=0, stddev=1))
print(w)

# 四则运算
a = tf.ones([1, 3])
b = tf.fill([1, 3], 3.)
print(a)
print(b)
print(tf.add(a,b))
print(tf.subtract(a, b))
print(tf.multiply(a, b))
print(tf.divide(b, a))

# 平方，次方与开方
a = tf.fill([1, 2], 3.)
print(a)
print(tf.pow(a, 3))
print(tf.square(a))
print(tf.sqrt(a))

# 矩阵乘
a = tf.ones([3, 2])
b = tf.fill([2, 3], 3.)
print(tf.matmul(a, b))

# 切分传入张量，生成输入特征/ 标签对， 构建数据集
features = tf.constant([12, 23, 10, 17])
labels = tf.constant([0, 1, 1, 0])

dataset = tf.data.Dataset.from_tensor_slices((features, labels))
print(dataset)
for element in dataset:
    print(element)

# tf.GradienTape 对指定参数求导运算
with tf.GradientTape() as tape:
    w = tf.Variable(tf.constant(3.0))
    loss = tf.pow(w, 2)
grad = tape.gradient(loss, w)
print(grad)

 # enumerate 是python 内置函数 遍历元素，组成：索引 元素
seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    print(i, element)

# tf.one_hot 独热编码
classes = 3
labels = tf.constant([1, 0, 2])
output = tf.one_hot(labels, depth=classes)
print(output)

# tf.nn.softmax
y = tf.constant([1.01, 2.01, -0.66])
y_pro = tf.nn.softmax(y)
print('After softmax, y_pro is:', y_pro)

# assign_sub 更新参数的值并返回，
#  调用assign_sub前，先用tf.Variable定义变量w为可训练（可自更新）
w = tf.Variable(4)
w.assign_sub(1)
print(w)
 
# tf.argmax 返回张量沿指定维度最大值索引
test = np.array([[1, 2, 3], [2, 3, 4], [5, 4, 3], [8, 7, 2]])
print(test)
print(tf.argmax(test, axis=0))
print(tf.argmax(test, axis=1))

# tf.where(条件语句，真返回A， 假返回B) 
a = tf.constant([1, 2, 3, 1, 1])
b = tf.constant([0, 1, 3, 4, 5])
c = tf.where(tf.greater(a, b), a, b)
print('c:', c)
 
# np.random.RandomState.rand()
rdm = np.random.RandomState(seed=1)
a = rdm.rand()
b = rdm.rand(2, 3)
print('a:', a)
print('b:', b)

# np.vstack() 将两个数组按垂直方向叠加
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.vstack((a, b))
print('c:\n', c)

# np.mgrid[]  .ravel()   np.c_[]
# np.mgrid[起始值： 结束值： 步长， ...]
# x.ravel() 将x变为一维数组
# np.c_[] 使返回的间隔值点配对， np.c_[数组1， 数组2， ...]
x, y = np.mgrid[1:3:1, 2:4:0.5]
grid = np.c_[x.ravel(), y.ravel()]
print('x:', x)
print('y:', y) 
print('grid:\n', grid)


# 损失函数 cross entropy
loss_ce1 = tf.losses.categorical_crossentropy([1, 0], [0.6, 0.4])
loss_ce2 = tf.losses.categorical_crossentropy([1, 0], [0.8, 0.2])
print('loss_ce1:', loss_ce1)
print('loss_ce2:', loss_ce2)

# softmax 与交叉熵结合
y_ = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1],[1, 0, 0], [0, 1, 0]])
y = np.array([[12, 3, 2], [3, 10, 1], [1, 2, 5], [4, 6.5, 1.2], [3, 6, 1]])

y_pro = tf.nn.softmax(y)
loss_ce1 = tf.losses.categorical_crossentropy(y_, y_pro)
loss_ce2 = tf.nn.softmax_cross_entropy_with_logits(y_, y)
print('分步计算的结果：\n', loss_ce1)
print('结合计算的结果: \n', loss_ce2)