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
#from requests import ge
#ip = get('https://api.ipify.org').text
#print(f'My public IP is: {ip}')
#st.write('**Local IP:** ' + str(local_ip) + ' // **Public IP:** ' + str(ip))


#Config Final Array:
# Nom, aK, aS, Tx, RetroC, HWM 

st.markdown('''# **AlgoFinance AUM**
''')

###################################################################################################################################################################### API

TXCOM_00TFio = 1
RETRO_00TFio = 0
HWM_00TFio = 0
c00TFio = np.array(['00TFio', st.secrets["aK00TFio"], st.secrets["aS00TFio"], 0.3, 1/3, 0])
session_auth_00TFio = usdt_perpetual.HTTP(endpoint="https://api.bybit.com",api_key=st.secrets["aK00TFio"],api_secret=st.secrets["aS00TFio"])
authUSDT_00TFio = session_auth_00TFio.get_wallet_balance()
posUSDT_00TFio = session_auth_00TFio.my_position()


TXCOM_01Vitor = 0.1
RETRO_01Vitor = 0
HWM_01Vitor = 150
c01Vitor = np.array(['01Vitor', st.secrets["aK01Vitor"], st.secrets["aS01Vitor"], 0.3, 0, 0])
session_auth_01Vitor = usdt_perpetual.HTTP(endpoint="https://api.bybit.com",api_key=st.secrets["aK01Vitor"],api_secret=st.secrets["aS01Vitor"])
authUSDT_01Vitor = session_auth_01Vitor.get_wallet_balance()
posUSDT_01Vitor = session_auth_01Vitor.my_position()


TXCOM_02Joao = 0.1
RETRO_02Joao = 0
HWM_02Joao = 0
c02Joao = np.array(['02Joao', st.secrets["aK02Joao"], st.secrets["aS02Joao"], 0.3, 0, 0])
session_auth_02Joao = usdt_perpetual.HTTP(endpoint="https://api.bybit.com",api_key=st.secrets["aK02Joao"],api_secret=st.secrets["aS02Joao"])
authUSDT_02Joao = session_auth_02Joao.get_wallet_balance()
posUSDT_02Joao = session_auth_02Joao.my_position()

TXCOM_03Rayan = 0.1
RETRO_03Rayan = 0
HWM_03Rayan = 0
c03Rayan = np.array(['03Rayan', st.secrets["aK03Rayan"], st.secrets["aS03Rayan"], 0.3, 0, 0])
session_auth_03Rayan = usdt_perpetual.HTTP(endpoint="https://api.bybit.com",api_key=st.secrets["aK03Rayan"],api_secret=st.secrets["aS03Rayan"])
authUSDT_03Rayan = session_auth_03Rayan.get_wallet_balance()
posUSDT_03Rayan = session_auth_03Rayan.my_position()


TXCOM_04Sandra = 0.1
RETRO_04Sandra = 0
HWM_04Sandra = 0
c04Sandra = np.array(['04Sandra', st.secrets["aK04Sandra"], st.secrets["aS04Sandra"], 0.3, 0, 0])
session_auth_04Sandra = usdt_perpetual.HTTP(endpoint="https://api.bybit.com",api_key=st.secrets["aK04Sandra"],api_secret=st.secrets["aS04Sandra"])
authUSDT_04Sandra = session_auth_04Sandra.get_wallet_balance()
posUSDT_04Sandra = session_auth_04Sandra.my_position()



allUsers = np.array([c00TFio, c01Vitor, c02Joao, c03Rayan, c04Sandra])





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

###################################################################################################################################################################### API


#print(len(posUSDT_00TFio['result']))

##-----------------------------------------------------------------------> API LIMIT

st.write('**Request Limit:** ' + str(STATELIMIT_00) + '/' + str(RATELIMIT_00))


###################################################################################################################################################################### DASHBOARD

###################################################################################################################################################################### CONFIG 00TFio

###################################################################################################################################################################### CONFIG 00TFio



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


###################################################################################################################################################################### CONFIG 01Vitor

###################################################################################################################################################################### CONFIG 01Vitor


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


###################################################################################################################################################################### CONFIG 02Joao

###################################################################################################################################################################### CONFIG 02Joao


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


###################################################################################################################################################################### CONFIG 03Rayan

###################################################################################################################################################################### CONFIG 03Rayan

