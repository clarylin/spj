import shioaji as sj
import pandas as pd
import os
import pickle
import argparse
from datetime import datetime, timedelta

api = sj.Shioaji()
def login():
    api.login(
    api_key="E9oPqAhnU6WzX6Zn6JLJWzwqJMzXL69Qpqx5RYe1sSBc", 
    secret_key="DyrsLjt6VpRugvr2jSnihr8ZT65FbXVzbe8kwoZQPrAt",
    contracts_timeout=10000,
)
'''
data = api.Contracts.Stocks["0050"]
ticks = api.ticks(data, "2024-09-18")
ticks
tick_data_df = pd.DataFrame({**ticks})
tick_data_df.ts = pd.to_datetime(tick_data_df.ts)
tick_data_df.head() #回傳最前面的資料，沒有指定資料筆數，預設為5筆
print(tick_data_df)'''

'''
kbars = api.kbars(
    contract=api.Contracts.Stocks["0050"], 
    start="2024-09-18", 
    end="2024-09-18", 
)
kbars
kbars_data_df = pd.DataFrame({**kbars})
kbars_data_df.ts = pd.to_datetime(kbars_data_df.ts)
kbars_data_df.head()
print(kbars_data_df)'''

#kbars_data_df.to_pickle('20240918_0050.pickle')

def generate_stock_pickle(stock_code, date, output_dir='/data'):
    # 下載股票數據
    contract = api.Contracts.Stocks[stock_code]
    # 設置日期範圍
    start_date = datetime.strptime(date, "%Y-%m-%d")
    end_date = start_date + timedelta(days=1)

    kbars = api.kbars(contract, start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
      # 將數據轉換為 DataFrame
    df = pd.DataFrame({
        'ts': pd.to_datetime(kbars.ts),
        'Open': kbars.Open,
        'High': kbars.High,
        'Low': kbars.Low,
        'Close': kbars.Close,
        'Volume': kbars.Volume
    })

    # 將數據存為 pickle 文件
    pickle_file = os.path.join(output_dir, f"{stock_code}_{date}.pkl")
    # 檢查 /data 資料夾是否存在，不存在則創建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    df.to_pickle(pickle_file)

    print(f"股票數據已保存到 {pickle_file}")

# 解析命令行參數
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="下載股票數據並保存為 pickle 文件")
    parser.add_argument('--stock', type=str, required=True, help="股票代號")
    parser.add_argument('--date', type=str, required=True, help="日期 (YYYY-MM-DD)")

    args = parser.parse_args()

    # 登入 Shioaji
    login()

    # 下載股票數據並生成 pickle
    generate_stock_pickle(args.stock, args.date)