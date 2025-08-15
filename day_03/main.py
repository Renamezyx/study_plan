# 装饰器与闭包 — functools.wraps（统计函数执行时间装饰器）
import functools
import time

notes = """
闭包是嵌套函数的组合：
外层函数返回内层函数
内层函数可以访问外层函数的局部变量，即使外层函数已经执行结束
"""


def outer(msg):
    def inner():
        print(f"消息: {msg}")  # inner 可以访问 outer 的局部变量

    return inner


func = outer("Hello, World!")
func()  # 输出: 消息: Hello, World!


def timing(func):
    # 使用装饰器后，原函数的__name__、__doc__  会被 wrapper 覆盖
    # functools.wraps(func)会把原函数的元信息复制到wrapper上
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 执行时间: {end - start:.4f} 秒")
        return result
    return wrapper


@timing
def compute(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total


compute(1000000)