ALL_03Rayan = list(range(0, len(posUSDT_03Rayan['result']))) #print(ALL)
a_03Rayan = arr.array('i', ALL_03Rayan)

######################################################################################### DATA

EQUITY_03Rayan = authUSDT_03Rayan['result']['USDT']['equity']
NRZ_03Rayan = authUSDT_03Rayan['result']['USDT']['unrealised_pnl']
PERF_03Rayan = authUSDT_03Rayan['result']['USDT']['cum_realised_pnl']
AVAILABLE_03Rayan = authUSDT_03Rayan['result']['USDT']['available_balance']
INPLAY_03Rayan = (EQUITY_03Rayan - AVAILABLE_03Rayan)/EQUITY_03Rayan


DEPOSIT_03Rayan = EQUITY_03Rayan - NRZ_03Rayan - PERF_03Rayan
PNL100_03Rayan = (round(EQUITY_03Rayan/DEPOSIT_03Rayan,4)-1)*100

TAXABLE_03Rayan = NRZ_03Rayan + PERF_03Rayan

if TAXABLE_03Rayan > 0:
    COMMISSION_03Rayan = TAXABLE_03Rayan * TXCOM_03Rayan
if TAXABLE_03Rayan <= 0:
    COMMISSION_03Rayan = 0


######################################################################################### NB

nbTrade_03Rayan = 0
nbLong_03Rayan = 0
nbShort_03Rayan = 0

for x in a_03Rayan:
   oneTrade = posUSDT_03Rayan['result'][x]['data']["entry_price"] != 0
   if oneTrade:
       nbTrade_03Rayan += 1

for x in a_03Rayan:
   oneLong = posUSDT_03Rayan['result'][x]['data']["side"] == "Buy" and posUSDT_03Rayan['result'][x]['data']["entry_price"] != 0
   if oneLong:
       nbLong_03Rayan += 1

for x in a_03Rayan:
   oneShort = posUSDT_03Rayan['result'][x]['data']["side"] == "Sell" and posUSDT_03Rayan['result'][x]['data']["entry_price"] != 0
   if oneShort:
       nbShort_03Rayan += 1



###################################################################################################################################################################### CONFIG 04Sandra

###################################################################################################################################################################### CONFIG 04Sandra

ALL_04Sandra = list(range(0, len(posUSDT_04Sandra['result']))) #print(ALL)
a_04Sandra = arr.array('i', ALL_04Sandra)

######################################################################################### DATA

EQUITY_04Sandra = authUSDT_04Sandra['result']['USDT']['equity']
NRZ_04Sandra = authUSDT_04Sandra['result']['USDT']['unrealised_pnl']
PERF_04Sandra = authUSDT_04Sandra['result']['USDT']['cum_realised_pnl'] - 262.57
AVAILABLE_04Sandra = authUSDT_04Sandra['result']['USDT']['available_balance']
INPLAY_04Sandra = (EQUITY_04Sandra - AVAILABLE_04Sandra)/EQUITY_04Sandra


DEPOSIT_04Sandra = EQUITY_04Sandra - NRZ_04Sandra - PERF_04Sandra
PNL100_04Sandra = (round(EQUITY_04Sandra/DEPOSIT_04Sandra,4)-1)*100

TAXABLE_04Sandra = NRZ_04Sandra + PERF_04Sandra

if TAXABLE_04Sandra > 0:
    COMMISSION_04Sandra = TAXABLE_04Sandra * TXCOM_04Sandra
if TAXABLE_04Sandra <= 0:
    COMMISSION_04Sandra = 0


######################################################################################### NB

nbTrade_04Sandra = 0
nbLong_04Sandra = 0
nbShort_04Sandra = 0

for x in a_04Sandra:
   oneTrade = posUSDT_04Sandra['result'][x]['data']["entry_price"] != 0
   if oneTrade:
       nbTrade_04Sandra += 1

for x in a_04Sandra:
   oneLong = posUSDT_04Sandra['result'][x]['data']["side"] == "Buy" and posUSDT_04Sandra['result'][x]['data']["entry_price"] != 0
   if oneLong:
       nbLong_04Sandra += 1

for x in a_04Sandra:
   oneShort = posUSDT_04Sandra['result'][x]['data']["side"] == "Sell" and posUSDT_04Sandra['result'][x]['data']["entry_price"] != 0
   if oneShort:
       nbShort_04Sandra += 1



