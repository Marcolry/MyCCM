import streamlit as st
import time
st.set_page_config(layout="wide")
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


c00Feli = np.array(['00Feli', st.secrets["aK00Feli"], st.secrets["aS00Feli"], 0.3, 1/3, 0])
c00Marc = np.array(['00Marc', st.secrets["aK00Marc"], st.secrets["aS00Marc"], 0.3, 0, 0])

#c00Feli = np.array(['00Feli', config.aK00Feli, config.aS00Feli, 0.3, 1/3, 0])
#c00Marc = np.array(['00Marc', config.aK00Marc, config.aS00Marc, 0.3, 0, 0])

#c00Feli = np.array(['00Feli', 'JZ24WpMKpp9rwlFKVZ', 'AHlS383YuQYNo1YGeY1S5c8e4DyIEu93rhUT', 0.3, 1/3, 0])
#c00Marc = np.array(['00Marc', "UF0dKfVrCZuzv03TPy", "gzzHsA7oulat7i0qzq5zNbOfAwvQyTLBC8Pf", 0.3, 0, 0])

allUsers = np.array([c00Feli, c00Marc])


session_auth_00Feli = usdt_perpetual.HTTP(endpoint="https://api.bybit.com",api_key=st.secrets["aK00Feli"],api_secret=st.secrets["aS00Feli"])
session_auth_00Marc = usdt_perpetual.HTTP(endpoint="https://api.bybit.com",api_key=st.secrets["aK00Marc"],api_secret=st.secrets["aS00Marc"])

#session_auth_00Feli = usdt_perpetual.HTTP(endpoint="https://api.bybit.com",api_key=allUsers[0][1],api_secret=allUsers[0][2])
#session_auth_00Marc = usdt_perpetual.HTTP(endpoint="https://api.bybit.com",api_key=allUsers[1][1],api_secret=allUsers[1][2])

#session_auth_00Feli = usdt_perpetual.HTTP(endpoint="https://api.bybit.com",api_key='JZ24WpMKpp9rwlFKVZ',api_secret='AHlS383YuQYNo1YGeY1S5c8e4DyIEu93rhUT')
#session_auth_00Marc = usdt_perpetual.HTTP(endpoint="https://api.bybit.com",api_key="UF0dKfVrCZuzv03TPy",api_secret="gzzHsA7oulat7i0qzq5zNbOfAwvQyTLBC8Pf")

authUSDT_00Feli = session_auth_00Feli.get_wallet_balance()
authUSDT_00Marc = session_auth_00Marc.get_wallet_balance()

posUSDT_00Feli = session_auth_00Feli.my_position()
posUSDT_00Marc = session_auth_00Marc.my_position()



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
# #print(c00Feli[0])
# #print(c00Feli[1])
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



RATELIMIT_00 = authUSDT_00Feli['rate_limit']
STATELIMIT_00 = authUSDT_00Feli['rate_limit_status']
RESETLIMIT_00 = authUSDT_00Feli['rate_limit_reset_ms']
print(str(STATELIMIT_00) + '------------------------------------------------------------------------------->')
##-----------------------------------------------------------------------> 00 - Marc
RATELIMIT_01 = authUSDT_00Marc['rate_limit']
STATELIMIT_01 = authUSDT_00Marc['rate_limit_status']
RESETLIMIT_01 = authUSDT_00Marc['rate_limit_reset_ms']
print(str(STATELIMIT_01) + '------------------------------------------------------------------------------->')


###################################################################################################################################################################### API


#print(len(posUSDT_00Feli['result']))
#print(len(posUSDT_00Marc['result']))

ALL = list(range(0, len(posUSDT_00Marc['result']))) #print(ALL)
a = arr.array('i', ALL)

##-----------------------------------------------------------------------> API LIMIT

st.write('**Request Limit:** ' + str(STATELIMIT_00) + '/' + str(RATELIMIT_00) + ' & ' + str(STATELIMIT_01) + '/' + str(RATELIMIT_01))


###################################################################################################################################################################### CONFIG Feli


EQUITY_00 = authUSDT_00Feli['result']['USDT']['equity']
NRZ_00 = authUSDT_00Feli['result']['USDT']['unrealised_pnl']
PERF_00 = authUSDT_00Feli['result']['USDT']['cum_realised_pnl']

AVAILABLE_00 = authUSDT_00Feli['result']['USDT']['available_balance']
INPLAY_00 = (EQUITY_00 - AVAILABLE_00)/EQUITY_00


