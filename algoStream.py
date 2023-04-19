import streamlit as st
import time
st.set_page_config(layout="wide", initial_sidebar_state="collapsed", page_icon="👀")
import pandas as pd
import bybit
from pybit import usdt_perpetual
import array as arr
import numpy as np

###################################################################################################################################################################### IP
import socket
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print('My local IP is: ' + local_ip)
from requests import get
ip = get('https://api.ipify.org').text
print(f'My public IP is: {ip}')
st.write('**Local IP:** ' + str(local_ip) + ' // **Public IP:** ' + str(ip))


#Config Final Array:
# Nom, aK, aS, Tx, RetroC, HWM

st.markdown('''# **AlgoFinance AUM**
''')

###################################################################################################################################################################### API

TXCOM_00TFio = 1
RETRO_00TFio = 0
HWM_00TFio = 0
TXCOM_00Xm33 = 1
RETRO_00Xm33 = 0
HWM_00Xm33 = 0
TXCOM_00Liqi = 1
RETRO_00Liqi = 0
HWM_00Liqi = 0
TXCOM_01Vitor = 1
RETRO_01Vitor = 0
HWM_01Vitor = 0
TXCOM_02Joao = 1
RETRO_02Joao = 0
HWM_02Joao = 0


c00TFio = np.array(['00TFio', st.secrets["aK00TFio"], st.secrets["aS00TFio"], 0.3, 1/3, 0])
c00Xm33 = np.array(['00Xm33', st.secrets["aK00Xm33"], st.secrets["aS00Xm33"], 0.3, 0, 0])
c00Liqi = np.array(['00Liqi', st.secrets["aK00Liqi"], st.secrets["aS00Liqi"], 0.3, 0, 0])
c01Vitor = np.array(['01Vitor', st.secrets["aK01Vitor"], st.secrets["aS01Vitor"], 0.3, 0, 0])
c02Joao = np.array(['02Joao', st.secrets["aK02Joao"], st.secrets["aS02Joao"], 0.3, 0, 0])

allUsers = np.array([c00TFio, c00Xm33, c00Liqi, c01Vitor, c02Joao])


session_auth_00TFio = usdt_perpetual.HTTP(endpoint="https://api.bybit.com",api_key=st.secrets["aK00TFio"],api_secret=st.secrets["aS00TFio"])
session_auth_00Xm33 = usdt_perpetual.HTTP(endpoint="https://api.bybit.com",api_key=st.secrets["aK00Xm33"],api_secret=st.secrets["aS00Xm33"])
session_auth_00Liqi = usdt_perpetual.HTTP(endpoint="https://api.bybit.com",api_key=st.secrets["aK00Liqi"],api_secret=st.secrets["aS00Liqi"])
session_auth_01Vitor = usdt_perpetual.HTTP(endpoint="https://api.bybit.com",api_key=st.secrets["aK01Vitor"],api_secret=st.secrets["aS01Vitor"])
session_auth_02Joao = usdt_perpetual.HTTP(endpoint="https://api.bybit.com",api_key=st.secrets["aK02Joao"],api_secret=st.secrets["aS02Joao"])

authUSDT_00TFio = session_auth_00TFio.get_wallet_balance()
authUSDT_00Xm33 = session_auth_00Xm33.get_wallet_balance()
authUSDT_00Liqi = session_auth_00Liqi.get_wallet_balance()
authUSDT_01Vitor = session_auth_01Vitor.get_wallet_balance()
authUSDT_02Joao = session_auth_02Joao.get_wallet_balance()

posUSDT_00TFio = session_auth_00TFio.my_position()
posUSDT_00Xm33 = session_auth_00Xm33.my_position()
posUSDT_00Liqi = session_auth_00Liqi.my_position()
posUSDT_01Vitor = session_auth_01Vitor.my_position()
posUSDT_02Joao = session_auth_02Joao.my_position()


# # def fAuth(a):
# #   for x in a:
# #     print(x)
#
# print(allUsers[0][2])
#
# def fAuth(x):
#     for i in range(0,len(allUsers)):
#         session_auth = usdt_perpetual.HTTP(endpoint="https://api.bybit.com",api_key=allUsers[i][1],api_secret=allUsers[i][2])
#         print(x)
#         print(session_auth.get_wallet_balance())
#         #return session_auth
#
#         #print(session_auth.get_wallet_balance())
#
# fAuth(allUsers)
#
# #print(session_auth)
# st.stop()
#
#
# #print(c00TFio[0])
# #print(c00TFio[1])
# #print(allUsers[0][0])
# #print(len(allUsers))
# #for i in range(0,len(allUsers)):
#
#
# #print(allUsers[0][1])
# #print(allUsers[0][2])
# #print(allUsers[1][1])
# #print(allUsers[1][2])
# #print(len(allUsers))
#
# print(allUsers[0][3])
# print(allUsers[0][4])
# print(allUsers[0][5])
# print("Stop")
#
#








##-----------------------------------------------------------------------> 00 - Feli



RATELIMIT_00 = authUSDT_00TFio['rate_limit']
STATELIMIT_00 = authUSDT_00TFio['rate_limit_status']
RESETLIMIT_00 = authUSDT_00TFio['rate_limit_reset_ms']
print(str(STATELIMIT_00) + '------------------------------------------------------------------------------->')
##-----------------------------------------------------------------------> 00 - Marc
RATELIMIT_01 = authUSDT_00Xm33['rate_limit']
STATELIMIT_01 = authUSDT_00Xm33['rate_limit_status']
RESETLIMIT_01 = authUSDT_00Xm33['rate_limit_reset_ms']
print(str(STATELIMIT_01) + '------------------------------------------------------------------------------->')


###################################################################################################################################################################### API


#print(len(posUSDT_00TFio['result']))
#print(len(posUSDT_00Xm33['result']))

##-----------------------------------------------------------------------> API LIMIT

st.write('**Request Limit:** ' + str(STATELIMIT_00) + '/' + str(RATELIMIT_00) + ' & ' + str(STATELIMIT_01) + '/' + str(RATELIMIT_01))


###################################################################################################################################################################### CONFIG Feli

###################################################################################################################################################################### DASHBOARD


ALL_00TFio = list(range(0, len(posUSDT_00TFio['result']))) #print(ALL)
a_00TFio = arr.array('i', ALL_00TFio)

######################################################################################### DATA

EQUITY_00TFio = authUSDT_00TFio['result']['USDT']['equity']
NRZ_00TFio = authUSDT_00TFio['result']['USDT']['unrealised_pnl']
PERF_00TFio = authUSDT_00TFio['result']['USDT']['cum_realised_pnl']
AVAILABLE_00TFio = authUSDT_00TFio['result']['USDT']['available_balance']
INPLAY_00TFio = (EQUITY_00TFio - AVAILABLE_00TFio)/EQUITY_00TFio