######################################################################################################################################################################

###################################################################################################################################################################### FIN CONFIG

###################################################################################################################################################################### 

############################################################################################################ PRICE

client = bybit.bybit(test=False, api_key=st.secrets["aK00TFio"], api_secret=st.secrets["aS00TFio"])
info = client.Market.Market_symbolInfo().result()
keys = info[0]['result']
btc = keys[50]['last_price']
name = keys[50]['symbol']

############################################################################################################


###################################################################################################################################################################### 
###################################################################################################################################################################### My FIRST DASH
###################################################################################################################################################################### 



########################### First Line

col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)

for i in range(10):
    if i == 0:
        with col1:
            st.info("₿: "+ btc)
            st.info('💁🏾‍♀️'' 00TFio')
            st.info("💰"' : ' + str(round((EQUITY_00TFio)/float(btc), 4)) + ' BTC')
    if i == 1:
        with col2:
            st.info("💰 Equity 💰")
            st.info("💰"' : ' + str(round(EQUITY_00TFio,2)))
            st.info("💰"' : ' + str(round(EQUITY_00TFio,2)))
    if i == 2:
        with col3:
            st.info("⬇️ Deposit ⬇️")
            st.info("⬇️"' : ' + str(round(DEPOSIT_00TFio,2)))
            st.info("⬇️"' : ' + str(round(DEPOSIT_00TFio,1)))
    if i == 3:
        with col4:
            st.info("💸 Bénéfice 💸")
            st.info("💸"' : ' + str(round(TAXABLE_00TFio,2)))
            st.info("💸"' : ' + str(round(TAXABLE_00TFio+2410,2)))
    if i == 4:
        with col5:
            st.info("💸 Realized 💸")
            st.info("💸"' : ' + str(round(PERF_00TFio,2)))
            st.info("💸"' : ' + str(round(PERF_00TFio+2410,2)))
    if i == 5:
        with col6:
            st.info("💸 Unrealized 💸")
            st.info("💸"' : ' + str(round(NRZ_00TFio,2)))
            st.info("💸"' : ' + str(round(NRZ_00TFio,2)))
    if i == 6:
        with col7:
            st.info("💀 In Play 💀")
            st.info("💀"' : ' + str(round(INPLAY_00TFio*100,2)) +'%')
            st.info("💀"' : ' + str(round((EQUITY_00TFio - AVAILABLE_00TFio) * 100 / (EQUITY_00TFio), 2)) + '%')
#    if i == 7:
#        with col8:
#            st.info("🫶 L/S 🫶")
#            if nbTrade_00TFio == 0:
#                st.info("🫶"' : No Trade')
#            else:
#                st.info("🫶"' : ' + str(nbLong_00TFio) + ' / ' + str(nbShort_00TFio) + ' (' + str(round((nbLong_00TFio/nbTrade_00TFio)*100)) + '/' + str(round((nbShort_00TFio/nbTrade_00TFio)*100)) + '%)')
#           st.info("🫶 Long/Short 🫶")
#    if i == 8:
#        with col9:
#            st.info("#️⃣ Nb. T #️⃣")
#            st.info("#️⃣"' : ' + str(nbTrade_00TFio))
#            st.info("#️⃣"' : ' + str(nbTrade_00TFio))
    if i == 7:
        with col8:
            st.info('〽️ Perf. 〽️')
            st.info('〽️'' : ' + str(round(PNL100_00TFio,3)) +'%')
            st.info('〽️'' : ' + str(round((PNL100_00TFio * DEPOSIT_00TFio) / (DEPOSIT_00TFio), 2)) + '%')
    if i == 8:
        with col9:
            st.info('✂️ HWM ✂️')
            st.info('✂️'' : ' + str(round(HWM_00TFio)))
            st.info('✂️'' : ' + str(round(HWM_00TFio)))
    if i == 9:
        with col10:
            st.info('✂️ Com. ✂️')
            st.info('✂️'' : ' + str(round(COMMISSION_00TFio-HWM_00TFio,2)))
            st.info('✂️'' : ' + str(round(COMMISSION_00TFio - HWM_00TFio, 2)))
