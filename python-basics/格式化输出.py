"""
1.准备数据
2.格式化符号输出数据
"""

age = 18
name = 'jack'
weight = 65.8
stu_id = 1
stu_id2 = 1001

# 1.今年我的年龄是18岁
print('今年我的年龄是%d岁' % age)

# 2.我的名字是
print('我的名字是%s' % name)

# 3.我的体重是65公斤
print('我的体重是%.2f公斤' % weight)

# 4.我的学号是
print('我的学号是%d' % stu_id)
# 4.1.我的学号是001。不足补全，多了原样输出
print('我的学号是%03d' % stu_id)
print('我的学号是%03d' % stu_id2)

# 5.我的名字是 ，今年 岁了
print('我的名字是%s，今年%d岁了' % (name, age))

# 6.我的名字是  ，今年 岁了，体重 公斤，学号是
print('我的名字是%s，今年%d岁了，体重%.2f公斤，学号是%03d' % (name, age, weight, stu_id))
