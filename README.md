# spj
shioaji test project
# 股票數據 Pickle 生成器
此專案使用 Docker 與永豐 Shioaji API 來自動下載指定股票代號及日期的數據，並將其保存為 pickle 文件到 `/data` 資料夾中。

## 使用說明
1. 構建 Docker 映像
首先，在專案根目錄下運行以下命令來構建 Docker 映像：
docker build -t stock-pickle-generator .

2. 運行 Docker 容器
構建完成後，使用以下命令來運行 Docker 容器並生成股票數據的 pickle 文件：
docker run -v ${PWD}/data:/data stock-pickle-generator python fdata.py --stock <股票代號> --date <日期>
例如:docker run -v ${PWD}/data:/data stock-pickle-generator python fdata.py --stock 2330 --date 2024-01-01

3. 確認生成的 pickle 文件
容器運行完成後，檢查本地的 ./data/ 資料夾，你會看到一個 pickle 文件，其中包含了指定股票的數據。

4.讀取pkl檔案
執行rd.py檔案

