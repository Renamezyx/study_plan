# 上下文管理器 — __enter__ / __exit__（自动计时并记录日志的类）
import logging
import time
import traceback

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

class TimerLogger(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.start = time.time()
        logging.info(f"{self.name} 计时开始：{self.start}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        if exc_type:
            logging.error(f"{self.name} 出现异常: {exc_val}")
            print("异常堆栈:")
            print("".join(traceback.format_tb(exc_tb)))
        logging.info(f"{self.name} 计时结束：{self.end}")
        logging.info(f"本次执行耗时 {self.end - self.start} ms")
        return False


with TimerLogger("计算平方和"):
    total = sum(i ** 2 for i in range(1000000))


notes = """
上下文管理器协议 
__enter__ / __exit__ 只有配合with语句才会自动调用嘛
__exit__ 会自动传入参数 
    exc_type：异常的类型（无异常时是 None）
    exc_val：异常实例（无异常时是 None）
    exc_tb：traceback 对象（无异常时是 None）
    如果 __exit__ 返回 True，Python 会吞掉异常，不再向外抛， False 则会继续外抛
"""