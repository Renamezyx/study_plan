# Python 4 周训练计划

## 第 1 周：语言进阶 & Pythonic 思维
- [x] 1. 数据结构底层 — list/dict/set 内存结构、时间复杂度（用 dict 模拟 LRU 缓存）
- [x] 2. 迭代器与生成器 — iter() / next() / yield / yield from（可分页生成器读取大文件）
- [x] 3. 装饰器与闭包 — functools.wraps（统计函数执行时间装饰器）
- [x] 4. 上下文管理器 — __enter__ / __exit__（自动计时并记录日志的类）
- [x] 5. Pythonic 写法 — 列表推导式、生成器表达式、解包（一行提取 CSV 第 3 列）
- [x] 6. 标准库精通 — collections / itertools / functools（按日期聚合数据）
- [x] 7. 总结 + 练习 — 刷 5 道 LeetCode Easy（普通写法 vs Pythonic 写法）

## 第 2 周：工程化能力
- [x] 8. 项目结构 — 包与模块、入口文件（三层结构 CLI 项目）
- [x] 9. 依赖管理 — Poetry / venv / requirements（Poetry 创建项目并锁版本）
- [x] 10. 测试框架 — pytest、mock、参数化（3 个单元测试）
- [x] 11. 格式化工具 — black / isort / flake8 / pre-commit（自动检查）
- [x] 12. 日志与配置 — logging / .env / pydantic（日志 & 配置管理）
- [x] 13. 异常处理 — 自定义异常、分层捕获（统一异常处理器）
- [x] 14. 总结 — CLI 项目打包可执行文件（pyinstaller）

## 第 3 周：设计模式与业务建模
- [x] 15. 单例模式 — 应用场景、线程安全（全局配置单例类）
- [ ] 16. 工厂模式 — 简化对象创建（消息发送器工厂 Email/SMS）
- [ ] 17. 策略模式 — 动态切换算法（折扣计算策略）
- [ ] 18. 装饰器模式 — 动态增强功能（API 权限验证装饰器）
- [ ] 19. 观察者模式 — 事件驱动（事件总线）
- [ ] 20. DDD 概念 — 领域模型、值对象、聚合根（任务系统模型）
- [ ] 21. 总结 — 模式组合项目（任务系统 + 策略 + 事件驱动）

## 第 4 周：架构设计与实战
- [ ] 22. 分层架构 — Controller / Service / Repository（用户系统三层架构）
- [ ] 23. 模块拆分 — 高内聚、低耦合（用户系统独立包）
- [ ] 24. API 设计 — REST / GraphQL（FastAPI 用户 CRUD）
- [ ] 25. 数据访问层 — ORM 封装（SQLAlchemy）
- [ ] 26. 异步任务 — Celery / asyncio（注册后异步发送邮件）
- [ ] 27. 中间件设计 — 请求日志、认证（API 全局中间件）
- [ ] 28. 总结 — 部署上线（Docker 部署）
## Notes
```shell
next(iter(dict_obj)) 等价 list(dict_obj.keys())[0]
next(iter(dict_obj)) 更加快速 节省空间
```

```shell
如果函数内部使用了 yield，这个函数就不再是普通函数，而是生成器函数
调用这个函数 不会立即执行函数体，而是返回一个生成器对象（iterator）
每次调用 next() 或在 for 循环中迭代时，函数从上一次 yield 停下的地方继续执行
yield 相当于“返回一个值，同时记住函数执行状态”
```

```shell
闭包是嵌套函数的组合：
外层函数返回内层函数
内层函数可以访问外层函数的局部变量，即使外层函数已经执行结束
```

```shell
上下文管理器协议 
__enter__ / __exit__ 只有配合with语句才会自动调用
__exit__ 会自动传入参数 
    exc_type：异常的类型（无异常时是 None）
    exc_val：异常实例（无异常时是 None）
    exc_tb：traceback 对象（无异常时是 None）
    如果 __exit__ 返回 True，Python 会吞掉异常，不再向外抛， False 则会继续外抛
```

```shell
(x % 3 for x in range(100)) 生成器表达式 占用较小内存 生成器
[x % 3 for x in range(100)] 列表推导式 占用较多内存 一次性加载
{x % 3 for x in range(100)} 集合推导式 惰性 且去重 一次性加载
```

```shell
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
```