DEPOSIT_00TFio = EQUITY_00TFio - NRZ_00TFio - PERF_00TFio
PNL100_00TFio = (round(EQUITY_00TFio/DEPOSIT_00TFio,4)-1)*100

TAXABLE_00TFio = NRZ_00TFio + PERF_00TFio

if TAXABLE_00TFio > 0:
    COMMISSION_00TFio = TAXABLE_00TFio * TXCOM_00TFio
if TAXABLE_00TFio <= 0:
    COMMISSION_00TFio = 0


######################################################################################### NB

nbTrade_00TFio = 0
nbLong_00TFio = 0
nbShort_00TFio = 0

for x in a_00TFio:
   oneTrade = posUSDT_00TFio['result'][x]['data']["entry_price"] != 0
   if oneTrade:
       nbTrade_00TFio += 1

for x in a_00TFio:
   oneLong = posUSDT_00TFio['result'][x]['data']["side"] == "Buy" and posUSDT_00TFio['result'][x]['data']["entry_price"] != 0
   if oneLong:
       nbLong_00TFio += 1

for x in a_00TFio:
   oneShort = posUSDT_00TFio['result'][x]['data']["side"] == "Sell" and posUSDT_00TFio['result'][x]['data']["entry_price"] != 0
   if oneShort:
       nbShort_00TFio += 1


###################################################################################################################################################################### CONFIG Marc

###################################################################################################################################################################### DASHBOARD


ALL_00Xm33 = list(range(0, len(posUSDT_00Xm33['result']))) #print(ALL)
a_00Xm33 = arr.array('i', ALL_00Xm33)

######################################################################################### DATA

EQUITY_00Xm33 = authUSDT_00Xm33['result']['USDT']['equity']
NRZ_00Xm33 = authUSDT_00Xm33['result']['USDT']['unrealised_pnl']
PERF_00Xm33 = authUSDT_00Xm33['result']['USDT']['cum_realised_pnl']

AVAILABLE_00Xm33 = authUSDT_00Xm33['result']['USDT']['available_balance']
INPLAY_00Xm33 = (EQUITY_00Xm33 - AVAILABLE_00Xm33)/EQUITY_00Xm33


DEPOSIT_00Xm33 = EQUITY_00Xm33 - NRZ_00Xm33 - PERF_00Xm33
PNL100_00Xm33 = (round(EQUITY_00Xm33/DEPOSIT_00Xm33,4)-1)*100

TAXABLE_00Xm33 = NRZ_00Xm33 + PERF_00Xm33

if TAXABLE_00Xm33 > 0:
    COMMISSION_00Xm33 = TAXABLE_00Xm33 * TXCOM_00Xm33
if TAXABLE_00Xm33 <= 0:
    COMMISSION_00Xm33 = TAXABLE_00Xm33 * TXCOM_00Xm33


######################################################################################### NB

nbTrade_00Xm33 = 0
nbLong_00Xm33 = 0
nbShort_00Xm33 = 0

for x in a_00Xm33:
   oneTrade = posUSDT_00Xm33['result'][x]['data']["entry_price"] != 0
   if oneTrade:
       nbTrade_00Xm33 += 1

for x in a_00Xm33:
   oneLong = posUSDT_00Xm33['result'][x]['data']["side"] == "Buy" and posUSDT_00Xm33['result'][x]['data']["entry_price"] != 0
   if oneLong:
       nbLong_00Xm33 += 1

for x in a_00Xm33:
   oneShort = posUSDT_00Xm33['result'][x]['data']["side"] == "Sell" and posUSDT_00Xm33['result'][x]['data']["entry_price"] != 0
   if oneShort:
       nbShort_00Xm33 += 1


###################################################################################################################################################################### DASHBOARD

###################################################################################################################################################################### CONFIG Feli


ALL_00Liqi = list(range(0, len(posUSDT_00Liqi['result']))) #print(ALL)
a_00Liqi = arr.array('i', ALL_00Liqi)

######################################################################################### DATA

EQUITY_00Liqi = authUSDT_00Liqi['result']['USDT']['equity']
NRZ_00Liqi = authUSDT_00Liqi['result']['USDT']['unrealised_pnl']
PERF_00Liqi = authUSDT_00Liqi['result']['USDT']['cum_realised_pnl']
AVAILABLE_00Liqi = authUSDT_00Liqi['result']['USDT']['available_balance']
INPLAY_00Liqi = (EQUITY_00Liqi - AVAILABLE_00Liqi)/EQUITY_00Liqi


DEPOSIT_00Liqi = EQUITY_00Liqi - NRZ_00Liqi - PERF_00Liqi
PNL100_00Liqi = (round(EQUITY_00Liqi/DEPOSIT_00Liqi,4)-1)*100

TAXABLE_00Liqi = NRZ_00Liqi + PERF_00Liqi

if TAXABLE_00Liqi > 0:
    COMMISSION_00Liqi = TAXABLE_00Liqi * TXCOM_00Liqi
if TAXABLE_00Liqi <= 0:
    COMMISSION_00Liqi = 0


######################################################################################### NB

nbTrade_00Liqi = 0
nbLong_00Liqi = 0
nbShort_00Liqi = 0

for x in a_00Liqi:
   oneTrade = posUSDT_00Liqi['result'][x]['data']["entry_price"] != 0
   if oneTrade:
       nbTrade_00Liqi += 1

for x in a_00Liqi:
   oneLong = posUSDT_00Liqi['result'][x]['data']["side"] == "Buy" and posUSDT_00Liqi['result'][x]['data']["entry_price"] != 0
   if oneLong:
       nbLong_00Liqi += 1

for x in a_00Liqi:
   oneShort = posUSDT_00Liqi['result'][x]['data']["side"] == "Sell" and posUSDT_00Liqi['result'][x]['data']["entry_price"] != 0
   if oneShort:
       nbShort_00Liqi += 1


###################################################################################################################################################################### CONFIG Marc

###################################################################################################################################################################### CONFIG Feli


ALL_01Vitor = list(range(0, len(posUSDT_01Vitor['result']))) #print(ALL)
a_01Vitor = arr.array('i', ALL_01Vitor)

######################################################################################### DATA

