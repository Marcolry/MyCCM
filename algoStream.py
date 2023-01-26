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


c00TFio = np.array(['00TFio', st.secrets["aK00TFio"], st.secrets["aS00TFio"], 0.3, 1/3, 0])
c00Xm33 = np.array(['00Xm33', st.secrets["aK00Xm33"], st.secrets["aS00Xm33"], 0.3, 0, 0])


allUsers = np.array([c00TFio, c00Xm33])


session_auth_00TFio = usdt_perpetual.HTTP(endpoint="https://api.bybit.com",api_key=st.secrets["aK00TFio"],api_secret=st.secrets["aS00TFio"])
session_auth_00Xm33 = usdt_perpetual.HTTP(endpoint="https://api.bybit.com",api_key=st.secrets["aK00Xm33"],api_secret=st.secrets["aS00Xm33"])


authUSDT_00TFio = session_auth_00TFio.get_wallet_balance()
authUSDT_00Xm33 = session_auth_00Xm33.get_wallet_balance()

posUSDT_00TFio = session_auth_00TFio.my_position()
posUSDT_00Xm33 = session_auth_00Xm33.my_position()



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




############################################################################################################ PRICE

client = bybit.bybit(test=False, api_key=st.secrets["aK00TFio"], api_secret=st.secrets["aS00TFio"])
info = client.Market.Market_symbolInfo().result()
keys = info[0]['result']
btc = keys[42]['last_price']
name = keys[42]['symbol']

############################################################################################################




########################### First Line

col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13 = st.columns(13)

