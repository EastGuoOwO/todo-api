# Todo API

一个基于 Python、FastAPI 和 SQLite 实现的待办事项 REST API 项目，用于学习后端开发、HTTP 接口设计和数据库操作。

## 功能特性

* 创建待办事项
* 查询待办事项列表
* 根据 ID 查询单个待办事项
* 更新待办事项
* 删除待办事项
* 使用 SQLite 持久化保存数据
* 使用 Pydantic 进行请求参数校验
* 对不存在的任务返回 HTTP 404
* 支持通过查询参数限制列表返回数量

## 技术栈

* Python
* FastAPI
* Pydantic
* SQLite
* Git / GitHub

## 项目结构

```text
todo_api/
├── main.py
├── database.py
├── crud.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 环境要求

* Python 3.10 或更高版本
* pip

## 安装与运行

### 1. 克隆项目

```bash
git clone https://github.com/EastGuoOwO/todo-api.git
cd todo-api
```

### 2. 安装依赖

```bash
python -m pip install -r requirements.txt
```

### 3. 启动服务

```bash
fastapi dev main.py
```

启动后访问：

* API 文档：http://127.0.0.1:8000/docs
* 服务地址：http://127.0.0.1:8000

首次运行时，项目会初始化 SQLite 数据库和任务表。

## API 接口

| Method | Endpoint           | Description |
| ------ | ------------------ | ----------- |
| POST   | `/tasks`           | 创建任务        |
| GET    | `/tasks`           | 获取任务列表      |
| GET    | `/tasks/{task_id}` | 获取指定任务      |
| PUT    | `/tasks/{task_id}` | 更新任务        |
| DELETE | `/tasks/{task_id}` | 删除任务        |

### 创建任务示例

请求：

```http
POST /tasks
Content-Type: application/json
```

请求体：

```json
{
  "title": "学习 FastAPI"
}
```

响应示例：

```json
{
  "id": 1,
  "title": "学习 FastAPI"
}
```

### 查询任务列表

```http
GET /tasks?limit=10
```

`limit` 用于限制返回的任务数量，默认值为 10，且必须大于或等于 1。

## 学习收获

通过本项目实践了：

* FastAPI 路由与 HTTP 请求处理
* 请求参数和请求体校验
* REST API 的基本设计
* SQLite 数据库连接、SQL 查询与事务提交
* CRUD 操作与代码模块化
* Git 版本管理及 GitHub 项目托管

## 后续计划

* 进一步完善自动化测试
* 学习数据库连接与事务管理
* 在后续项目中实践大模型 API 调用与 AI 应用开发