#    if i == 12:
#        with col13:
#            st.info('✂️ Retro C. ✂️')
#            if RETRO_00TFio == 0 or COMMISSION_00TFio-HWM_00TFio <= 0:
#                st.info("🫶"' : N/A')
#            else:
#                st.info('✂️'' : ' + str(round((COMMISSION_00TFio-HWM_00TFio)*RETRO_00TFio,2)))
#            st.info('✂️'' : ' + str(round((COMMISSION_00TFio - HWM_00TFio) * RETRO_00TFio,2)))




######################################################################################################################################################################

######################################################################################################################################################################


st.markdown('''# **Clients**''')


######################################################################################################################################################################


######################################################################################################################################################################


col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)

for i in range(10):
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
            st.info('〽️ Perf. 〽️')
    if i == 8:
        with col9:
            st.info('✂️ HWM ✂️')
    if i == 9:
        with col10:
            st.info('✂️ Com. ✂️')

            

####----------------------
####---------------------- 01Vitor
####----------------------


col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)

for i in range(10):
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
            st.info('〽️'' : ' + str(round(PNL100_01Vitor,3)) +'%')
    if i == 8:
        with col9:
            st.info('✂️'' : ' + str(round(HWM_01Vitor)))
    if i == 9:
        with col10:
            st.info('✂️'' : ' + str(round(COMMISSION_01Vitor-HWM_01Vitor,2)))


####----------------------
####---------------------- 02Joao
####----------------------

col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)

for i in range(10):
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
            st.info('〽️'' : ' + str(round(PNL100_02Joao,3)) +'%')
    if i == 8:
        with col9:
            st.info('✂️'' : ' + str(round(HWM_02Joao)))
    if i == 9:
        with col10:
            st.info('✂️'' : ' + str(round(COMMISSION_02Joao-HWM_02Joao,2)))

####----------------------
####---------------------- 03Rayan
####----------------------

col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)

for i in range(10):
    if i == 0:
        with col1:
            st.info('💁🏾‍♀️'' 03Rayan')
    if i == 1:
        with col2:
            st.info("💰"' : ' + str(round(EQUITY_03Rayan,2)))
    if i == 2:
        with col3:
            st.info("⬇️"' : ' + str(round(DEPOSIT_03Rayan,2)))
    if i == 3:
        with col4:
            st.info("💸"' : ' + str(round(TAXABLE_03Rayan,2)))
    if i == 4:
        with col5:
            st.info("💸"' : ' + str(round(PERF_03Rayan,2)))
    if i == 5:
        with col6:
            st.info("💸"' : ' + str(round(NRZ_03Rayan,2)))
    if i == 6:
        with col7:
            st.info("💀"' : ' + str(round(INPLAY_03Rayan*100,2)) +'%')
    if i == 7:
        with col8:
            st.info('〽️'' : ' + str(round(PNL100_03Rayan,3)) +'%')
    if i == 8:
        with col9:
            st.info('✂️'' : ' + str(round(HWM_03Rayan)))
    if i == 9:
        with col10:
            st.info('✂️'' : ' + str(round(COMMISSION_03Rayan-HWM_03Rayan,2)))


####----------------------
####---------------------- 04Sandra
####----------------------

col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)

for i in range(10):
    if i == 0:
        with col1:
            st.info('💁🏾‍♀️'' 04Sandra')
    if i == 1:
        with col2:
            st.info("💰"' : ' + str(round(EQUITY_04Sandra,2)))
    if i == 2:
        with col3:
            st.info("⬇️"' : ' + str(round(DEPOSIT_04Sandra,2)))
    if i == 3:
        with col4:
            st.info("💸"' : ' + str(round(TAXABLE_04Sandra,2)))
    if i == 4:
        with col5:
            st.info("💸"' : ' + str(round(PERF_04Sandra,2)))
    if i == 5:
        with col6:
            st.info("💸"' : ' + str(round(NRZ_04Sandra,2)))
    if i == 6:
        with col7:
            st.info("💀"' : ' + str(round(INPLAY_04Sandra*100,2)) +'%')
    if i == 7:
        with col8:
            st.info('〽️'' : ' + str(round(PNL100_04Sandra,3)) +'%')
    if i == 8:
        with col9:
            st.info('✂️'' : ' + str(round(HWM_04Sandra)))
    if i == 9:
        with col10:
            st.info('✂️'' : ' + str(round(COMMISSION_04Sandra-HWM_04Sandra,2)))