for i in range(13):
    if i == 0:
        with col1:
            st.info("₿: "+ btc)
            st.info('💁🏾‍♀️'' 00TFio')
            st.info('💁🏾‍♀️'' 00Xm33')
            #st.info('💁🏾‍♀️'' 00TFio')
            st.info("💰"' : ' + str(round((EQUITY_00TFio + EQUITY_00Xm33)/float(btc), 4)) + ' BTC')
    if i == 1:
        with col2:
            st.info("💰 Equity 💰")
            st.info("💰"' : ' + str(round(EQUITY_00TFio,2)))
            st.info("💰"' : ' + str(round(EQUITY_00Xm33,2)))
            #st.info("💰"' : ' + str(round(EQUITY_00TFio,2)))
            st.info("💰"' : ' + str(round(EQUITY_00TFio + EQUITY_00Xm33, 2)))
    if i == 2:
        with col3:
            st.info("⬇️ Deposit ⬇️")
            st.info("⬇️"' : ' + str(round(DEPOSIT_00TFio,2)))
            st.info("⬇️"' : ' + str(round(DEPOSIT_00Xm33,2)))
            #st.info("⬇️"' : ' + str(round(DEPOSIT_00TFio,2)))
            st.info("⬇️"' : ' + str(round(DEPOSIT_00TFio + DEPOSIT_00Xm33, 1)))
    if i == 3:
        with col4:
            st.info("💸 Bénéfice 💸")
            st.info("💸"' : ' + str(round(TAXABLE_00TFio,2)))
            st.info("💸"' : ' + str(round(TAXABLE_00Xm33,2)))
            #st.info("💸"' : ' + str(round(TAXABLE_00TFio,2)))
            st.info("💸"' : ' + str(round(TAXABLE_00TFio + TAXABLE_00Xm33, 2)))
    if i == 4:
        with col5:
            st.info("💸 Realized 💸")
            st.info("💸"' : ' + str(round(PERF_00TFio,2)))
            st.info("💸"' : ' + str(round(PERF_00Xm33,2)))
            #st.info("💸"' : ' + str(round(PERF_00TFio,2)))
            st.info("💸"' : ' + str(round(PERF_00TFio + PERF_00Xm33, 2)))
    if i == 5:
        with col6:
            st.info("💸 Unrealized 💸")
            st.info("💸"' : ' + str(round(NRZ_00TFio,2)))
            st.info("💸"' : ' + str(round(NRZ_00Xm33,2)))
            #st.info("💸"' : ' + str(round(NRZ_00TFio,2)))
            st.info("💸"' : ' + str(round(NRZ_00TFio + NRZ_00Xm33, 2)))
    if i == 6:
        with col7:
            st.info("💀 In Play 💀")
            st.info("💀"' : ' + str(round(INPLAY_00TFio*100,2)) +'%')
            st.info("💀"' : ' + str(round(INPLAY_00Xm33*100,2)) +'%')
            #st.info("💀"' : ' + str(round(INPLAY_00TFio*100,2)) +'%')
            st.info("💀"' : ' + str(round((EQUITY_00TFio + EQUITY_00Xm33 - AVAILABLE_00TFio - AVAILABLE_00Xm33) * 100 / (EQUITY_00TFio + EQUITY_00Xm33), 2)) + '%')
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
            # if nbTrade_00TFio == 0:
            #     st.info("🫶"' : No Trade')
            # else:
            #     st.info("🫶"' : ' + str(nbLong_00TFio) + ' / ' + str(nbShort_00TFio) + ' (' + str(round((nbLong_00TFio/nbTrade_00TFio)*100)) + '/' + str(round((nbShort_00TFio/nbTrade_00TFio)*100)) + '%)')
            st.info("🫶 Long/Short 🫶")
    if i == 8:
        with col9:
            st.info("#️⃣ Nb. T #️⃣")
            st.info("#️⃣"' : ' + str(nbTrade_00TFio))
            st.info("#️⃣"' : ' + str(nbTrade_00Xm33))
            #st.info("#️⃣"' : ' + str(nbTrade_00TFio))
            st.info("#️⃣"' : ' + str(nbTrade_00TFio + nbTrade_00Xm33))
    if i == 9:
        with col10:
            st.info('〽️ Perf. 〽️')
            st.info('〽️'' : ' + str(round(PNL100_00TFio,3)) +'%')
            st.info('〽️'' : ' + str(round(PNL100_00Xm33,3)) +'%')
            #st.info('〽️'' : ' + str(round(PNL100_00TFio,3)) +'%')
            st.info('〽️'' : ' + str(round((PNL100_00TFio * DEPOSIT_00TFio + PNL100_00Xm33 * DEPOSIT_00Xm33) / (DEPOSIT_00TFio + DEPOSIT_00Xm33), 2)) + '%')
    if i == 10:
        with col11:
            st.info('✂️ HWM ✂️')
            st.info('✂️'' : ' + str(round(HWM_00TFio)))
            st.info('✂️'' : ' + str(round(HWM_00Xm33)))
            #st.info('✂️'' : ' + str(round(HWM_00TFio)))
            st.info('✂️'' : ' + str(round(HWM_00TFio+HWM_00Xm33)))
    if i == 11:
        with col12:
            st.info('✂️ Com. ✂️')
            st.info('✂️'' : ' + str(round(COMMISSION_00TFio-HWM_00TFio,2)))
            st.info('✂️'' : ' + str(round(COMMISSION_00Xm33-HWM_00Xm33,2)))
            #st.info('✂️'' : ' + str(round(COMMISSION_00TFio-HWM_00TFio,2)))
            st.info('✂️'' : ' + str(round(COMMISSION_00TFio + COMMISSION_00Xm33 - HWM_00TFio - HWM_00Xm33, 2)))
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
            # if RETRO_00TFio == 0 or COMMISSION_00TFio-HWM_00TFio <= 0:
            #     st.info("🫶"' : N/A')
            # else:
            #     st.info('✂️'' : ' + str(round((COMMISSION_00TFio-HWM_00TFio)*RETRO_00TFio,2)))
            st.info('✂️'' : ' + str(round((COMMISSION_00TFio - HWM_00TFio) * RETRO_00TFio + (COMMISSION_00Xm33 - HWM_00Xm33) * RETRO_00Xm33, 2)))





###################################################################################################################################################################### 00 - Feli


###################################################################################################################################################################### 00 - Marc






























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

##########################



# -----------------------------------------------------------------------> 00 - Feli
# -----------------------------------------------------------------------> 00 - Feli
# -----------------------------------------------------------------------> 00 - Feli
# -----------------------------------------------------------------------> 00 - Feli
# -----------------------------------------------------------------------> 00 - Feli

col0_01, col1_01, col2_01 , col3_01, col4_01, col5_01, col6_01, col7_01, col8_01, col9_01, col10_01, col11_01, col12_01 = st.columns(13)

