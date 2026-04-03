# Base image
FROM python:3.12-slim

# 2. 设置容器内的工作目录
WORKDIR /app

# 3. 复制依赖清单到容器
COPY requirements.txt .

# 4. 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 5. 复制当前目录下的所有代码到容器
COPY . .

# Runtime env (avoid .pyc, flush logs)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 7. 暴露 5000 端口
EXPOSE 5000

# 8. 启动命令
# Production entrypoint uses gunicorn (instead of app.run())
# 'project:app' means: project.py exports a variable named `app`
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "project:app"]