EQUITY_01Vitor = authUSDT_01Vitor['result']['USDT']['equity']
NRZ_01Vitor = authUSDT_01Vitor['result']['USDT']['unrealised_pnl']
PERF_01Vitor = authUSDT_01Vitor['result']['USDT']['cum_realised_pnl']
AVAILABLE_01Vitor = authUSDT_01Vitor['result']['USDT']['available_balance']
INPLAY_01Vitor = (EQUITY_01Vitor - AVAILABLE_01Vitor)/EQUITY_01Vitor


DEPOSIT_01Vitor = EQUITY_01Vitor - NRZ_01Vitor - PERF_01Vitor
PNL100_01Vitor = (round(EQUITY_01Vitor/DEPOSIT_01Vitor,4)-1)*100

TAXABLE_01Vitor = NRZ_01Vitor + PERF_01Vitor

if TAXABLE_01Vitor > 0:
    COMMISSION_01Vitor = TAXABLE_01Vitor * TXCOM_01Vitor
if TAXABLE_01Vitor <= 0:
    COMMISSION_01Vitor = 0


######################################################################################### NB

nbTrade_01Vitor = 0
nbLong_01Vitor = 0
nbShort_01Vitor = 0

for x in a_01Vitor:
   oneTrade = posUSDT_01Vitor['result'][x]['data']["entry_price"] != 0
   if oneTrade:
       nbTrade_01Vitor += 1

for x in a_01Vitor:
   oneLong = posUSDT_01Vitor['result'][x]['data']["side"] == "Buy" and posUSDT_01Vitor['result'][x]['data']["entry_price"] != 0
   if oneLong:
       nbLong_01Vitor += 1

for x in a_01Vitor:
   oneShort = posUSDT_01Vitor['result'][x]['data']["side"] == "Sell" and posUSDT_01Vitor['result'][x]['data']["entry_price"] != 0
   if oneShort:
       nbShort_01Vitor += 1


###################################################################################################################################################################### CONFIG Marc

###################################################################################################################################################################### CONFIG Feli


ALL_02Joao = list(range(0, len(posUSDT_02Joao['result']))) #print(ALL)
a_02Joao = arr.array('i', ALL_02Joao)

######################################################################################### DATA

EQUITY_02Joao = authUSDT_02Joao['result']['USDT']['equity']
NRZ_02Joao = authUSDT_02Joao['result']['USDT']['unrealised_pnl']
PERF_02Joao = authUSDT_02Joao['result']['USDT']['cum_realised_pnl']
AVAILABLE_02Joao = authUSDT_02Joao['result']['USDT']['available_balance']
INPLAY_02Joao = (EQUITY_02Joao - AVAILABLE_02Joao)/EQUITY_02Joao


DEPOSIT_02Joao = EQUITY_02Joao - NRZ_02Joao - PERF_02Joao
PNL100_02Joao = (round(EQUITY_02Joao/DEPOSIT_02Joao,4)-1)*100

TAXABLE_02Joao = NRZ_02Joao + PERF_02Joao

if TAXABLE_02Joao > 0:
    COMMISSION_02Joao = TAXABLE_02Joao * TXCOM_02Joao
if TAXABLE_02Joao <= 0:
    COMMISSION_02Joao = 0


######################################################################################### NB

nbTrade_02Joao = 0
nbLong_02Joao = 0
nbShort_02Joao = 0

for x in a_02Joao:
   oneTrade = posUSDT_02Joao['result'][x]['data']["entry_price"] != 0
   if oneTrade:
       nbTrade_02Joao += 1

for x in a_02Joao:
   oneLong = posUSDT_02Joao['result'][x]['data']["side"] == "Buy" and posUSDT_02Joao['result'][x]['data']["entry_price"] != 0
   if oneLong:
       nbLong_02Joao += 1

for x in a_02Joao:
   oneShort = posUSDT_02Joao['result'][x]['data']["side"] == "Sell" and posUSDT_02Joao['result'][x]['data']["entry_price"] != 0
   if oneShort:
       nbShort_02Joao += 1


###################################################################################################################################################################### CONFIG Marc

###################################################################################################################################################################### CONFIG Marc






############################################################################################################ PRICE

client = bybit.bybit(test=False, api_key=st.secrets["aK00TFio"], api_secret=st.secrets["aS00TFio"])
info = client.Market.Market_symbolInfo().result()
keys = info[0]['result']
btc = keys[46]['last_price']
name = keys[46]['symbol']

############################################################################################################




########################### First Line

col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13 = st.columns(13)

