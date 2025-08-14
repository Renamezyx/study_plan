# 数据结构底层 — list/dict/set 内存结构、时间复杂度（用 dict 模拟 LRU 缓存）
"""
LRU 缓存
给一个长度的空间
当容量满时，删除最早插入（或最久未访问）的元素。
每次访问（get）时，把元素移动到末尾表示最近使用。
"""


class LRU:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key):
        if key not in self.cache:
            raise KeyError(key)
        else:
            v = self.cache.pop(key)
            self.cache[key] = v

    def put(self, key, val):
        if key in self.cache:
            self.cache.pop(key)
        if len(self.cache) >= self.capacity:
            # 淘汰最旧的 key
            oldest_key = next(iter(self.cache))
            self.cache.pop(oldest_key)
        self.cache[key] = val


notes = """
next(iter(dict_obj)) 等价 list(dict_obj.keys())[0]
next(iter(dict_obj)) 更加快速 节省空间
"""
