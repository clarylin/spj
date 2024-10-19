# 股票數據 Pickle 生成器
shioaji test project-fdata.py此專案使用 Docker 與永豐 Shioaji API 來自動下載指定股票代號及日期的數據，並將其保存為 pickle 文件到 `/data` 資料夾中。

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

# 自動化交易系統
shioaji test project-fdata2.py
本專案是基於永豐 Shioaji API 實現的自動化台指期貨交易系統，通過定時從 API 獲取加權指數與台指期貨的價格，根據預設的交易策略自動執行下單。整個系統運行於 Docker 容器中，並且通過 cronjob 定時觸發下單腳本。

#環境需求
Docker
永豐 Shioaji API 金鑰（API_KEY 和 API_SECRET）
#依賴安裝
Shioaji 是永豐證券提供的 API，用於程式化交易。你需要提前申請 API 金鑰和密碼，並使用它們進行程式登錄。
本專案所需的主要 Python 依賴：
1.shioaji：永豐證券 API 套件
2.cron：定時任務工具

#如何構建 Docker 映像
在專案目錄下運行以下命令來構建 Docker 映像：docker build -t fdata2-bot .這條命令會根據 Dockerfile 構建一個包含 Python 3.7、Shioaji API 和定時任務的 Docker 映像。

#如何運行 Docker 容器
構建好映像後，運行以下命令來啟動 Docker 容器：docker run -d --name fdata2-bot -e API_KEY="your_api_key" -e API_SECRET="your_api_secret" fdata2-bot
請將 your_api_key 和 your_api_secret 替換為你自己的永豐 API 金鑰和密碼。
這些憑據將被用於自動化交易系統的 API 登錄。

#如何設置帳號與密碼
申請永豐 Shioaji API：你需要向永豐證券申請 API 金鑰（API_KEY）和 API 密碼（API_SECRET）。
配置環境變數： 當你運行 Docker 容器時，可以通過環境變數傳入 API 金鑰和密碼。運行容器的時候使用 -e 參數來設置：
docker run -d --name fdata2-bot -e API_KEY="your_api_key" -e API_SECRET="your_api_secret" fdata2-bot
在 Python 中登錄： Docker 容器內的 fdata2.py 文件中會自動使用這些環境變數來登錄：
import os
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

#登錄API
api.login(api_key, api_secret)
這樣配置後，Docker 容器內的 Python 腳本將會使用你提供的 API 金鑰和密碼進行登錄，並自動化執行交易。