for i in range(13):
    if i == 0:
        with col1:
            st.info("₿: "+ btc)
            st.info('💁🏾‍♀️'' 00TFio')
            st.info('💁🏾‍♀️'' 00Xm33')
            st.info('💁🏾‍♀️'' 00Liqi')
            st.info("💰"' : ' + str(round((EQUITY_00TFio + EQUITY_00Xm33 + EQUITY_00Liqi)/float(btc), 4)) + ' BTC')
    if i == 1:
        with col2:
            st.info("💰 Equity 💰")
            st.info("💰"' : ' + str(round(EQUITY_00TFio,2)))
            st.info("💰"' : ' + str(round(EQUITY_00Xm33,2)))
            st.info("💰"' : ' + str(round(EQUITY_00Liqi,2)))
            st.info("💰"' : ' + str(round(EQUITY_00TFio + EQUITY_00Xm33 + EQUITY_00Liqi, 2)))
    if i == 2:
        with col3:
            st.info("⬇️ Deposit ⬇️")
            st.info("⬇️"' : ' + str(round(DEPOSIT_00TFio,2)))
            st.info("⬇️"' : ' + str(round(DEPOSIT_00Xm33,2)))
            st.info("⬇️"' : ' + str(round(DEPOSIT_00Liqi,2)))
            st.info("⬇️"' : ' + str(round(DEPOSIT_00TFio + DEPOSIT_00Xm33 + DEPOSIT_00Liqi, 1)))
    if i == 3:
        with col4:
            st.info("💸 Bénéfice 💸")
            st.info("💸"' : ' + str(round(TAXABLE_00TFio,2)))
            st.info("💸"' : ' + str(round(TAXABLE_00Xm33,2)))
            st.info("💸"' : ' + str(round(TAXABLE_00Liqi,2)))
            st.info("💸"' : ' + str(round(TAXABLE_00TFio + TAXABLE_00Xm33 + TAXABLE_00Liqi, 2)))
    if i == 4:
        with col5:
            st.info("💸 Realized 💸")
            st.info("💸"' : ' + str(round(PERF_00TFio,2)))
            st.info("💸"' : ' + str(round(PERF_00Xm33,2)))
            st.info("💸"' : ' + str(round(PERF_00Liqi,2)))
            st.info("💸"' : ' + str(round(PERF_00TFio + PERF_00Xm33 + PERF_00Liqi, 2)))
    if i == 5:
        with col6:
            st.info("💸 Unrealized 💸")
            st.info("💸"' : ' + str(round(NRZ_00TFio,2)))
            st.info("💸"' : ' + str(round(NRZ_00Xm33,2)))
            st.info("💸"' : ' + str(round(NRZ_00Liqi,2)))
            st.info("💸"' : ' + str(round(NRZ_00TFio + NRZ_00Xm33 + NRZ_00Liqi, 2)))
    if i == 6:
        with col7:
            st.info("💀 In Play 💀")
            st.info("💀"' : ' + str(round(INPLAY_00TFio*100,2)) +'%')
            st.info("💀"' : ' + str(round(INPLAY_00Xm33*100,2)) +'%')
            st.info("💀"' : ' + str(round(INPLAY_00Liqi*100,2)) +'%')
            st.info("💀"' : ' + str(round((EQUITY_00TFio + EQUITY_00Xm33 + EQUITY_00Liqi - AVAILABLE_00TFio - AVAILABLE_00Xm33 - AVAILABLE_00Liqi) * 100 / (EQUITY_00TFio + EQUITY_00Xm33 + EQUITY_00Liqi), 2)) + '%')
    if i == 7:
        with col8:
            st.info("🫶 L/S 🫶")
            if nbTrade_00TFio == 0:
                st.info("🫶"' : No Trade')
            else:
                st.info("🫶"' : ' + str(nbLong_00TFio) + ' / ' + str(nbShort_00TFio) + ' (' + str(round((nbLong_00TFio/nbTrade_00TFio)*100)) + '/' + str(round((nbShort_00TFio/nbTrade_00TFio)*100)) + '%)')
            if nbTrade_00Xm33 == 0:
                st.info("🫶"' : No Trade')
            else:
                st.info("🫶"' : ' + str(nbLong_00Xm33) + ' / ' + str(nbShort_00Xm33) + ' (' + str(round((nbLong_00Xm33/nbTrade_00Xm33)*100)) + '/' + str(round((nbShort_00Xm33/nbTrade_00Xm33)*100)) + '%)')
            if nbTrade_00Liqi == 0:
                st.info("🫶"' : No Trade')
            else:
                st.info("🫶"' : ' + str(nbLong_00Liqi) + ' / ' + str(nbShort_00Liqi) + ' (' + str(round((nbLong_00Liqi/nbTrade_00Liqi)*100)) + '/' + str(round((nbShort_00Liqi/nbTrade_00Liqi)*100)) + '%)')
            st.info("🫶 Long/Short 🫶")
    if i == 8:
        with col9:
            st.info("#️⃣ Nb. T #️⃣")
            st.info("#️⃣"' : ' + str(nbTrade_00TFio))
            st.info("#️⃣"' : ' + str(nbTrade_00Xm33))
            st.info("#️⃣"' : ' + str(nbTrade_00Liqi))
            st.info("#️⃣"' : ' + str(nbTrade_00TFio + nbTrade_00Xm33 + nbTrade_00Liqi))
    if i == 9:
        with col10:
            st.info('〽️ Perf. 〽️')
            st.info('〽️'' : ' + str(round(PNL100_00TFio,3)) +'%')
            st.info('〽️'' : ' + str(round(PNL100_00Xm33,3)) +'%')
            st.info('〽️'' : ' + str(round(PNL100_00Liqi,3)) +'%')
            st.info('〽️'' : ' + str(round((PNL100_00TFio * DEPOSIT_00TFio + PNL100_00Xm33 * DEPOSIT_00Xm33 + PNL100_00Liqi + DEPOSIT_00Liqi) / (DEPOSIT_00TFio + DEPOSIT_00Xm33 + DEPOSIT_00Liqi), 2)) + '%')
    if i == 10:
        with col11:
            st.info('✂️ HWM ✂️')
            st.info('✂️'' : ' + str(round(HWM_00TFio)))
            st.info('✂️'' : ' + str(round(HWM_00Xm33)))
            st.info('✂️'' : ' + str(round(HWM_00Liqi)))
            st.info('✂️'' : ' + str(round(HWM_00TFio+HWM_00Xm33+HWM_00Liqi)))
    if i == 11:
        with col12:
            st.info('✂️ Com. ✂️')
            st.info('✂️'' : ' + str(round(COMMISSION_00TFio-HWM_00TFio,2)))
            st.info('✂️'' : ' + str(round(COMMISSION_00Xm33-HWM_00Xm33,2)))
            st.info('✂️'' : ' + str(round(COMMISSION_00Liqi-HWM_00Liqi,2)))
            st.info('✂️'' : ' + str(round(COMMISSION_00TFio + COMMISSION_00Xm33 + COMMISSION_00Liqi - HWM_00TFio - HWM_00Xm33 - HWM_00Liqi, 2)))
    if i == 12:
        with col13:
            st.info('✂️ Retro C. ✂️')
            if RETRO_00TFio == 0 or COMMISSION_00TFio-HWM_00TFio <= 0:
                st.info("🫶"' : N/A')
            else:
                st.info('✂️'' : ' + str(round((COMMISSION_00TFio-HWM_00TFio)*RETRO_00TFio,2)))
            if RETRO_00Xm33 == 0 or COMMISSION_00Xm33-HWM_00Xm33 <= 0:
                st.info("🫶"' : N/A')
            else:
                st.info('✂️'' : ' + str(round((COMMISSION_00Xm33-HWM_00Xm33)*RETRO_00Xm33,2)))
            if RETRO_00Liqi == 0 or COMMISSION_00Liqi-HWM_00Liqi <= 0:
                st.info("🫶"' : N/A')
            else:
                st.info('✂️'' : ' + str(round((COMMISSION_00Liqi-HWM_00Liqi)*RETRO_00Liqi,2)))
            st.info('✂️'' : ' + str(round((COMMISSION_00TFio - HWM_00TFio) * RETRO_00TFio + (COMMISSION_00Xm33 - HWM_00Xm33) * RETRO_00Xm33 + (COMMISSION_00Liqi - HWM_00Liqi) * RETRO_00Liqi, 2)))




###################################################################################################################################################################### 00 - Feli


###################################################################################################################################################################### 00 - Marc


###################################################################################################################################################################### 00 - Marc


col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13 = st.columns(13)

