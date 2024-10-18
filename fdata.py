import shioaji as sj
import pandas as pd
import os
import pickle

api = sj.Shioaji()
api.login(
    api_key="E9oPqAhnU6WzX6Zn6JLJWzwqJMzXL69Qpqx5RYe1sSBc", 
    secret_key="DyrsLjt6VpRugvr2jSnihr8ZT65FbXVzbe8kwoZQPrAt",
    contracts_timeout=10000,
)

data = api.Contracts.Stocks["0050"]

ticks = api.ticks(data, "2024-09-18")
ticks

tick_data_df = pd.DataFrame({**ticks})
tick_data_df.ts = pd.to_datetime(tick_data_df.ts)
tick_data_df.head() #回傳最前面的資料，沒有指定資料筆數，預設為5筆
print(tick_data_df)

kbars = api.kbars(
    contract=api.Contracts.Stocks["0050"], 
    start="2024-09-18", 
    end="2024-09-18", 
)
kbars
kbars_data_df = pd.DataFrame({**kbars})
kbars_data_df.ts = pd.to_datetime(kbars_data_df.ts)
kbars_data_df.head()
print(kbars_data_df)

kbars_data_df.to_pickle('20240918_0050.pickle')

if __name__ == "__main__":
    # 可以根據需求修改個股代碼
    ticker = "AAPL"
    output_dir = "/data"