####----------------------
####----------------------
####----------------------               
####----------------------
####---------------------- Total
####----------------------
####----------------------
####----------------------
####----------------------



col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)

for i in range(10):
    if i == 0:
        with col1:
            st.info('Total')
    if i == 1:
        with col2:
            st.info("💰"' : ' + str(round(EQUITY_01Vitor+EQUITY_02Joao+EQUITY_03Rayan+EQUITY_04Sandra, 2)))
    if i == 2:
        with col3:
            st.info("⬇️"' : ' + str(round(DEPOSIT_01Vitor+DEPOSIT_02Joao+DEPOSIT_03Rayan+DEPOSIT_04Sandra,2)))
    if i == 3:
        with col4:
            st.info("💸"' : ' + str(round(TAXABLE_01Vitor+TAXABLE_02Joao+TAXABLE_03Rayan+TAXABLE_04Sandra, 2)))
    if i == 4:
        with col5:
            st.info("💸"' : ' + str(round(PERF_01Vitor+PERF_02Joao+PERF_03Rayan+PERF_04Sandra, 2)))
    if i == 5:
        with col6:
            st.info("💸"' : ' + str(round(NRZ_01Vitor+NRZ_02Joao+NRZ_03Rayan+NRZ_04Sandra, 2)))
    if i == 6:
        with col7:
            st.info("💀 In Play 💀")
#    if i == 7:
#        with col8:
#            st.info("🫶 Long/Short 🫶")
#    if i == 8:
#        with col9:
#            st.info("#️⃣ Nb. T #️⃣")
    if i == 7:
        with col8:
            st.info('〽️ Perf. 〽️')
    if i == 8:
        with col9:
            st.info('✂️ HWM ✂️')
    if i == 9:
        with col10:
            st.info('✂️ Com. ✂️')
#    if i == 12:
#        with col13:
#            st.info('✂️ Retro C. ✂️')




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

col0_01, col1_01, col2_01 , col3_01, col4_01, col5_01, col6_01, col7_01, col8_01, col9_01 = st.columns(10)

for i in range(10):
    if i == 0:
        with col0_01:
            st.info("All Account")
            st.info("00TFio")
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
####---------------------- 01Vitor
####----------------------

col0_01, col1_01, col2_01 , col3_01, col4_01, col5_01, col6_01, col7_01, col8_01, col9_01 = st.columns(10)

for i in range(10):
    if i == 0:
        with col0_01:
            st.info("01Vitor")
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

col0_01, col1_01, col2_01 , col3_01, col4_01, col5_01, col6_01, col7_01, col8_01, col9_01 = st.columns(10)

for i in range(10):
    if i == 0:
        with col0_01:
            st.info("02Joao")
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

  

####----------------------
####---------------------- 03Rayan
####----------------------

col0_01, col1_01, col2_01 , col3_01, col4_01, col5_01, col6_01, col7_01, col8_01, col9_01 = st.columns(10)

