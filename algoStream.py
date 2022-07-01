import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
import config
import bybit
from pybit import usdt_perpetual
TX = 0.3

st.markdown('''# **AlgoFinance AUM**
''')
#st.header('**Summary**')

################################## API

#client = bybit.bybit(test=False, api_key=apiKey00, api_secret=apiSecret00)
#print('loggedin')
#PERP
session_auth_00 = usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com",
    api_key=config.apiKey1000,
    api_secret=config.apiSecret1000
)
authUSDT_00 = session_auth_00.get_wallet_balance()

session_auth_01 = usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com",
    api_key=config.apiKey100,
    api_secret=config.apiSecret100
)
authUSDT_01 = session_auth_01.get_wallet_balance()

################################################LIMIT

RATELIMIT_00 = authUSDT_00['rate_limit']
STATELIMIT_00 = authUSDT_00['rate_limit_status']
RESETLIMIT_00 = authUSDT_00['rate_limit_reset_ms']

RATELIMIT_01 = authUSDT_01['rate_limit']
STATELIMIT_01 = authUSDT_01['rate_limit_status']
RESETLIMIT_01 = authUSDT_01['rate_limit_reset_ms']

############################################################################################# IP
import socket
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print('My local IP is: ' + local_ip)
from requests import get
ip = get('https://api.ipify.org').text
print(f'My public IP is: {ip}')
st.write('**Local IP:** ' + str(local_ip) + ' // **Public IP:** ' + str(ip))
st.write('**Request Limit:** ' + str(STATELIMIT_00) + '/' + str(RATELIMIT_00))
#st.write('**Request Limit:** ' + str(STATELIMIT_01) + '/' + str(RATELIMIT_01))

###################################################################################################### API 00Marc

##################################

EQUITY_00 = authUSDT_00['result']['USDT']['equity']
NRZ_00 = authUSDT_00['result']['USDT']['unrealised_pnl']
PERF_00 = authUSDT_00['result']['USDT']['cum_realised_pnl']

EQUITY_01 = authUSDT_01['result']['USDT']['equity']
NRZ_01 = authUSDT_01['result']['USDT']['unrealised_pnl']
PERF_01 = authUSDT_01['result']['USDT']['cum_realised_pnl']

############################################################################################# END


###############

col1_00, col2_00 , col3_00, col4_00, col5_00, col6_00 = st.columns(6)

Math_00 = EQUITY_00 - NRZ_00 - PERF_00
PNL100_00 = (round(EQUITY_00/round(Math_00),4)-1)*100

TAXABLE_00 = NRZ_00 + PERF_00
print('TO TAX: ' + str(TAXABLE_00))

if TAXABLE_00 > 0:
    COMMISSION_00 = TAXABLE_00 * TX
if TAXABLE_00 < 0:
    COMMISSION_00 = 0

for i in range(6):
    if i == 0:
        with col1_00:
            st.info('💁🏾‍♀️'' 00Feli')
    if i == 1:
        with col2_00:
            st.info("💰"' : ' + str(round(EQUITY_00,2)))
    if i == 2:
        with col3_00:
            st.info("⬇️"' : ' + str(round(Math_00)))
    if i == 3:
        with col4_00:
            st.info("💸"' : ' + str(round(TAXABLE_00,2)) + ' (' + str(round(PERF_00,2)) + ' + ' + str(round(NRZ_00,2)) + ')')
    if i == 4:
        with col5_00:
            st.info('〽️'' : ' + str(round(PNL100_00,3)) +'%')
    if i == 5:
        with col6_00:
            st.info('✂️'' : ' + str(round(COMMISSION_00,2)))

#################

###############

col1_01, col2_01 , col3_01, col4_01, col5_01, col6_01 = st.columns(6)

Math_01 = EQUITY_01 - NRZ_01 - PERF_01
PNL100_01 = (round(EQUITY_01/round(Math_01),4)-1)*100

TAXABLE_01 = NRZ_01 + PERF_01
print('TO TAX: ' + str(TAXABLE_01))

if TAXABLE_01 > 0:
    COMMISSION_01 = TAXABLE_01 * TX
if TAXABLE_01 < 0:
    COMMISSION_01 = 0

for i in range(6):
    if i == 0:
        with col1_01:
            st.info('👨🏽‍🎓'' 01Algo')
    if i == 1:
        with col2_01:
            st.info("💰"' : ' + str(round(EQUITY_01,2)))
    if i == 2:
        with col3_01:
            st.info("⬇️"' : ' + str(round(Math_01)))
    if i == 3:
        with col4_01:
            st.info("💸"' : ' + str(round(TAXABLE_01,2)) + ' (' + str(round(PERF_01,2)) + ' + ' + str(round(NRZ_01,2)) + ')')
    if i == 4:
        with col5_01:
            st.info('〽️'' : ' + str(round(PNL100_01,3)) +'%')
    if i == 5:
        with col6_01:
            st.info('✂️'' : ' + str(round(COMMISSION_01,2)))

#################