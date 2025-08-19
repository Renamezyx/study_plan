# 单例模式 — 应用场景、线程安全（全局配置单例类）
import threading

notes = """
单例模式的应用场景：
适合“全局只应存在一个实例”的东西, eg：
连接池/客户端：数据库、缓存、消息队列（避免重复昂贵初始化）
统一日志器（尽管 logging 模块已帮你做了类似单例/缓存）
配置中心：如 GlobalConfig（读取 env/文件/远端）

模块是天然的单例
模块只会被导入一次
当你第一次 import xxx 时，Python 会把这个模块加载进内存，并在 sys.modules 里缓存起来。
以后再 import xxx，不会重新执行模块代码，而是直接从 sys.modules 里取缓存的对象。
模块级变量是全局共享的
在模块里定义的变量、类、函数，导入它的所有地方访问到的都是同一份。

class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super.__call__(*args, **kwargs)
        return cls._instances[cls]


class A(metaclass=SingletonMeta):
    # A 也变成了单例模式
    pass

    
'metaclass' 是类的构造工厂
类是对象，类的工厂就是 metaclass
类 → 生产对象；元类 → 生产类
"""


class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super.__call__(*args, **kwargs)
        return cls._instances[cls]


class A(metaclass=SingletonMeta):
    pass


class B(metaclass=SingletonMeta):
    pass


a = A()
a1 = A()
b = B()
b1 = B()
print(id(a), id(a1))
print(id(b), id(b1))
print(a)
print(b)