for i in range(13):
    if i == 0:
        with col1:
            st.info(' 📘 ')
    if i == 1:
        with col2:
            st.info("💰 Equity 💰")
    if i == 2:
        with col3:
            st.info("⬇️ Deposit ⬇️")
    if i == 3:
        with col4:
            st.info("💸 Bénéfice 💸")
    if i == 4:
        with col5:
            st.info("💸 Realized 💸")
    if i == 5:
        with col6:
            st.info("💸 Unrealized 💸")
    if i == 6:
        with col7:
            st.info("💀 In Play 💀")
    if i == 7:
        with col8:
            st.info("🫶 L/S 🫶")
    if i == 8:
        with col9:
            st.info("#️⃣ Nb. T #️⃣")
    if i == 9:
        with col10:
            st.info('〽️ Perf. 〽️')
    if i == 10:
        with col11:
            st.info('✂️ HWM ✂️')
    if i == 11:
        with col12:
            st.info('✂️ Com. ✂️')
    if i == 12:
        with col13:
            st.info('✂️ Retro C. ✂️')



####----------------------
####---------------------- 01Vitor
####----------------------


col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13 = st.columns(13)

for i in range(13):
    if i == 0:
        with col1:
            st.info('💁🏾‍♀️'' 01Vitor')
    if i == 1:
        with col2:
            st.info("💰"' : ' + str(round(EQUITY_01Vitor,2)))
    if i == 2:
        with col3:
            st.info("⬇️"' : ' + str(round(DEPOSIT_01Vitor,2)))
    if i == 3:
        with col4:
            st.info("💸"' : ' + str(round(TAXABLE_01Vitor,2)))
    if i == 4:
        with col5:
            st.info("💸"' : ' + str(round(PERF_01Vitor,2)))
    if i == 5:
        with col6:
            st.info("💸"' : ' + str(round(NRZ_01Vitor,2)))
    if i == 6:
        with col7:
            st.info("💀"' : ' + str(round(INPLAY_01Vitor*100,2)) +'%')
    if i == 7:
        with col8:
            if nbTrade_01Vitor == 0:
                st.info("🫶"' : No Trade')
            else:
                st.info("🫶"' : ' + str(nbLong_01Vitor) + ' / ' + str(nbShort_01Vitor) + ' (' + str(round((nbLong_01Vitor/nbTrade_01Vitor)*100)) + '/' + str(round((nbShort_01Vitor/nbTrade_01Vitor)*100)) + '%)')
    if i == 8:
        with col9:
            st.info("#️⃣"' : ' + str(nbTrade_01Vitor))
    if i == 9:
        with col10:
            st.info('〽️'' : ' + str(round(PNL100_01Vitor,3)) +'%')
    if i == 10:
        with col11:
            st.info('✂️'' : ' + str(round(HWM_01Vitor)))
    if i == 11:
        with col12:
            st.info('✂️'' : ' + str(round(COMMISSION_01Vitor-HWM_01Vitor,2)))
    if i == 12:
        with col13:
            if RETRO_01Vitor == 0:
                st.info("🫶"' : N/A')
            else:
                st.info('✂️'' : ' + str(round((COMMISSION_01Vitor-RETRO_01Vitor)*HWM_01Vitor,2)))


####----------------------
####---------------------- 02Joao
####----------------------

col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13 = st.columns(13)

for i in range(13):
    if i == 0:
        with col1:
            st.info('💁🏾‍♀️'' 02Joao')
    if i == 1:
        with col2:
            st.info("💰"' : ' + str(round(EQUITY_02Joao,2)))
    if i == 2:
        with col3:
            st.info("⬇️"' : ' + str(round(DEPOSIT_02Joao,2)))
    if i == 3:
        with col4:
            st.info("💸"' : ' + str(round(TAXABLE_02Joao,2)))
    if i == 4:
        with col5:
            st.info("💸"' : ' + str(round(PERF_02Joao,2)))
    if i == 5:
        with col6:
            st.info("💸"' : ' + str(round(NRZ_02Joao,2)))
    if i == 6:
        with col7:
            st.info("💀"' : ' + str(round(INPLAY_02Joao*100,2)) +'%')
    if i == 7:
        with col8:
            if nbTrade_02Joao == 0:
                st.info("🫶"' : No Trade')
            else:
                st.info("🫶"' : ' + str(nbLong_02Joao) + ' / ' + str(nbShort_02Joao) + ' (' + str(round((nbLong_02Joao/nbTrade_02Joao)*100)) + '/' + str(round((nbShort_02Joao/nbTrade_02Joao)*100)) + '%)')
    if i == 8:
        with col9:
            st.info("#️⃣"' : ' + str(nbTrade_02Joao))
    if i == 9:
        with col10:
            st.info('〽️'' : ' + str(round(PNL100_02Joao,3)) +'%')
    if i == 10:
        with col11:
            st.info('✂️'' : ' + str(round(HWM_02Joao)))
    if i == 11:
        with col12:
            st.info('✂️'' : ' + str(round(COMMISSION_02Joao-HWM_02Joao,2)))
    if i == 12:
        with col13:
            if RETRO_02Joao == 0:
                st.info("🫶"' : N/A')
            else:
                st.info('✂️'' : ' + str(round((COMMISSION_02Joao-RETRO_02Joao)*HWM_02Joao,2)))


####----------------------
####---------------------- Total
####----------------------


col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13 = st.columns(13)

for i in range(13):
    if i == 0:
        with col1:
            st.info('Total')
    if i == 1:
        with col2:
            st.info("💰"' : ' + str(round(EQUITY_01Vitor+EQUITY_02Joao, 2)))
    if i == 2:
        with col3:
            st.info("⬇️"' : ' + str(round(DEPOSIT_01Vitor+DEPOSIT_02Joao,2)))
    if i == 3:
        with col4:
            st.info("💸"' : ' + str(round(TAXABLE_01Vitor+TAXABLE_02Joao, 2)))
    if i == 4:
        with col5:
            st.info("💸"' : ' + str(round(PERF_01Vitor+PERF_02Joao, 2)))
    if i == 5:
        with col6:
            st.info("💸"' : ' + str(round(NRZ_01Vitor+NRZ_02Joao, 2)))
    if i == 6:
        with col7:
            st.info("💀 In Play 💀")
    if i == 7:
        with col8:
            st.info("🫶 Long/Short 🫶")
    if i == 8:
        with col9:
            st.info("#️⃣ Nb. T #️⃣")
    if i == 9:
        with col10:
            st.info('〽️ Perf. 〽️')
    if i == 10:
        with col11:
            st.info('✂️ HWM ✂️')
    if i == 11:
        with col12:
            st.info('✂️ Com. ✂️')
    if i == 12:
        with col13:
            st.info('✂️ Retro C. ✂️')




###################################################################################################################################################################### TOTAL DASH


