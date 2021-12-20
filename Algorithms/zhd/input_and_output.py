# 输入，input()方法,
# 数据的处理通常依赖于strip()方法和split()方法。
# strip():去掉字符串首尾的指定字符，默认为换行符和空格。
# split():以某个字串或者字符拆分已有的字符串，默认情况以空格拆分。
# a = 'abc_dr'
# print(a.split('_')[-1])  # dr
# 读取一行
line = list(map(float, input().strip().split()))
print(line)
# 读取多行，指定行数
n, m = map(int, input().strip().split())
lit = []
for i in range(n):
    lit.append(list(map(float, input().strip().split())))
print(lit)
# 读取多行，不指定行数
lis = []
while True:
    line = input().strip()
    if line == '':
        break
    lines = list(map(float, line.split()))
    lis.append(lines)
print(lis)
# 2 5
# -1.739623 -4.587115 -4.286510 4.015947 -2.671629
# 2.323935 3.158164 -3.211263 2.444232 -0.413941

