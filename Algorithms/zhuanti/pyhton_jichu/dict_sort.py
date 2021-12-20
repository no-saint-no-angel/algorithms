"""
    这个文件的功能是，对字典排序做一个归纳总结。
    1、根据字典的key排序
    2、根据字典的value排序

"""
# 先定义一个字典，首先声明注意一点，本案例中的字典中的值需要为同一种数据类型；比如在本案例中的值都是字符串类型。
sys = {'name': '张三',
       'age': '十八',
       'gender': 'man'}

"""
    根据字典的key排序
"""

#  单独打印出排序后的key值
new_sys = sorted(sys)
print(new_sys)

new_sys = sorted(sys.keys())
print(new_sys)

# 根据key的升序排列，把key value都打印出来
new_sys1 = sorted(sys.items(), key=lambda d: d[0], reverse=False)
print(new_sys1)

new_sys1 = sorted(sys.items(), reverse=False)
print(new_sys1)

"""
    根据字典的value值进行排序
"""
# 单独打印出排序后的value值
new_sys1 = sorted(sys.values())
print(new_sys1)

# 打印出根据value排序后的键值对的具体值
new_sys2 = sorted(sys.items(),  key=lambda d: d[1], reverse=False)
print(new_sys2)