###################################################################################################################################################################### POSITIONS
##----------------------------------------------------------------------->
##----------------------------------------------------------------------->
##----------------------------------------------------------------------->
##-----------------------------------------------------------------------> POSITIONS
##----------------------------------------------------------------------->
##----------------------------------------------------------------------->
##----------------------------------------------------------------------->


st.markdown('''# **Positions:**
''')

#############################################################################################################################################
#############################################################################################################################################
#############################################################################################################################################
#############################################################################################################################################
#############################################################################################################################################
#############################################################################################################################################
#############################################################################################################################################


####----------------------
####---------------------- TFio
####----------------------

col0_01, col1_01, col2_01 , col3_01, col4_01, col5_01, col6_01, col7_01, col8_01, col9_01, col10_01, col11_01, col12_01 = st.columns(13)

for i in range(13):
    if i == 0:
        with col0_01:
            st.info("All Account")
            st.info("00 - TFio")
    if i == 1:
        with col1_01:
            st.info("Symbol")
            for x in a_00TFio:
                oneTrade = posUSDT_00TFio['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00TFio['result'][x]['data']['symbol']))
    if i == 2:
        with col2_01:
            st.info("Side")
            for x in a_00TFio:
                oneTrade = posUSDT_00TFio['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00TFio['result'][x]['data']['side']))
    if i == 3:
        with col3_01:
            st.info("Size")
            for x in a_00TFio:
                oneTrade = posUSDT_00TFio['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00TFio['result'][x]['data']['size']))
    if i == 4:
        with col4_01:
            st.info("Unrealised PNL")
            for x in a_00TFio:
                oneTrade = posUSDT_00TFio['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    if posUSDT_00TFio['result'][x]['data']['unrealised_pnl'] >= 0:
                        st.success(str(round(posUSDT_00TFio['result'][x]['data']['unrealised_pnl'],2)))
                    else:
                        st.error(str(round(posUSDT_00TFio['result'][x]['data']['unrealised_pnl'],2)))
    if i == 5:
        with col5_01:
            st.info("Unrealised %")
            for x in a_00TFio:
                oneTrade = posUSDT_00TFio['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    if posUSDT_00TFio['result'][x]['data']['unrealised_pnl'] >= 0:
                        st.success(str(round((posUSDT_00TFio['result'][x]['data']['unrealised_pnl']/(posUSDT_00TFio['result'][x]['data']['entry_price']*posUSDT_00TFio['result'][x]['data']['size']))*100,2))+ '%')
                    else:
                        st.error(str(round((posUSDT_00TFio['result'][x]['data']['unrealised_pnl']/(posUSDT_00TFio['result'][x]['data']['entry_price']*posUSDT_00TFio['result'][x]['data']['size']))*100,2))+ '%')
    if i == 6:
        with col6_01:
            st.info("Realized PNL")
            for x in a_00TFio:
                oneTrade = posUSDT_00TFio['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00TFio['result'][x]['data']['cum_realised_pnl']))
    if i == 7:
        with col7_01:
            st.info("Entry Price")
            for x in a_00TFio:
                oneTrade = posUSDT_00TFio['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00TFio['result'][x]['data']['entry_price']))
    if i == 8:
        with col8_01:
            st.info("Total Size")
            for x in a_00TFio:
                oneTrade = posUSDT_00TFio['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(round(posUSDT_00TFio['result'][x]['data']['entry_price']*posUSDT_00TFio['result'][x]['data']['size'],2)))

####----------------------
####---------------------- Xm33
####----------------------

col0_01, col1_01, col2_01 , col3_01, col4_01, col5_01, col6_01, col7_01, col8_01, col9_01, col10_01, col11_01, col12_01 = st.columns(13)

for i in range(13):
    if i == 0:
        with col0_01:
            st.info("00 - Xm33")
    if i == 1:
        with col1_01:
            for x in a_00Xm33:
                oneTrade = posUSDT_00Xm33['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00Xm33['result'][x]['data']['symbol']))
    if i == 2:
        with col2_01:
            for x in a_00Xm33:
                oneTrade = posUSDT_00Xm33['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00Xm33['result'][x]['data']['side']))
    if i == 3:
        with col3_01:
            for x in a_00Xm33:
                oneTrade = posUSDT_00Xm33['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00Xm33['result'][x]['data']['size']))
    if i == 4:
        with col4_01:
            for x in a_00Xm33:
                oneTrade = posUSDT_00Xm33['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    if posUSDT_00Xm33['result'][x]['data']['unrealised_pnl'] >= 0:
                        st.success(str(round(posUSDT_00Xm33['result'][x]['data']['unrealised_pnl'],2)))
                    else:
                        st.error(str(round(posUSDT_00Xm33['result'][x]['data']['unrealised_pnl'],2)))
    if i == 5:
        with col5_01:
            for x in a_00Xm33:
                oneTrade = posUSDT_00Xm33['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    if posUSDT_00Xm33['result'][x]['data']['unrealised_pnl'] >= 0:
                        st.success(str(round((posUSDT_00Xm33['result'][x]['data']['unrealised_pnl']/(posUSDT_00Xm33['result'][x]['data']['entry_price']*posUSDT_00Xm33['result'][x]['data']['size']))*100,2))+ '%')
                    else:
                        st.error(str(round((posUSDT_00Xm33['result'][x]['data']['unrealised_pnl']/(posUSDT_00Xm33['result'][x]['data']['entry_price']*posUSDT_00Xm33['result'][x]['data']['size']))*100,2))+ '%')
    if i == 6:
        with col6_01:
            for x in a_00Xm33:
                oneTrade = posUSDT_00Xm33['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00Xm33['result'][x]['data']['cum_realised_pnl']))
    if i == 7:
        with col7_01:
            for x in a_00Xm33:
                oneTrade = posUSDT_00Xm33['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00Xm33['result'][x]['data']['entry_price']))
    if i == 8:
        with col8_01:
            for x in a_00Xm33:
                oneTrade = posUSDT_00Xm33['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(round(posUSDT_00Xm33['result'][x]['data']['entry_price']*posUSDT_00Xm33['result'][x]['data']['size'],2)))

                    

####----------------------
####---------------------- Liqi
####----------------------

col0_01, col1_01, col2_01 , col3_01, col4_01, col5_01, col6_01, col7_01, col8_01, col9_01, col10_01, col11_01, col12_01 = st.columns(13)

for i in range(13):
    if i == 0:
        with col0_01:
            st.info("00 - Liqi")
    if i == 1:
        with col1_01:
            for x in a_00Liqi:
                oneTrade = posUSDT_00Liqi['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00Liqi['result'][x]['data']['symbol']))
    if i == 2:
        with col2_01:
            for x in a_00Liqi:
                oneTrade = posUSDT_00Liqi['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00Liqi['result'][x]['data']['side']))
    if i == 3:
        with col3_01:
            for x in a_00Liqi:
                oneTrade = posUSDT_00Liqi['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00Liqi['result'][x]['data']['size']))
    if i == 4:
        with col4_01:
            for x in a_00Liqi:
                oneTrade = posUSDT_00Liqi['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    if posUSDT_00Liqi['result'][x]['data']['unrealised_pnl'] >= 0:
                        st.success(str(round(posUSDT_00Liqi['result'][x]['data']['unrealised_pnl'],2)))
                    else:
                        st.error(str(round(posUSDT_00Liqi['result'][x]['data']['unrealised_pnl'],2)))
    if i == 5:
        with col5_01:
            for x in a_00Liqi:
                oneTrade = posUSDT_00Liqi['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    if posUSDT_00Liqi['result'][x]['data']['unrealised_pnl'] >= 0:
                        st.success(str(round((posUSDT_00Liqi['result'][x]['data']['unrealised_pnl']/(posUSDT_00Liqi['result'][x]['data']['entry_price']*posUSDT_00Liqi['result'][x]['data']['size']))*100,2))+ '%')
                    else:
                        st.error(str(round((posUSDT_00Liqi['result'][x]['data']['unrealised_pnl']/(posUSDT_00Liqi['result'][x]['data']['entry_price']*posUSDT_00Liqi['result'][x]['data']['size']))*100,2))+ '%')
    if i == 6:
        with col6_01:
            for x in a_00Liqi:
                oneTrade = posUSDT_00Liqi['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00Liqi['result'][x]['data']['cum_realised_pnl']))
    if i == 7:
        with col7_01:
            for x in a_00Liqi:
                oneTrade = posUSDT_00Liqi['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00Liqi['result'][x]['data']['entry_price']))
    if i == 8:
        with col8_01:
            for x in a_00Liqi:
                oneTrade = posUSDT_00Liqi['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(round(posUSDT_00Liqi['result'][x]['data']['entry_price']*posUSDT_00Liqi['result'][x]['data']['size'],2)))

                    
                    
                    
                    
                    
st.markdown('''# **Clients**''')




####----------------------
####---------------------- 01Vitor
####----------------------

col0_01, col1_01, col2_01 , col3_01, col4_01, col5_01, col6_01, col7_01, col8_01, col9_01, col10_01, col11_01, col12_01 = st.columns(13)

for i in range(13):
    if i == 0:
        with col0_01:
            st.info("01 - Vitor")
    if i == 1:
        with col1_01:
            for x in a_01Vitor:
                oneTrade = posUSDT_01Vitor['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_01Vitor['result'][x]['data']['symbol']))
    if i == 2:
        with col2_01:
            for x in a_01Vitor:
                oneTrade = posUSDT_01Vitor['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_01Vitor['result'][x]['data']['side']))
    if i == 3:
        with col3_01:
            for x in a_01Vitor:
                oneTrade = posUSDT_01Vitor['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_01Vitor['result'][x]['data']['size']))
    if i == 4:
        with col4_01:
            for x in a_01Vitor:
                oneTrade = posUSDT_01Vitor['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    if posUSDT_01Vitor['result'][x]['data']['unrealised_pnl'] >= 0:
                        st.success(str(round(posUSDT_01Vitor['result'][x]['data']['unrealised_pnl'],2)))
                    else:
                        st.error(str(round(posUSDT_01Vitor['result'][x]['data']['unrealised_pnl'],2)))
    if i == 5:
        with col5_01:
            for x in a_01Vitor:
                oneTrade = posUSDT_01Vitor['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    if posUSDT_01Vitor['result'][x]['data']['unrealised_pnl'] >= 0:
                        st.success(str(round((posUSDT_01Vitor['result'][x]['data']['unrealised_pnl']/(posUSDT_01Vitor['result'][x]['data']['entry_price']*posUSDT_01Vitor['result'][x]['data']['size']))*100,2))+ '%')
                    else:
                        st.error(str(round((posUSDT_01Vitor['result'][x]['data']['unrealised_pnl']/(posUSDT_01Vitor['result'][x]['data']['entry_price']*posUSDT_01Vitor['result'][x]['data']['size']))*100,2))+ '%')
    if i == 6:
        with col6_01:
            for x in a_01Vitor:
                oneTrade = posUSDT_01Vitor['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_01Vitor['result'][x]['data']['cum_realised_pnl']))
    if i == 7:
        with col7_01:
            for x in a_01Vitor:
                oneTrade = posUSDT_01Vitor['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_01Vitor['result'][x]['data']['entry_price']))
    if i == 8:
        with col8_01:
            for x in a_01Vitor:
                oneTrade = posUSDT_01Vitor['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(round(posUSDT_01Vitor['result'][x]['data']['entry_price']*posUSDT_01Vitor['result'][x]['data']['size'],2)))

####----------------------
####---------------------- 02Joao
####----------------------

col0_01, col1_01, col2_01 , col3_01, col4_01, col5_01, col6_01, col7_01, col8_01, col9_01, col10_01, col11_01, col12_01 = st.columns(13)

for i in range(13):
    if i == 0:
        with col0_01:
            st.info("02 - Joao")
    if i == 1:
        with col1_01:
            for x in a_02Joao:
                oneTrade = posUSDT_02Joao['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_02Joao['result'][x]['data']['symbol']))
    if i == 2:
        with col2_01:
            for x in a_02Joao:
                oneTrade = posUSDT_02Joao['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_02Joao['result'][x]['data']['side']))
    if i == 3:
        with col3_01:
            for x in a_02Joao:
                oneTrade = posUSDT_02Joao['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_02Joao['result'][x]['data']['size']))
    if i == 4:
        with col4_01:
            for x in a_02Joao:
                oneTrade = posUSDT_02Joao['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    if posUSDT_02Joao['result'][x]['data']['unrealised_pnl'] >= 0:
                        st.success(str(round(posUSDT_02Joao['result'][x]['data']['unrealised_pnl'],2)))
                    else:
                        st.error(str(round(posUSDT_02Joao['result'][x]['data']['unrealised_pnl'],2)))
    if i == 5:
        with col5_01:
            for x in a_02Joao:
                oneTrade = posUSDT_02Joao['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    if posUSDT_02Joao['result'][x]['data']['unrealised_pnl'] >= 0:
                        st.success(str(round((posUSDT_02Joao['result'][x]['data']['unrealised_pnl']/(posUSDT_02Joao['result'][x]['data']['entry_price']*posUSDT_02Joao['result'][x]['data']['size']))*100,2))+ '%')
                    else:
                        st.error(str(round((posUSDT_02Joao['result'][x]['data']['unrealised_pnl']/(posUSDT_02Joao['result'][x]['data']['entry_price']*posUSDT_02Joao['result'][x]['data']['size']))*100,2))+ '%')
    if i == 6:
        with col6_01:
            for x in a_02Joao:
                oneTrade = posUSDT_02Joao['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_02Joao['result'][x]['data']['cum_realised_pnl']))
    if i == 7:
        with col7_01:
            for x in a_02Joao:
                oneTrade = posUSDT_02Joao['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_02Joao['result'][x]['data']['entry_price']))
    if i == 8:
        with col8_01:
            for x in a_02Joao:
                oneTrade = posUSDT_02Joao['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(round(posUSDT_02Joao['result'][x]['data']['entry_price']*posUSDT_02Joao['result'][x]['data']['size'],2)))

  
                    
                    
                    
                    
############################################################################################################ ONE-WAY

# print("Change A !")
# st.header("Change A  !")
#
# for x in a:
#     try:
#         ii_00 = str(posUSDT_00TFio['result'][x]['data']['symbol'])
#         print(session_auth_00TFio.position_mode_switch(symbol=(ii_00), mode="MergedSingle"))
#         print(posUSDT_00TFio['result'][x]['data']['symbol'])
#         ii_01 = str(posUSDT_00Xm33['result'][x]['data']['symbol'])
#         print(session_auth_00Xm33.position_mode_switch(symbol=(ii_01), mode="MergedSingle"))
#         print(posUSDT_00Xm33['result'][x]['data']['symbol'])
#         print("ok")
#     except:
#         #print("pass")
#         pass
#
#
#
# print("Done !")
# st.header("Done !")

############################################################################################################ CLOSED TRADES

st.header('**All Trades**')

print("Begin !")
st.header("Begin !")

from datetime import datetime, date, time, timezone
now = datetime.now() # current date and time
Unix = datetime.timestamp(now)
UnixY = datetime.timestamp(now) - 24*3600
dt1 = datetime.fromtimestamp(Unix)
dt2 = datetime.fromtimestamp(UnixY)
print(dt1)

for x in a_00Xm33:
    try:
        ii = str(posUSDT_00Xm33['result'][x]['data']['symbol'])
        authPNL_00Xm33 = session_auth_00Xm33.closed_profit_and_loss(symbol=(ii))
        for i in range(0,len(authPNL_00Xm33)):
            #print(authPNL_00["result"]["data"][i]["created_at"])
            if authPNL_00Xm33["result"]["data"][i]["created_at"] > UnixY:
                #print("Id: " + str(authPNL_00Xm33["result"]["data"][i]["id"]) + " Time: " + str(authPNL_00Xm33["result"]["data"][i]["created_at"]) + " Symbole: " + str(authPNL_00Xm33["result"]["data"][i]["symbol"]) + " Side: " + str(authPNL_00Xm33["result"]["data"][i]["side"]) + " Entry Price: " + str(authPNL_00Xm33["result"]["data"][i]["avg_entry_price"]) + " Exit Price: " + str(authPNL_00Xm33["result"]["data"][i]["avg_exit_price"]) + " PNL: " + str(authPNL_00Xm33["result"]["data"][i]["closed_pnl"]) + " $IN$: " + str(authPNL_00Xm33["result"]["data"][i]["cum_entry_value"]) + " $OUT$: " + str(authPNL_00Xm33["result"]["data"][i]["cum_exit_value"]))
                #st.subheader(str(("Id: " + str(authPNL_00Xm33["result"]["data"][i]["id"]) + " Time: " + str(authPNL_00Xm33["result"]["data"][i]["created_at"]) + " Symbole: " + str(authPNL_00Xm33["result"]["data"][i]["symbol"]) + " Side: " + str(authPNL_00Xm33["result"]["data"][i]["side"]) + " Entry Price: " + str(authPNL_00Xm33["result"]["data"][i]["avg_entry_price"]) + " Exit Price: " + str(authPNL_00Xm33["result"]["data"][i]["avg_exit_price"]) + " PNL: " + str(authPNL_00Xm33["result"]["data"][i]["closed_pnl"]) + " $IN$: " + str(authPNL_00Xm33["result"]["data"][i]["cum_entry_value"]) + " $OUT$: " + str(authPNL_00Xm33["result"]["data"][i]["cum_exit_value"]))))
                if str(authPNL_00Xm33["result"]["data"][i]["side"]) == "Buy":
                    print(str(datetime.fromtimestamp(authPNL_00Xm33["result"]["data"][i]["created_at"])) + " Symbol: " + str(authPNL_00Xm33["result"]["data"][i]["symbol"]) + " Short: " + str(round((((authPNL_00Xm33["result"]["data"][i]["avg_exit_price"] / authPNL_00Xm33["result"]["data"][i]["avg_entry_price"] - 1) * -100)),2)) + "%")
                    st.subheader(str(datetime.fromtimestamp(authPNL_00Xm33["result"]["data"][i]["created_at"]+7200)) + " Symbol: " + str(authPNL_00Xm33["result"]["data"][i]["symbol"]) + " Short: " + str(round((((authPNL_00Xm33["result"]["data"][i]["avg_exit_price"] / authPNL_00Xm33["result"]["data"][i]["avg_entry_price"] - 1) * -100)), 2)) + "%")
                elif str(authPNL_00Xm33["result"]["data"][i]["side"]) == "Sell":
                    print(str(datetime.fromtimestamp(authPNL_00Xm33["result"]["data"][i]["created_at"])) + " Symbol: " + str(authPNL_00Xm33["result"]["data"][i]["symbol"]) + " Long: " + str(round((((authPNL_00Xm33["result"]["data"][i]["avg_exit_price"] / authPNL_00Xm33["result"]["data"][i]["avg_entry_price"] - 1) * 100)),2)) + "%")
                    st.subheader(str(datetime.fromtimestamp(authPNL_00Xm33["result"]["data"][i]["created_at"]+7200)) + " Symbol: " + str(authPNL_00Xm33["result"]["data"][i]["symbol"]) + " Long: " + str(round((((authPNL_00Xm33["result"]["data"][i]["avg_exit_price"] / authPNL_00Xm33["result"]["data"][i]["avg_entry_price"] - 1) * 100)), 2)) + "%")
                else:
                    print("N/A")
                    st.subheader("N/A")
    except:
        pass




print("Done !")
st.header("Done !")