DEPOSIT_00 = EQUITY_00 - NRZ_00 - PERF_00
PNL100_00 = (round(EQUITY_00/DEPOSIT_00,4)-1)*100

TAXABLE_00 = NRZ_00 + PERF_00
#print('TO TAX: ' + str(TAXABLE_00))

if TAXABLE_00 > 0:
    COMMISSION_00 = TAXABLE_00 * float(allUsers[0][3])
if TAXABLE_00 < 0:
    COMMISSION_00 = 0


##-----------------------------------------------------------------------> Nb

nbTrade_00 = 0
nbLong_00 = 0
nbShort_00 = 0

for x in a:
   oneTrade = posUSDT_00Feli['result'][x]['data']["entry_price"] != 0
   if oneTrade:
       nbTrade_00 += 1

for x in a:
   oneLong = posUSDT_00Feli['result'][x]['data']["side"] == "Buy"
   if oneLong:
       nbLong_00 += 1

for x in a:
   oneShort = posUSDT_00Feli['result'][x]['data']["side"] == "Sell"
   if oneShort:
       nbShort_00 += 1


###################################################################################################################################################################### CONFIG Marc


EQUITY_01 = authUSDT_00Marc['result']['USDT']['equity']
NRZ_01 = authUSDT_00Marc['result']['USDT']['unrealised_pnl']
PERF_01 = authUSDT_00Marc['result']['USDT']['cum_realised_pnl']

AVAILABLE_01 = authUSDT_00Marc['result']['USDT']['available_balance']
INPLAY_01 = (EQUITY_01 - AVAILABLE_01)/EQUITY_01


DEPOSIT_01 = EQUITY_01 - NRZ_01 - PERF_01
PNL100_01 = (round(EQUITY_01/DEPOSIT_01,4)-1)*100

TAXABLE_01 = NRZ_01 + PERF_01
#print('TO TAX: ' + str(TAXABLE_01))

if TAXABLE_01 > 0:
    COMMISSION_01 = TAXABLE_01 * float(allUsers[1][3])
if TAXABLE_01 < 0:
    COMMISSION_01 = 0

##-----------------------------------------------------------------------> NB

nbTrade_01 = 0
nbLong_01 = 0
nbShort_01 = 0

for x in a:
    oneTrade = posUSDT_00Marc['result'][x]['data']["entry_price"] != 0
    if oneTrade:
        nbTrade_01 += 1

for x in a:
    oneLong = posUSDT_00Marc['result'][x]['data']["side"] == "Buy"
    if oneLong:
        nbLong_01 += 1

for x in a:
    oneShort = posUSDT_00Marc['result'][x]['data']["side"] == "Sell"
    if oneShort:
        nbShort_01 += 1







###################################################################################################################################################################### DASHBOARD








########################### First Line

col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13 = st.columns(13)

