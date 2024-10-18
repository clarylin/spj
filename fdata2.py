import time as time_module
import shioaji as sj
import pandas as pd
from shioaji import TickFOPv1, BidAskFOPv1, Exchange
from shioaji.constant import Action, StockPriceType, OrderType
from datetime import datetime, time

api = sj.Shioaji()
api = sj.Shioaji(simulation=True)
api.login(
    api_key="E9oPqAhnU6WzX6Zn6JLJWzwqJMzXL69Qpqx5RYe1sSBc", 
    secret_key="DyrsLjt6VpRugvr2jSnihr8ZT65FbXVzbe8kwoZQPrAt",
)
api.activate_ca(
    ca_path="c:/ekey/551/E225206498/S/Sinopac.pfx",
    ca_passwd="E225206498",
    person_id="E225206498",
)
accounts = api.list_accounts()
print(accounts)


# 取加權指收盤及台指期當下價格
'''contracts = [api.Contracts.Indexs.TSE['001'], api.Contracts.Futures.TXF['TXFR1']]
snapshots = api.snapshots(contracts)
snapshots

df = pd.DataFrame(s.__dict__ for s in snapshots)
df.ts = pd.to_datetime(df.ts)
df
print(df)'''

# 台指期13.35時價格
'''ticks = api.ticks(
    contract=api.Contracts.Futures.TXF['TXFR1'], 
    date="2024-10-18",
    query_type=sj.constant.TicksQueryType.RangeTime,
    time_start="13:35:00",
    time_end="13:35:59",
)
ticks
df = pd.DataFrame({**ticks})
df.ts = pd.to_datetime(df.ts)
df.head()
print(df)'''


# 取得台指期貨當下價格 
def get_futures_price():
    contracts = api.Contracts.Futures
    future_contract = contracts.TXF.TXFR1  
    snapshot = api.snapshots([future_contract])
    futures_price = snapshot[0].close  # 應使用 13:35 的價格 
    return futures_price

# 取得台灣加權指數收盤價
def get_taiwan_weighted_index():
    contracts = api.Contracts.Indexs.TSE.TSE001  # 加權指數合約
    snapshot = api.snapshots([contracts])
    weighted_index = snapshot[0].close  # 使用收盤價
    return weighted_index

# 調整台指期貨倉位
def adjust_position():
    futures_price = get_futures_price()
    tw_index = get_taiwan_weighted_index()
    
    print(f"加權指數收盤價: {tw_index}")
    print(f"台指期貨價格: {futures_price}")
    
    if futures_price > tw_index:
        print(f"{datetime.now()}: 台指期貨 {futures_price} > 加權指數 {tw_index}，調整成空單")
        #進行空單操作
        place_order('short')
    elif futures_price < tw_index:
        print(f"{datetime.now()}: 台指期貨 {futures_price} < 加權指數 {tw_index}，調整成多單")
        # 進行多單操作
        place_order('long')
    else:
        print(f"{datetime.now()}: 台指期貨 {futures_price} = 加權指數 {tw_index}，無需調整")


# 下單函數 
def place_order(position_type):
   
    contracts = api.Contracts.Futures.TXF.TXFR1  
    if position_type == 'long':
        order = api.Order(
            action=sj.constant.Action.Buy,
            price=0,  # 使用市價單下單
            quantity=1,
            price_type=sj.constant.FuturesPriceType.LMT, # 市價單
            order_type=sj.constant.OrderType.ROD, 
            octype=sj.constant.FuturesOCType.Auto,
            account=api.futopt_account
        )
    elif position_type == 'short':
        order = api.Order(
            action=sj.constant.Action.Sell,
            price=0,  # 使用市價單下單
            quantity=1,
            price_type=sj.constant.FuturesPriceType.LMT, # 市價單
            order_type=sj.constant.OrderType.ROD, 
            octype=sj.constant.FuturesOCType.Auto,
            account=api.futopt_account
        )
    else:
        raise ValueError("position_type 必須是 'long' 或 'short'")  # 若無效參數拋出錯誤

    
    trade = api.place_order(contracts, order)
    print(f"下單成功: {trade}")






'''# 設定每天在 13:40 調整台指期貨
schedule.every().monday.to.friday.at("13:40").do(adjust_position)

# 登入 API 並開始任務
if __name__ == "__main__":
    login()
    
    while True:
        schedule.run_pending()
        time_module.sleep(1)'''
