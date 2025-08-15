# 迭代器与生成器 — iter() / next() / yield / yield from（可分页生成器读取大文件）

def read_file_in_chunks(file_path, chunk_size=100):
    chunk = []
    with open(file_path, 'r', encoding="utf-8") as file:
        for index, line in enumerate(file, 1):
            chunk.append(line.strip())
            if index % chunk_size == 0:
                yield chunk
                chunk = []
        if chunk:
            yield chunk


notes = """
如果函数内部使用了 yield，这个函数就不再是普通函数，而是生成器函数
调用这个函数 不会立即执行函数体，而是返回一个生成器对象（iterator）
每次调用 next() 或在 for 循环中迭代时，函数从上一次 yield 停下的地方继续执行
yield 相当于“返回一个值，同时记住函数执行状态”
"""
