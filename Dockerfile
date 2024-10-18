# 使用 Python 3.7 作為基礎映像
FROM python:3.7-slim

# 設定工作目錄
WORKDIR /app

# 複製當前目錄下所有檔案到 Docker 容器的 /app 資料夾
COPY . .

# 安裝所需的 Python 套件
RUN pip install --no-cache-dir yfinance

# 創建存放 pickle 文件的資料夾
RUN mkdir -p /data

# 設定容器啟動時執行的指令
CMD ["python", "python main.py --stock 0050 --date 20240918"]