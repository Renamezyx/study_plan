# Pythonic 写法 — 列表推导式、生成器表达式、解包（一行提取 CSV 第 3 列）
notes = """
(x % 3 for x in range(100)) 生成器表达式 占用较小内存 生成器
[x % 3 for x in range(100)] 列表推导式 占用较多内存 一次性加载
{x % 3 for x in range(100)} 集合推导式 惰性 且去重 一次性加载 
"""

a = (x % 3 for x in range(100))
b = [x % 3 for x in range(100)]
c = {x % 3 for x in range(100)}

print(a)
print(b)
print(c)