for i in range(13):
    if i == 0:
        with col0_01:
            st.info("All Account")
            st.info("00 - Feli")
    if i == 1:
        with col1_01:
            st.info("Symbol")
            for x in a:
                oneTrade = posUSDT_00TFio['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00TFio['result'][x]['data']['symbol']))
    if i == 2:
        with col2_01:
            st.info("Side")
            for x in a:
                oneTrade = posUSDT_00TFio['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00TFio['result'][x]['data']['side']))
    if i == 3:
        with col3_01:
            st.info("Size")
            for x in a:
                oneTrade = posUSDT_00TFio['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00TFio['result'][x]['data']['size']))
    if i == 4:
        with col4_01:
            st.info("Unrealised PNL")
            for x in a:
                oneTrade = posUSDT_00TFio['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    if posUSDT_00TFio['result'][x]['data']['unrealised_pnl'] >= 0:
                        st.success(str(round(posUSDT_00TFio['result'][x]['data']['unrealised_pnl'],2)))
                    else:
                        st.error(str(round(posUSDT_00TFio['result'][x]['data']['unrealised_pnl'],2)))
    if i == 5:
        with col5_01:
            st.info("Unrealised %")
            for x in a:
                oneTrade = posUSDT_00TFio['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    if posUSDT_00TFio['result'][x]['data']['unrealised_pnl'] >= 0:
                        st.success(str(round((posUSDT_00TFio['result'][x]['data']['unrealised_pnl']/(posUSDT_00TFio['result'][x]['data']['entry_price']*posUSDT_00TFio['result'][x]['data']['size']))*100,2))+ '%')
                    else:
                        st.error(str(round((posUSDT_00TFio['result'][x]['data']['unrealised_pnl']/(posUSDT_00TFio['result'][x]['data']['entry_price']*posUSDT_00TFio['result'][x]['data']['size']))*100,2))+ '%')
    if i == 6:
        with col6_01:
            st.info("Realized PNL")
            for x in a:
                oneTrade = posUSDT_00TFio['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00TFio['result'][x]['data']['cum_realised_pnl']))
    if i == 7:
        with col7_01:
            st.info("Entry Price")
            for x in a:
                oneTrade = posUSDT_00TFio['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00TFio['result'][x]['data']['entry_price']))
    if i == 8:
        with col8_01:
            st.info("Total Size")
            for x in a:
                oneTrade = posUSDT_00TFio['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(round(posUSDT_00TFio['result'][x]['data']['entry_price']*posUSDT_00TFio['result'][x]['data']['size'],2)))


##-----------------------------------------------------------------------> 00 - Feli
##-----------------------------------------------------------------------> 00 - Feli
##-----------------------------------------------------------------------> 00 - Feli
##-----------------------------------------------------------------------> 00 - Feli
##-----------------------------------------------------------------------> 00 - Feli



#st.markdown('''# **Detail: 👨🏽‍🎓 01 - Marc**
#''')

##########################


##-----------------------------------------------------------------------> 01 - Marc


col0_01, col1_01, col2_01 , col3_01, col4_01, col5_01, col6_01, col7_01, col8_01, col9_01, col10_01, col11_01, col12_01 = st.columns(13)

for i in range(13):
    if i == 0:
        with col0_01:
            st.info("00 - Marc")
    if i == 1:
        with col1_01:
            for x in a:
                oneTrade = posUSDT_00Xm33['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00Xm33['result'][x]['data']['symbol']))
    if i == 2:
        with col2_01:
            for x in a:
                oneTrade = posUSDT_00Xm33['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00Xm33['result'][x]['data']['side']))
    if i == 3:
        with col3_01:
            for x in a:
                oneTrade = posUSDT_00Xm33['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00Xm33['result'][x]['data']['size']))
    if i == 4:
        with col4_01:
            for x in a:
                oneTrade = posUSDT_00Xm33['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    if posUSDT_00Xm33['result'][x]['data']['unrealised_pnl'] >= 0:
                        st.success(str(round(posUSDT_00Xm33['result'][x]['data']['unrealised_pnl'],2)))
                    else:
                        st.error(str(round(posUSDT_00Xm33['result'][x]['data']['unrealised_pnl'],2)))
    if i == 5:
        with col5_01:
            for x in a:
                oneTrade = posUSDT_00Xm33['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    if posUSDT_00Xm33['result'][x]['data']['unrealised_pnl'] >= 0:
                        st.success(str(round((posUSDT_00Xm33['result'][x]['data']['unrealised_pnl']/(posUSDT_00Xm33['result'][x]['data']['entry_price']*posUSDT_00Xm33['result'][x]['data']['size']))*100,2))+ '%')
                    else:
                        st.error(str(round((posUSDT_00Xm33['result'][x]['data']['unrealised_pnl']/(posUSDT_00Xm33['result'][x]['data']['entry_price']*posUSDT_00Xm33['result'][x]['data']['size']))*100,2))+ '%')
    if i == 6:
        with col6_01:
            for x in a:
                oneTrade = posUSDT_00Xm33['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00Xm33['result'][x]['data']['cum_realised_pnl']))
    if i == 7:
        with col7_01:
            for x in a:
                oneTrade = posUSDT_00Xm33['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00Xm33['result'][x]['data']['entry_price']))
    if i == 8:
        with col8_01:
            for x in a:
                oneTrade = posUSDT_00Xm33['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(round(posUSDT_00Xm33['result'][x]['data']['entry_price']*posUSDT_00Xm33['result'][x]['data']['size'],2)))


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

for x in a:
    try:
        ii = str(posUSDT_00Xm33['result'][x]['data']['symbol'])
        authPNL_01 = session_auth_00Xm33.closed_profit_and_loss(symbol=(ii))
        for i in range(0,len(authPNL_01)):
            #print(authPNL_00["result"]["data"][i]["created_at"])
            if authPNL_01["result"]["data"][i]["created_at"] > UnixY:
                #print("Id: " + str(authPNL_01["result"]["data"][i]["id"]) + " Time: " + str(authPNL_01["result"]["data"][i]["created_at"]) + " Symbole: " + str(authPNL_01["result"]["data"][i]["symbol"]) + " Side: " + str(authPNL_01["result"]["data"][i]["side"]) + " Entry Price: " + str(authPNL_01["result"]["data"][i]["avg_entry_price"]) + " Exit Price: " + str(authPNL_01["result"]["data"][i]["avg_exit_price"]) + " PNL: " + str(authPNL_01["result"]["data"][i]["closed_pnl"]) + " $IN$: " + str(authPNL_01["result"]["data"][i]["cum_entry_value"]) + " $OUT$: " + str(authPNL_01["result"]["data"][i]["cum_exit_value"]))
                #st.subheader(str(("Id: " + str(authPNL_01["result"]["data"][i]["id"]) + " Time: " + str(authPNL_01["result"]["data"][i]["created_at"]) + " Symbole: " + str(authPNL_01["result"]["data"][i]["symbol"]) + " Side: " + str(authPNL_01["result"]["data"][i]["side"]) + " Entry Price: " + str(authPNL_01["result"]["data"][i]["avg_entry_price"]) + " Exit Price: " + str(authPNL_01["result"]["data"][i]["avg_exit_price"]) + " PNL: " + str(authPNL_01["result"]["data"][i]["closed_pnl"]) + " $IN$: " + str(authPNL_01["result"]["data"][i]["cum_entry_value"]) + " $OUT$: " + str(authPNL_01["result"]["data"][i]["cum_exit_value"]))))
                if str(authPNL_01["result"]["data"][i]["side"]) == "Buy":
                    #print(str(datetime.fromtimestamp(authPNL_01["result"]["data"][i]["created_at"])) + " Symbol: " + str(authPNL_01["result"]["data"][i]["symbol"]) + " Short: " + str(round((((authPNL_01["result"]["data"][i]["avg_exit_price"] / authPNL_01["result"]["data"][i]["avg_entry_price"] - 1) * -100)-0.12),2)) + "%")
                    st.subheader(str(datetime.fromtimestamp(authPNL_01["result"]["data"][i]["created_at"]+7200)) + " Symbol: " + str(authPNL_01["result"]["data"][i]["symbol"]) + " Short: " + str(round((((authPNL_01["result"]["data"][i]["avg_exit_price"] / authPNL_01["result"]["data"][i]["avg_entry_price"] - 1) * -100) - 0.12), 2)) + "%")
                elif str(authPNL_01["result"]["data"][i]["side"]) == "Sell":
                    #print(str(datetime.fromtimestamp(authPNL_01["result"]["data"][i]["created_at"])) + " Symbol: " + str(authPNL_01["result"]["data"][i]["symbol"]) + " Long: " + str(round((((authPNL_01["result"]["data"][i]["avg_exit_price"] / authPNL_01["result"]["data"][i]["avg_entry_price"] - 1) * 100)-0.12),2)) + "%")
                    st.subheader(str(datetime.fromtimestamp(authPNL_01["result"]["data"][i]["created_at"]+7200)) + " Symbol: " + str(authPNL_01["result"]["data"][i]["symbol"]) + " Long: " + str(round((((authPNL_01["result"]["data"][i]["avg_exit_price"] / authPNL_01["result"]["data"][i]["avg_entry_price"] - 1) * 100) - 0.12), 2)) + "%")
                else:
                    print("N/A")
                    st.subheader("N/A")
    except:
        pass


print("Done !")
st.header("Done !")

