import streamlit as st
import pandas as pd
import config
import bybit
from pybit import usdt_perpetual
TX = 0.3

st.markdown('''# **AlgoFinance Dashboard**
''')
st.header('**Summary**')

############################################################################################# IP
import socket
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print('My local IP is: ' + local_ip)
from requests import get
ip = get('https://api.ipify.org').text
print(f'My public IP is: {ip}')
st.write(str(local_ip))
st.write(str(ip))


###################################################################################################### API 00Marc
################################## API

apiKey00 = config.apiKey1000
apiSecret00 = config.apiSecret1000
client = bybit.bybit(test=False, api_key=apiKey00, api_secret=apiSecret00)
#PERP
session_auth = usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com",
    api_key=apiKey00,
    api_secret=apiSecret00
)
print('loggedin')
authUSDT = session_auth.get_wallet_balance()

################################################LIMIT

RATELIMIT_USDT = authUSDT['rate_limit']
STATELIMIT_USDT = authUSDT['rate_limit_status']
RESETLIMIT_USDT = authUSDT['rate_limit_reset_ms']

################################################### Refresh

# from streamlit_autorefresh import st_autorefresh
#
# count = st_autorefresh(interval=30000, limit=100, key="FizzBuzz")
#
# if count == 0:
#     st.write("Count is zero" + ' and ' + str(STATELIMIT_USDT) + '/' + str(RATELIMIT_USDT))
# elif count % 3 == 0 and count % 5 == 0:
#     st.write(f"Count: {count}/100")
# elif count % 3 == 0:
#     st.write(f"Count: {count}/100" + ' and ' + str(STATELIMIT_USDT) + '/' + str(RATELIMIT_USDT))
# elif count % 5 == 0:
#     st.write(f"Count: {count}/100" + ' and ' + str(STATELIMIT_USDT) + '/' + str(RATELIMIT_USDT))
# else:
#     st.write(f"Count: {count}/100" + ' and ' + str(STATELIMIT_USDT) + '/' + str(RATELIMIT_USDT))

st.write(str(STATELIMIT_USDT) + '/' + str(RATELIMIT_USDT))
##################################

EQUITY_USDT = authUSDT['result']['USDT']['equity']
NRZ_USDT = authUSDT['result']['USDT']['unrealised_pnl']
PERF_USDT = authUSDT['result']['USDT']['cum_realised_pnl']

############################################################################################# END

def round_value(input_value):
    if input_value.values > 1:
        a = float(round(input_value, 2))
    else:
        a = float(round(input_value, 8))
    return a

crpytoList = {
    'Price 1': 'BTCUSDT',
    'Price 2': 'ETHUSDT',
    'Price 3': 'BNBUSDT',
    'Price 4': 'XMRUSDT',
    'Price 5': 'ADAUSDT',
    'Price 6': 'DOGEUSDT'
}

col1, col2 , col3, col4, col5 = st.columns(5)

Math = EQUITY_USDT - NRZ_USDT - PERF_USDT
PNL100 = (round(EQUITY_USDT/round(Math),4)-1)*100

TAXABLE = NRZ_USDT + PERF_USDT
print('TO TAX: ' + str(TAXABLE))

COMMISSION = TAXABLE * TX
if TAXABLE > 0:
    print('COMMISSION: ' + str(COMMISSION))
if TAXABLE < 0:
    print('COMMISSION: 0')

for i in range(len(crpytoList.keys())):
    if i == 0:
        with col1:
            st.info('👨🏽‍🎓'' 00Marc')
    if i == 1:
        with col2:
            st.info("💰"' : ' + str(round(EQUITY_USDT,2)))
    if i == 2:
        with col3:
            st.info("⬇️"' : ' + str(round(Math)))
    if i == 3:
        with col4:
            st.info("💸"' : ' + str(round(TAXABLE,2)))
    if i == 4:
        with col5:
            st.info('〽️'' : ' + str(round(PNL100,2)) +'%')

###################################################################################################### API 00Marc