for i in range(10):
    if i == 0:
        with col0_01:
            st.info("03Rayan")
    if i == 1:
        with col1_01:
            for x in a_03Rayan:
                oneTrade = posUSDT_03Rayan['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_03Rayan['result'][x]['data']['symbol']))
    if i == 2:
        with col2_01:
            for x in a_03Rayan:
                oneTrade = posUSDT_03Rayan['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_03Rayan['result'][x]['data']['side']))
    if i == 3:
        with col3_01:
            for x in a_03Rayan:
                oneTrade = posUSDT_03Rayan['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_03Rayan['result'][x]['data']['size']))
    if i == 4:
        with col4_01:
            for x in a_03Rayan:
                oneTrade = posUSDT_03Rayan['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    if posUSDT_03Rayan['result'][x]['data']['unrealised_pnl'] >= 0:
                        st.success(str(round(posUSDT_03Rayan['result'][x]['data']['unrealised_pnl'],2)))
                    else:
                        st.error(str(round(posUSDT_03Rayan['result'][x]['data']['unrealised_pnl'],2)))
    if i == 5:
        with col5_01:
            for x in a_03Rayan:
                oneTrade = posUSDT_03Rayan['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    if posUSDT_03Rayan['result'][x]['data']['unrealised_pnl'] >= 0:
                        st.success(str(round((posUSDT_03Rayan['result'][x]['data']['unrealised_pnl']/(posUSDT_03Rayan['result'][x]['data']['entry_price']*posUSDT_03Rayan['result'][x]['data']['size']))*100,2))+ '%')
                    else:
                        st.error(str(round((posUSDT_03Rayan['result'][x]['data']['unrealised_pnl']/(posUSDT_03Rayan['result'][x]['data']['entry_price']*posUSDT_03Rayan['result'][x]['data']['size']))*100,2))+ '%')
    if i == 6:
        with col6_01:
            for x in a_03Rayan:
                oneTrade = posUSDT_03Rayan['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_03Rayan['result'][x]['data']['cum_realised_pnl']))
    if i == 7:
        with col7_01:
            for x in a_03Rayan:
                oneTrade = posUSDT_03Rayan['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_03Rayan['result'][x]['data']['entry_price']))
    if i == 8:
        with col8_01:
            for x in a_03Rayan:
                oneTrade = posUSDT_03Rayan['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(round(posUSDT_03Rayan['result'][x]['data']['entry_price']*posUSDT_03Rayan['result'][x]['data']['size'],2)))



####----------------------
####---------------------- 04Sandra
####----------------------

col0_01, col1_01, col2_01 , col3_01, col4_01, col5_01, col6_01, col7_01, col8_01, col9_01 = st.columns(10)

for i in range(10):
    if i == 0:
        with col0_01:
            st.info("04Sandra")
    if i == 1:
        with col1_01:
            for x in a_04Sandra:
                oneTrade = posUSDT_04Sandra['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_04Sandra['result'][x]['data']['symbol']))
    if i == 2:
        with col2_01:
            for x in a_04Sandra:
                oneTrade = posUSDT_04Sandra['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_04Sandra['result'][x]['data']['side']))
    if i == 3:
        with col3_01:
            for x in a_04Sandra:
                oneTrade = posUSDT_04Sandra['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_04Sandra['result'][x]['data']['size']))
    if i == 4:
        with col4_01:
            for x in a_04Sandra:
                oneTrade = posUSDT_04Sandra['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    if posUSDT_04Sandra['result'][x]['data']['unrealised_pnl'] >= 0:
                        st.success(str(round(posUSDT_04Sandra['result'][x]['data']['unrealised_pnl'],2)))
                    else:
                        st.error(str(round(posUSDT_04Sandra['result'][x]['data']['unrealised_pnl'],2)))
    if i == 5:
        with col5_01:
            for x in a_04Sandra:
                oneTrade = posUSDT_04Sandra['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    if posUSDT_04Sandra['result'][x]['data']['unrealised_pnl'] >= 0:
                        st.success(str(round((posUSDT_04Sandra['result'][x]['data']['unrealised_pnl']/(posUSDT_04Sandra['result'][x]['data']['entry_price']*posUSDT_04Sandra['result'][x]['data']['size']))*100,2))+ '%')
                    else:
                        st.error(str(round((posUSDT_04Sandra['result'][x]['data']['unrealised_pnl']/(posUSDT_04Sandra['result'][x]['data']['entry_price']*posUSDT_04Sandra['result'][x]['data']['size']))*100,2))+ '%')
    if i == 6:
        with col6_01:
            for x in a_04Sandra:
                oneTrade = posUSDT_04Sandra['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_04Sandra['result'][x]['data']['cum_realised_pnl']))
    if i == 7:
        with col7_01:
            for x in a_04Sandra:
                oneTrade = posUSDT_04Sandra['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_04Sandra['result'][x]['data']['entry_price']))
    if i == 8:
        with col8_01:
            for x in a_04Sandra:
                oneTrade = posUSDT_04Sandra['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(round(posUSDT_04Sandra['result'][x]['data']['entry_price']*posUSDT_04Sandra['result'][x]['data']['size'],2)))


                    
                    
############################################################################################################ ONE-WAY

# print("Change A !")
# st.header("Change A  !")
#
# for x in a:
#     try:
#         ii_00 = str(posUSDT_00TFio['result'][x]['data']['symbol'])
#         print(session_auth_00TFio.position_mode_switch(symbol=(ii_00), mode="MergedSingle"))
#         print(posUSDT_00TFio['result'][x]['data']['symbol'])
#         ii_01 = str(posUSDT_00TFio['result'][x]['data']['symbol'])
#         print(session_auth_00TFio.position_mode_switch(symbol=(ii_01), mode="MergedSingle"))
#         print(posUSDT_00TFio['result'][x]['data']['symbol'])
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

for x in a_00TFio:
    try:
        ii = str(posUSDT_00TFio['result'][x]['data']['symbol'])
        authPNL_00TFio = session_auth_00TFio.closed_profit_and_loss(symbol=(ii))
        for i in range(0,len(authPNL_00TFio)):
            #print(authPNL_00["result"]["data"][i]["created_at"])
            if authPNL_00TFio["result"]["data"][i]["created_at"] > UnixY:
                #print("Id: " + str(authPNL_00TFio["result"]["data"][i]["id"]) + " Time: " + str(authPNL_00TFio["result"]["data"][i]["created_at"]) + " Symbole: " + str(authPNL_00TFio["result"]["data"][i]["symbol"]) + " Side: " + str(authPNL_00TFio["result"]["data"][i]["side"]) + " Entry Price: " + str(authPNL_00TFio["result"]["data"][i]["avg_entry_price"]) + " Exit Price: " + str(authPNL_00TFio["result"]["data"][i]["avg_exit_price"]) + " PNL: " + str(authPNL_00TFio["result"]["data"][i]["closed_pnl"]) + " $IN$: " + str(authPNL_00TFio["result"]["data"][i]["cum_entry_value"]) + " $OUT$: " + str(authPNL_00TFio["result"]["data"][i]["cum_exit_value"]))
                #st.subheader(str(("Id: " + str(authPNL_00TFio["result"]["data"][i]["id"]) + " Time: " + str(authPNL_00TFio["result"]["data"][i]["created_at"]) + " Symbole: " + str(authPNL_00TFio["result"]["data"][i]["symbol"]) + " Side: " + str(authPNL_00TFio["result"]["data"][i]["side"]) + " Entry Price: " + str(authPNL_00TFio["result"]["data"][i]["avg_entry_price"]) + " Exit Price: " + str(authPNL_00TFio["result"]["data"][i]["avg_exit_price"]) + " PNL: " + str(authPNL_00TFio["result"]["data"][i]["closed_pnl"]) + " $IN$: " + str(authPNL_00TFio["result"]["data"][i]["cum_entry_value"]) + " $OUT$: " + str(authPNL_00TFio["result"]["data"][i]["cum_exit_value"]))))
                if str(authPNL_00TFio["result"]["data"][i]["side"]) == "Buy":
                    print(str(datetime.fromtimestamp(authPNL_00TFio["result"]["data"][i]["created_at"])) + " Symbol: " + str(authPNL_00TFio["result"]["data"][i]["symbol"]) + " Short: " + str(round((((authPNL_00TFio["result"]["data"][i]["avg_exit_price"] / authPNL_00TFio["result"]["data"][i]["avg_entry_price"] - 1) * -100)),2)) + "%")
                    st.subheader(str(datetime.fromtimestamp(authPNL_00TFio["result"]["data"][i]["created_at"]+7200)) + " Symbol: " + str(authPNL_00TFio["result"]["data"][i]["symbol"]) + " Short: " + str(round((((authPNL_00TFio["result"]["data"][i]["avg_exit_price"] / authPNL_00TFio["result"]["data"][i]["avg_entry_price"] - 1) * -100)), 2)) + "%")
                elif str(authPNL_00TFio["result"]["data"][i]["side"]) == "Sell":
                    print(str(datetime.fromtimestamp(authPNL_00TFio["result"]["data"][i]["created_at"])) + " Symbol: " + str(authPNL_00TFio["result"]["data"][i]["symbol"]) + " Long: " + str(round((((authPNL_00TFio["result"]["data"][i]["avg_exit_price"] / authPNL_00TFio["result"]["data"][i]["avg_entry_price"] - 1) * 100)),2)) + "%")
                    st.subheader(str(datetime.fromtimestamp(authPNL_00TFio["result"]["data"][i]["created_at"]+7200)) + " Symbol: " + str(authPNL_00TFio["result"]["data"][i]["symbol"]) + " Long: " + str(round((((authPNL_00TFio["result"]["data"][i]["avg_exit_price"] / authPNL_00TFio["result"]["data"][i]["avg_entry_price"] - 1) * 100)), 2)) + "%")
                else:
                    print("N/A")
                    st.subheader("N/A")
    except:
        pass




print("Done !")
st.header("Done !")
