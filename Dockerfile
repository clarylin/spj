# 使用 Python 3.7 作為基礎映像
FROM python:3.7-slim

# 設定工作目錄
WORKDIR /app

# 複製當前目錄下所有檔案到 Docker 容器的 /app 資料夾
COPY . .

# 安裝所需的 Python 套件
RUN pip install --no-cache-dir pandas shioaji shioaji[speed]

# 創建存放 pickle 文件的資料夾
RUN mkdir -p /data



# 安裝必要的依賴項
RUN apt-get update && apt-get install -y cron
# 複製 Python 文件到容器中
COPY fdata2.py .
# 添加 Cronjob 設置
RUN echo "*/5 * * * * python /app/fdata2.py >> /var/log/cron.log 2>&1" > /etc/cron.d/fdata2-cron

# 設置權限
RUN chmod 0644 /etc/cron.d/fdata2-cron

# 應用 Cronjob
RUN crontab /etc/cron.d/fdata2-cron

# 設定容器啟動時執行的指令
# 啟動 Cron 並保持前台運行
CMD ["python", "generate_stock_pickle.py"] ["sh", "-c", "cron && tail -f /var/log/cron.log"]