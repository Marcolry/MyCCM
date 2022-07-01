import bybit
from pybit import usdt_perpetual
import time
import config
import streamlit as st
import pandas as pd

############################################################################################# IP
import socket
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print('My local IP is: ' + local_ip)
from requests import get
ip = get('https://api.ipify.org').text
print(f'My public IP is: {ip}')

############################################################################################# CONNEXION
# Acc => FELI
TX = 0.3

#API IP Long
# apiKey00 = "gIvcjYR73pqtOhythq"
# apiSecret00 = "Dfnf104KvRfDA5olkQh89TjK2z9Vab6hE1Fw"

#3MOIS 1000
apiKey00 = config.apiKey1000
apiSecret00 = config.apiSecret1000
#100
# apiKey00 = "c5AGNYqyNoa5pFkrpk"
# apiSecret00 = "DHhHYRyF02jzkFA02wq1f2Laj6ZV8cq5U2Oh"

#SPOT
client = bybit.bybit(test=False, api_key=apiKey00, api_secret=apiSecret00)
#PERP
session_auth = usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com",
    api_key=apiKey00,
    api_secret=apiSecret00
)
print('loggedin')

############################################################################################# SPOT INFO



info = client.Market.Market_symbolInfo().result()
#print(info)

symbolBTCUSD = info[0]['result'][0]['symbol']
lastPrice = info[0]['result'][0]['last_price']
### To know what is the listing of the JSON
#for i in keys:
#    print(i)
###
#print(symbolBTCUSD + ": " + lastPrice)

balance = client.Wallet.Wallet_getBalance(coin="BTC").result()
#result = balance[0]['result']['BTC']['available_balance']
#print(result)

############################################################################################# USDT PERP EQUITY

authUSDT = session_auth.get_wallet_balance()

EQUITY_USDT = authUSDT['result']['USDT']['equity']
NRZ_USDT = authUSDT['result']['USDT']['unrealised_pnl']
PERF_USDT = authUSDT['result']['USDT']['cum_realised_pnl']

#for i in equityUSDT:
#    print(i)
print('EQUITY: ' + str(EQUITY_USDT))
print('NOT REALIZED: ' + str(NRZ_USDT))
print('PERFORMANCE: ' + str(PERF_USDT))

Math = EQUITY_USDT - NRZ_USDT - PERF_USDT
print('DEPOSIT: ' + str(round(Math)))

TAXABLE = NRZ_USDT + PERF_USDT
print('TAXABLE: ' + str(TAXABLE))

COMMISSION = TAXABLE * TX
if TAXABLE > 0:
    print('COMMISSION: ' + str(COMMISSION))
if TAXABLE < 0:
    print('COMMISSION: 0')
#print(balanceUSDT)
#print(session_auth.wallet_fund_records())

# equity
# available_balance
# used_margin
# order_margin
# position_margin
# occ_closing_fee
# occ_funding_fee
# wallet_balance
# realised_pnl
# unrealised_pnl
# cum_realised_pnl
# given_cash
# service_cash

############################################################################################# Withdrawals

# print(session_auth.my_position(symbol="MANAUSDT"))
# print(session_auth.my_position(symbol="SOLUSDT"))
# print(session_auth.my_position(symbol="DOGEUSDT"))
# print(session_auth.my_position(symbol="SFPUSDT"))
# print(session_auth.my_position(symbol="LTCUSDT"))


















