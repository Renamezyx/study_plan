# Python 4 周训练计划

## 第 1 周：语言进阶 & Pythonic 思维
- [ ] 1. 数据结构底层 — list/dict/set 内存结构、时间复杂度（用 dict 模拟 LRU 缓存）
- [ ] 2. 迭代器与生成器 — iter() / next() / yield / yield from（可分页生成器读取大文件）
- [ ] 3. 装饰器与闭包 — functools.wraps（统计函数执行时间装饰器）
- [ ] 4. 上下文管理器 — __enter__ / __exit__（自动计时并记录日志的类）
- [ ] 5. Pythonic 写法 — 列表推导式、生成器表达式、解包（一行提取 CSV 第 3 列）
- [ ] 6. 标准库精通 — collections / itertools / functools（按日期聚合数据）
- [ ] 7. 总结 + 练习 — 刷 5 道 LeetCode Easy（普通写法 vs Pythonic 写法）

## 第 2 周：工程化能力
- [ ] 8. 项目结构 — 包与模块、入口文件（三层结构 CLI 项目）
- [ ] 9. 依赖管理 — Poetry / venv / requirements（Poetry 创建项目并锁版本）
- [ ] 10. 测试框架 — pytest、mock、参数化（3 个单元测试）
- [ ] 11. 格式化工具 — black / isort / flake8 / pre-commit（自动检查）
- [ ] 12. 日志与配置 — logging / .env / pydantic（日志 & 配置管理）
- [ ] 13. 异常处理 — 自定义异常、分层捕获（统一异常处理器）
- [ ] 14. 总结 — CLI 项目打包可执行文件（pyinstaller）

## 第 3 周：设计模式与业务建模
- [ ] 15. 单例模式 — 应用场景、线程安全（全局配置单例类）
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
## 
```shell
next(iter(dict_obj)) 等价 list(dict_obj.keys())[0]
next(iter(dict_obj)) 更加快速 节省空间

```