for i in range(13):
    if i == 0:
        with col1:
            st.info(' 📘 ')
            st.info('💁🏾‍♀️'' 00Feli')
            st.info('👨🏽‍🎓'' 00Marc')
            st.info('Total')
    if i == 1:
        with col2:
            st.info("💰 Equity 💰")
            st.info("💰"' : ' + str(round(EQUITY_00,2)))
            st.info("💰"' : ' + str(round(EQUITY_01,2)))
            st.info("💰"' : ' + str(round(EQUITY_00 + EQUITY_01, 2)))
    if i == 2:
        with col3:
            st.info("⬇️ Deposit ⬇️")
            st.info("⬇️"' : ' + str(round(DEPOSIT_00,2)))
            st.info("⬇️"' : ' + str(round(DEPOSIT_01,2)))
            st.info("⬇️"' : ' + str(round(DEPOSIT_00+DEPOSIT_01,2)))
    if i == 3:
        with col4:
            st.info("💸 Bénéfice 💸")
            st.info("💸"' : ' + str(round(TAXABLE_00,2)))
            st.info("💸"' : ' + str(round(TAXABLE_01,2)))
            st.info("💸"' : ' + str(round(TAXABLE_00+TAXABLE_01,2)))
    if i == 4:
        with col5:
            st.info("💸 Realized 💸")
            st.info("💸"' : ' + str(round(PERF_00,2)))
            st.info("💸"' : ' + str(round(PERF_01,2)))
            st.info("💸"' : ' + str(round(PERF_00+PERF_01,2)))
    if i == 5:
        with col6:
            st.info("💸 Unrealized 💸")
            st.info("💸"' : ' + str(round(NRZ_00,2)))
            st.info("💸"' : ' + str(round(NRZ_01,2)))
            st.info("💸"' : ' + str(round(NRZ_00+NRZ_01,2)))

    if i == 6:
        with col7:
            st.info("💀 In Play 💀")
            st.info("💀"' : ' + str(round(INPLAY_00*100,2)) +'%')
            st.info("💀"' : ' + str(round(INPLAY_01*100,2)) +'%')
            st.info("💀"' : ' + str(round((EQUITY_00+EQUITY_01-AVAILABLE_00-AVAILABLE_01)*100/(EQUITY_00+EQUITY_01),2))+'%')
    if i == 7:
        with col8:
            st.info("🫶 L/S 🫶")
            if nbTrade_00 == 0:
                st.info("🫶"' : No Trade')
            else:
                st.info("🫶"' : ' + str(nbLong_00) + ' / ' + str(nbShort_00) + ' (' + str(round((nbLong_00/nbTrade_00)*100)) + '/' + str(round((nbShort_00/nbTrade_00)*100)) + '%)')
            if nbTrade_01 == 0:
                st.info("🫶"' : No Trade')
            else:
                st.info("🫶"' : ' + str(nbLong_01) + ' / ' + str(nbShort_01) + ' (' + str(round((nbLong_01/nbTrade_01)*100)) + '/' + str(round((nbShort_01/nbTrade_01)*100)) + '%)')
            st.info("🫶 Long/Short 🫶")
    if i == 8:
        with col9:
            st.info("#️⃣ Nb. T #️⃣")
            st.info("#️⃣"' : ' + str(nbTrade_00))
            st.info("#️⃣"' : ' + str(nbTrade_01))
            st.info("#️⃣"' : ' + str(nbTrade_00+nbTrade_01))
    if i == 9:
        with col10:
            st.info('〽️ Perf. 〽️')
            st.info('〽️'' : ' + str(round(PNL100_00,3)) +'%')
            st.info('〽️'' : ' + str(round(PNL100_01,3)) +'%')
            st.info('〽️'' : ' + str(round((PNL100_00 * DEPOSIT_00 + PNL100_01 * DEPOSIT_01) / (DEPOSIT_00 + DEPOSIT_01), 2)) + '%')
    if i == 10:
        with col11:
            st.info('✂️ HWM ✂️')
            st.info('✂️'' : ' + str(round(float(allUsers[0][5]),2)))
            st.info('✂️'' : ' + str(round(float(allUsers[1][5]),2)))
            st.info('✂️'' : ' + str(round(float(allUsers[0][5]) + float(allUsers[1][5]), 2)))
    if i == 11:
        with col12:
            st.info('✂️ Com. ✂️')
            st.info('✂️'' : ' + str(round(COMMISSION_00-float(allUsers[0][5]),2)))
            st.info('✂️'' : ' + str(round(COMMISSION_01-float(allUsers[1][5]),2)))
            st.info('✂️'' : ' + str(round(COMMISSION_00 + COMMISSION_01, 2)))
    if i == 12:
        with col13:
            st.info('✂️ Retro C. ✂️')
            if allUsers[0][4] == 0:
                st.info("🫶"' : N/A')
            else:
                st.info('✂️'' : ' + str(round((COMMISSION_00-float(allUsers[0][5]))*float(allUsers[0][4]),2)))
            if allUsers[1][4] == 0:
                st.info("🫶"' : N/A')
            else:
                st.info('✂️'' : ' + str(round((COMMISSION_01-float(allUsers[1][5]))*float(allUsers[1][4]),2)))
            st.info('✂️'' : ' + str(round((COMMISSION_00 - float(allUsers[0][5])) * float(allUsers[0][4]) + (COMMISSION_01 - float(allUsers[1][5])) * float(allUsers[1][4]), 2)))






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
                oneTrade = posUSDT_00Feli['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00Feli['result'][x]['data']['symbol']))
    if i == 2:
        with col2_01:
            st.info("Side")
            for x in a:
                oneTrade = posUSDT_00Feli['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00Feli['result'][x]['data']['side']))
    if i == 3:
        with col3_01:
            st.info("Size")
            for x in a:
                oneTrade = posUSDT_00Feli['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00Feli['result'][x]['data']['size']))
    if i == 4:
        with col4_01:
            st.info("Unrealised PNL")
            for x in a:
                oneTrade = posUSDT_00Feli['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    if posUSDT_00Feli['result'][x]['data']['unrealised_pnl'] >= 0:
                        st.success(str(round(posUSDT_00Feli['result'][x]['data']['unrealised_pnl'],2)))
                    else:
                        st.error(str(round(posUSDT_00Feli['result'][x]['data']['unrealised_pnl'],2)))
    if i == 5:
        with col5_01:
            st.info("Unrealised %")
            for x in a:
                oneTrade = posUSDT_00Feli['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    if posUSDT_00Feli['result'][x]['data']['unrealised_pnl'] >= 0:
                        st.success(str(round((posUSDT_00Feli['result'][x]['data']['unrealised_pnl']/(posUSDT_00Feli['result'][x]['data']['entry_price']*posUSDT_00Feli['result'][x]['data']['size']))*100,2))+ '%')
                    else:
                        st.error(str(round((posUSDT_00Feli['result'][x]['data']['unrealised_pnl']/(posUSDT_00Feli['result'][x]['data']['entry_price']*posUSDT_00Feli['result'][x]['data']['size']))*100,2))+ '%')
    if i == 6:
        with col6_01:
            st.info("Realized PNL")
            for x in a:
                oneTrade = posUSDT_00Feli['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00Feli['result'][x]['data']['cum_realised_pnl']))
    if i == 7:
        with col7_01:
            st.info("Entry Price")
            for x in a:
                oneTrade = posUSDT_00Feli['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00Feli['result'][x]['data']['entry_price']))
    if i == 8:
        with col8_01:
            st.info("Total Size")
            for x in a:
                oneTrade = posUSDT_00Feli['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(round(posUSDT_00Feli['result'][x]['data']['entry_price']*posUSDT_00Feli['result'][x]['data']['size'],2)))


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
                oneTrade = posUSDT_00Marc['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00Marc['result'][x]['data']['symbol']))
    if i == 2:
        with col2_01:
            for x in a:
                oneTrade = posUSDT_00Marc['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00Marc['result'][x]['data']['side']))
    if i == 3:
        with col3_01:
            for x in a:
                oneTrade = posUSDT_00Marc['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00Marc['result'][x]['data']['size']))
    if i == 4:
        with col4_01:
            for x in a:
                oneTrade = posUSDT_00Marc['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    if posUSDT_00Marc['result'][x]['data']['unrealised_pnl'] >= 0:
                        st.success(str(round(posUSDT_00Marc['result'][x]['data']['unrealised_pnl'],2)))
                    else:
                        st.error(str(round(posUSDT_00Marc['result'][x]['data']['unrealised_pnl'],2)))
    if i == 5:
        with col5_01:
            for x in a:
                oneTrade = posUSDT_00Marc['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    if posUSDT_00Marc['result'][x]['data']['unrealised_pnl'] >= 0:
                        st.success(str(round((posUSDT_00Marc['result'][x]['data']['unrealised_pnl']/(posUSDT_00Marc['result'][x]['data']['entry_price']*posUSDT_00Marc['result'][x]['data']['size']))*100,2))+ '%')
                    else:
                        st.error(str(round((posUSDT_00Marc['result'][x]['data']['unrealised_pnl']/(posUSDT_00Marc['result'][x]['data']['entry_price']*posUSDT_00Marc['result'][x]['data']['size']))*100,2))+ '%')
    if i == 6:
        with col6_01:
            for x in a:
                oneTrade = posUSDT_00Marc['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00Marc['result'][x]['data']['cum_realised_pnl']))
    if i == 7:
        with col7_01:
            for x in a:
                oneTrade = posUSDT_00Marc['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(posUSDT_00Marc['result'][x]['data']['entry_price']))
    if i == 8:
        with col8_01:
            for x in a:
                oneTrade = posUSDT_00Marc['result'][x]['data']["entry_price"] != 0
                if oneTrade:
                    st.info(str(round(posUSDT_00Marc['result'][x]['data']['entry_price']*posUSDT_00Marc['result'][x]['data']['size'],2)))


############################################################################################################ ONE-WAY

# print("Change A !")
# st.header("Change A  !")
#
# for x in a:
#     try:
#         ii_00 = str(posUSDT_00Feli['result'][x]['data']['symbol'])
#         print(session_auth_00Feli.position_mode_switch(symbol=(ii_00), mode="MergedSingle"))
#         print(posUSDT_00Feli['result'][x]['data']['symbol'])
#         ii_01 = str(posUSDT_00Marc['result'][x]['data']['symbol'])
#         print(session_auth_00Marc.position_mode_switch(symbol=(ii_01), mode="MergedSingle"))
#         print(posUSDT_00Marc['result'][x]['data']['symbol'])
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
        ii = str(posUSDT_00Marc['result'][x]['data']['symbol'])
        authPNL_01 = session_auth_00Marc.closed_profit_and_loss(symbol=(ii))
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

