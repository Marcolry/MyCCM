import streamlit as st
import websocket
st.set_page_config(layout="wide")
import pandas as pd
import config
import bybit
from pybit import usdt_perpetual
import array as arr
ALL = list(range(0, 349)) #print(ALL)
a = arr.array('i', ALL)
TX = 0.3


df = pd.read_json('https://api.bybit.com/v2/public/tickers')['result']
# print(df['last_price'])

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
posUSDT_00 = session_auth_00.my_position()

################################################LIMIT

RATELIMIT_00 = authUSDT_00['rate_limit']
STATELIMIT_00 = authUSDT_00['rate_limit_status']
RESETLIMIT_00 = authUSDT_00['rate_limit_reset_ms']
print(str(STATELIMIT_00) + '------------------------------------------------------------------------------->')

############################################################################################# IP
import socket
#hostname = socket.gethostname()
#local_ip = socket.gethostbyname(hostname)
#print('My local IP is: ' + local_ip)
from requests import get
ip = get('https://api.ipify.org').text
#print(f'My public IP is: {ip}')
#st.write('**Local IP:** ' + str(local_ip) + ' // **Public IP:** ' + str(ip))
#st.write('**Request Limit:** ' + str(STATELIMIT_00) + '/' + str(RATELIMIT_00))
#st.write('**Request Limit:** ' + str(STATELIMIT_01) + '/' + str(RATELIMIT_01))

###################################################################################################### API 00Marc

########################### First Line

col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11 = st.columns(11)

for i in range(11):
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
            st.info("🫶 Long/Short 🫶")
    if i == 8:
        with col9:
            st.info("#️⃣ Nb Trade #️⃣")
    if i == 9:
        with col10:
            st.info('〽️ Performance 〽️')
    if i == 10:
        with col11:
            st.info('✂️ Commission ✂️')



#################

##-----------------------------------------------------------------------> 00 - Feli

EQUITY_00 = authUSDT_00['result']['USDT']['equity']
NRZ_00 = authUSDT_00['result']['USDT']['unrealised_pnl']
PERF_00 = authUSDT_00['result']['USDT']['cum_realised_pnl']

AVAILABLE_00 = authUSDT_00['result']['USDT']['available_balance']
INPLAY_00 = (EQUITY_00 - AVAILABLE_00)/EQUITY_00



DEPOSIT_00 = EQUITY_00 - NRZ_00 - PERF_00
PNL100_00 = (round(EQUITY_00/DEPOSIT_00,4)-1)*100

TAXABLE_00 = NRZ_00 + PERF_00
#print('TO TAX: ' + str(TAXABLE_00))

if TAXABLE_00 > 0:
    COMMISSION_00 = TAXABLE_00 * TX
if TAXABLE_00 < 0:
    COMMISSION_00 = 0


##-----------------------------------------------------------------------> Nb

nbTrade_00 = 0
nbLong_00 = 0
nbShort_00 = 0

for x in a:
   oneTrade = posUSDT_00['result'][x]['data']["free_qty"] != 0
   if oneTrade:
       nbTrade_00 += 1

for x in a:
   oneLong = posUSDT_00['result'][x]['data']["free_qty"] < 0
   if oneLong:
       nbLong_00 += 1

for x in a:
   oneShort = posUSDT_00['result'][x]['data']["free_qty"] > 0
   if oneShort:
       nbShort_00 += 1

##-----------------------------------------------------------------------> Col

col1_00, col2_00 , col3_00, col4_00, col5_00, col6_00, col7_00, col8_00, col9_00, col10_00, col11_00 = st.columns(11)

for i in range(11):
    if i == 0:
        with col1_00:
            st.info('💁🏾‍♀️'' 00Feli')
    if i == 1:
        with col2_00:
            st.info("💰"' : ' + str(round(EQUITY_00,2)))
    if i == 2:
        with col3_00:
            st.info("⬇️"' : ' + str(round(DEPOSIT_00,2)))
    if i == 3:
        with col4_00:
            st.info("💸"' : ' + str(round(TAXABLE_00,2)))
    if i == 4:
        with col5_00:
            st.info("💸"' : ' + str(round(PERF_00,2)))
    if i == 5:
        with col6_00:
            st.info("💸"' : ' + str(round(NRZ_00,2)))
    if i == 6:
        with col7_00:
            st.info("💀"' : ' + str(round(INPLAY_00,2)*100) +'%')
    if i == 7:
        with col8_00:
            if nbTrade_00 == 0:
                st.info("🫶"' : No Trade')
            else:
                st.info("🫶"' : ' + str(nbLong_00) + ' / ' + str(nbShort_00) + ' (' + str(round((nbLong_00/nbTrade_00)*100)) + '/' + str(round((nbShort_00/nbTrade_00)*100)) + '%)')
    if i == 8:
        with col9_00:
            st.info("#️⃣"' : ' + str(nbTrade_00))
    if i == 9:
        with col10_00:
            st.info('〽️'' : ' + str(round(PNL100_00,3)) +'%')
    if i == 10:
        with col11_00:
            st.info('✂️'' : ' + str(round(COMMISSION_00,2)))

#################

#################

##-----------------------------------------------------------------------> 01 - Algo

session_auth_01 = usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com",
    api_key=config.apiKey100,
    api_secret=config.apiSecret100
)
authUSDT_01 = session_auth_01.get_wallet_balance()
posUSDT_01 = session_auth_01.my_position()


RATELIMIT_01 = authUSDT_01['rate_limit']
STATELIMIT_01 = authUSDT_01['rate_limit_status']
RESETLIMIT_01 = authUSDT_01['rate_limit_reset_ms']
#print(STATELIMIT_01)

EQUITY_01 = authUSDT_01['result']['USDT']['equity']
NRZ_01 = authUSDT_01['result']['USDT']['unrealised_pnl']
PERF_01 = authUSDT_01['result']['USDT']['cum_realised_pnl']

AVAILABLE_01 = authUSDT_01['result']['USDT']['available_balance']
INPLAY_01 = (EQUITY_01 - AVAILABLE_01)/EQUITY_01


DEPOSIT_01 = EQUITY_01 - NRZ_01 - PERF_01
PNL100_01 = (round(EQUITY_01/DEPOSIT_01,4)-1)*100

TAXABLE_01 = NRZ_01 + PERF_01
#print('TO TAX: ' + str(TAXABLE_01))

if TAXABLE_01 > 0:
    COMMISSION_01 = TAXABLE_01 * TX
if TAXABLE_01 < 0:
    COMMISSION_01 = 0

##-----------------------------------------------------------------------> NB

nbTrade_01 = 0
nbLong_01 = 0
nbShort_01 = 0

for x in a:
    oneTrade = posUSDT_01['result'][x]['data']["free_qty"] != 0
    if oneTrade:
        nbTrade_01 += 1

for x in a:
    oneLong = posUSDT_01['result'][x]['data']["free_qty"] < 0
    if oneLong:
        nbLong_01 += 1

for x in a:
    oneShort = posUSDT_01['result'][x]['data']["free_qty"] > 0
    if oneShort:
        nbShort_01 += 1


##-----------------------------------------------------------------------> Col

col1_01, col2_01 , col3_01, col4_01, col5_01, col6_01, col7_01, col8_01, col9_01, col10_01, col11_01 = st.columns(11)

for i in range(11):
    if i == 0:
        with col1_01:
            st.info('👨🏽‍🎓'' 01Algo')
    if i == 1:
        with col2_01:
            st.info("💰"' : ' + str(round(EQUITY_01,2)))
    if i == 2:
        with col3_01:
            st.info("⬇️"' : ' + str(round(DEPOSIT_01,2)))
    if i == 3:
        with col4_01:
            st.info("💸"' : ' + str(round(TAXABLE_01,2)))
    if i == 4:
        with col5_01:
            st.info("💸"' : ' + str(round(PERF_01,2)))
    if i == 5:
        with col6_01:
            st.info("💸"' : ' + str(round(NRZ_01,2)))
    if i == 6:
        with col7_01:
            st.info("💀"' : ' + str(round(INPLAY_01*100,0)) +'%')
    if i == 7:
        with col8_01:
            if nbTrade_01 == 0:
                st.info("🫶"' : No Trade')
            else:
                st.info("🫶"' : ' + str(nbLong_01) + ' / ' + str(nbShort_01) + ' (' + str(round((nbLong_01/nbTrade_01)*100)) + '/' + str(round((nbShort_01/nbTrade_01)*100)) + '%)')
    if i == 8:
        with col9_01:
            st.info("#️⃣"' : ' + str(nbTrade_01))
    if i == 9:
        with col10_01:
            st.info('〽️'' : ' + str(round(PNL100_01,3)) +'%')
    if i == 10:
        with col11_01:
            st.info('✂️'' : ' + str(round(COMMISSION_01,2)))

#################


col1T, col2T, col3T, col4T, col5T, col6T, col7T, col8T, col9T, col10T, col11T = st.columns(11)

for i in range(11):
    if i == 0:
        with col1T:
            st.info('Total')
    if i == 1:
        with col2T:
            st.info("💰"' : ' + str(round(EQUITY_00+EQUITY_01,2)))
    if i == 2:
        with col3T:
            st.info("⬇️"' : ' + str(round(DEPOSIT_00+DEPOSIT_01,2)))
    if i == 3:
        with col4T:
            st.info("💸"' : ' + str(round(TAXABLE_00+TAXABLE_01,2)))
    if i == 4:
        with col5T:
            st.info("💸"' : ' + str(round(PERF_00+PERF_01,2)))
    if i == 5:
        with col6T:
            st.info("💸"' : ' + str(round(NRZ_00+NRZ_01,2)))
    if i == 6:
        with col7T:
            st.info("💀"' : ' + str(round((EQUITY_00+EQUITY_01-AVAILABLE_00-AVAILABLE_01)/(EQUITY_00+EQUITY_01),2)*100)+'%')
    if i == 7:
        with col8T:
            st.info("🫶 Long/Short 🫶")
    if i == 8:
        with col9T:
            st.info("#️⃣"' : ' + str(nbTrade_00+nbTrade_01))
    if i == 9:
        with col10T:
            st.info('〽️'' : ' + str(round((PNL100_00*DEPOSIT_00+PNL100_01*DEPOSIT_01)/(DEPOSIT_00+DEPOSIT_01),2)) +'%')
    if i == 10:
        with col11T:
            st.info('✂️'' : ' + str(round(COMMISSION_00+COMMISSION_01,2)))



##----------------------------------------------------------------------->
##----------------------------------------------------------------------->
##----------------------------------------------------------------------->
##-----------------------------------------------------------------------> Details
##----------------------------------------------------------------------->
##----------------------------------------------------------------------->
##----------------------------------------------------------------------->




st.markdown('''# **Detail: 👨🏽‍🎓 01 - Algo**
''')

##########################


##-----------------------------------------------------------------------> 01 - Algo


col1_01, col2_01 , col3_01, col4_01, col5_01, col6_01, col7_01, col8_01, col9_01, col10_01, col11_01 = st.columns(11)

for i in range(11):
    if i == 0:
        with col1_01:
            st.info("Symbol")
            for x in a:
                oneTrade = posUSDT_01['result'][x]['data']["free_qty"] != 0
                if oneTrade:
                    st.info(str(posUSDT_01['result'][x]['data']['symbol']))
    if i == 1:
        with col2_01:
            st.info("Side")
            for x in a:
                oneTrade = posUSDT_01['result'][x]['data']["free_qty"] != 0
                if oneTrade:
                    st.info(str(posUSDT_01['result'][x]['data']['side']))
    if i == 2:
        with col3_01:
            st.info("Size")
            for x in a:
                oneTrade = posUSDT_01['result'][x]['data']["free_qty"] != 0
                if oneTrade:
                    st.info(str(posUSDT_01['result'][x]['data']['size']))
    if i == 3:
        with col4_01:
            st.info("Unrealised PNL")
            for x in a:
                oneTrade = posUSDT_01['result'][x]['data']["free_qty"] != 0
                if oneTrade:
                    st.info(str(posUSDT_01['result'][x]['data']['unrealised_pnl']))
    if i == 4:
        with col5_01:
            st.info("Realized PNL")
            for x in a:
                oneTrade = posUSDT_01['result'][x]['data']["free_qty"] != 0
                if oneTrade:
                    st.info(str(posUSDT_01['result'][x]['data']['cum_realised_pnl']))
    if i == 5:
        with col6_01:
            st.info("Entry Price")
            for x in a:
                oneTrade = posUSDT_01['result'][x]['data']["free_qty"] != 0
                if oneTrade:
                    st.info(str(posUSDT_01['result'][x]['data']['entry_price']))
    if i == 6:
        with col7_01:
            st.info("Last Price")
            # st.info(str(df[18]['last_price']))
            # st.info(str(df[18]['last_price']))
            # st.info(str(df[64]['last_price']))
            # st.info(str(df[64]['last_price']))
            # st.info(str(df[160]['last_price']))
            # st.info(str(df[160]['last_price']))
            # st.info(str(df[174]['last_price']))
            # st.info(str(df[174]['last_price']))
    # if i == 7:
    #     with col8_01:
    #         st.info("🫶"' : ' + str(nbLong_01) + ' / ' + str(nbShort_01) + ' (' + str(round((nbLong_01/nbTrade_01)*100)) + '/' + str(round((nbShort_01/nbTrade_01)*100)) + '%)')
    # if i == 8:
    #     with col9_01:
    #         st.info("#️⃣"' : ' + str(nbTrade_01))
    # if i == 9:
    #     with col10_01:
    #         st.info('〽️'' : ' + str(round(PNL100_01,3)) +'%')
    # if i == 10:
    #     with col11_01:
    #         st.info('✂️'' : ' + str(round(COMMISSION_01,2)))


##----------------------------------------------------------------------->



#st.markdown('''# **Detail: 💁🏾‍♀️ 00 - Feli**
#''')

##########################



##-----------------------------------------------------------------------> 00 - Feli
##-----------------------------------------------------------------------> 00 - Feli
##-----------------------------------------------------------------------> 00 - Feli
##-----------------------------------------------------------------------> 00 - Feli
##-----------------------------------------------------------------------> 00 - Feli

# col1_01, col2_01 , col3_01, col4_01, col5_01, col6_01, col7_01, col8_01, col9_01, col10_01, col11_01 = st.columns(11)
#
# for i in range(11):
#     if i == 0:
#         with col1_01:
#             st.info("Symbol")
#             for x in a:
#                 oneTrade = posUSDT_00['result'][x]['data']["free_qty"] != 0
#                 if oneTrade:
#                     st.info(str(posUSDT_00['result'][x]['data']['symbol']))
#     if i == 1:
#         with col2_01:
#             st.info("Side")
#             for x in a:
#                 oneTrade = posUSDT_00['result'][x]['data']["free_qty"] != 0
#                 if oneTrade:
#                     st.info(str(posUSDT_00['result'][x]['data']['side']))
#     if i == 2:
#         with col3_01:
#             st.info("Size")
#             for x in a:
#                 oneTrade = posUSDT_00['result'][x]['data']["free_qty"] != 0
#                 if oneTrade:
#                     st.info(str(posUSDT_00['result'][x]['data']['size']))
#     if i == 3:
#         with col4_01:
#             st.info("Unrealised PNL")
#             for x in a:
#                 oneTrade = posUSDT_00['result'][x]['data']["free_qty"] != 0
#                 if oneTrade:
#                     st.info(str(posUSDT_00['result'][x]['data']['unrealised_pnl']))
#     if i == 4:
#         with col5_01:
#             st.info("Realized PNL")
#             for x in a:
#                 oneTrade = posUSDT_00['result'][x]['data']["free_qty"] != 0
#                 if oneTrade:
#                     st.info(str(posUSDT_00['result'][x]['data']['cum_realised_pnl']))
#     if i == 5:
#         with col6_01:
#             st.info("Entry Price")
#             for x in a:
#                 oneTrade = posUSDT_00['result'][x]['data']["free_qty"] != 0
#                 if oneTrade:
#                     st.info(str(posUSDT_00['result'][x]['data']['entry_price']))
#     if i == 6:
#         with col7_01:
#             st.info("Last Price")


##-----------------------------------------------------------------------> 00 - Feli
##-----------------------------------------------------------------------> 00 - Feli
##-----------------------------------------------------------------------> 00 - Feli
##-----------------------------------------------------------------------> 00 - Feli
##-----------------------------------------------------------------------> 00 - Feli


























################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
###################################GARBAGE######################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
###################################GARBAGE######################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
###################################GARBAGE######################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
###################################GARBAGE######################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################



#for x in a:
#    print(x)
#    print(posUSDT_01['result'][x]['data']['symbol'])


#print(posUSDT_01['result'][139]['data']["side"])
#print(posUSDT_01['result'][140]['data']["side"])


# print(session_auth_01.query_kline(
#     symbol="BTCUSDT",
#     interval=1,
#     limit=2,
#     from_time=1581231260
# ))

# from time import sleep
# from pybit import usdt_perpetual
# ws_linear = usdt_perpetual.WebSocket(
#     test=True,
#     ping_interval=30000,  # the default is 30
#     ping_timeout=10000,  # the default is 10
#     domain="bybit"  # the default is "bybit"
# )


# def handle_message(msg):
#    print(msg)
# ##To subscribe to multiple symbols,
# ##pass a list: ["BTCUSDT", "ETHUSDT"]
#
# webS_00 = ws_linear.instrument_info_stream(handle_message, "ADAUSDT")
# webS_00 = ws_linear.instrument_info_stream(handle_message, "BTCUSDT")



#for i in webS_00:
#    print(i)

# ws_linear.instrument_info_stream(
#    handle_message, "BTCUSDT"
#



# user_id
# symbol
# side
# size
# position_value
# entry_price
# liq_price
# bust_price
# leverage
# auto_add_margin
# is_isolated
# position_margin
# occ_closing_fee
# realised_pnl
# cum_realised_pnl
# free_qty
# tp_sl_mode
# unrealised_pnl
# deleverage_indicator
# risk_id
# stop_loss
# take_profit
# trailing_stop
# position_idx
# mode


# df = pd.read_json('https://api.bybit.com/v2/public/tickers')['result'][0]['last_price']
# print(df)
# symbol : "BTCUSD"
# bid_price : "21550.5"
# ask_price : "21551"
# last_price : "21551.00"
# last_tick_direction : "ZeroPlusTick"
# prev_price_24h : "21650.00"
# price_24h_pcnt : "-0.004572"
# high_price_24h : "22552.00"
# low_price_24h : "21160.00"
# prev_price_1h : "21517.00"
# price_1h_pcnt : "0.00158"
# mark_price : "21563.84"
# index_price : "21565.39"
# open_interest : 436381001
# open_value : "14616.80"
# total_turnover : "108220000.03"
# turnover_24h : "54113.12"
# total_volume : 2800446771905
# volume_24h : 1175317818
# funding_rate : "-0.000065"
# predicted_funding_rate : "-0.000065"
# next_funding_time : "2022-07-09T08:00:00Z"
# countdown_hour : 7
# delivery_fee_rate : "0"
# predicted_delivery_price : ""
# delivery_time : ""


# import array as arr
#
# ALL = list(range(0, 349))
# print(ALL)
#
# a = arr.array('i', ALL)
#
# for x in a:
#     print(x)
#     print(posUSDT_01['result'][x]['data']['symbol'])


# print("Free QTY BUY:")
# print(posUSDT_01['result'][59]['data']["free_qty"])
#
#
#
# print("Free QTY SELL:")
# print(posUSDT_01['result'][60]['data']["free_qty"])
#

#
# print(bool(oneTrade))
# print(bool(oneLong))
# print(bool(oneShort))


# print("position_value:")
# print(posUSDT_01['result'][59]['data']["position_value"])
# print("Size:")
# print(posUSDT_01['result'][59]['data']["size"])
# print("Side:")
# print(posUSDT_01['result'][59]['data']["side"])
# print("Entry Price:")
# print(posUSDT_01['result'][59]['data']["entry_price"])
# print("Liq Price:")
# print(posUSDT_01['result'][59]['data']["liq_price"])
# print("Bust Price:")
# print(posUSDT_01['result'][59]['data']["bust_price"])
# print("Position Margin:")
# print(posUSDT_01['result'][59]['data']["position_margin"])
# print("R PNL:")
# print(posUSDT_01['result'][59]['data']["realised_pnl"])
# print("CUM PNL:")
# print(posUSDT_01['result'][59]['data']["cum_realised_pnl"])
# print("Free QTY:")
# print(posUSDT_01['result'][59]['data']["free_qty"])
# print("UN REALPNL:")
# print(posUSDT_01['result'][59]['data']["unrealised_pnl"])
# print("RISK ID:")
# print(posUSDT_01['result'][59]['data']["risk_id"])
# print("Position IDX:")
# print(posUSDT_01['result'][59]['data']["position_idx"])
# print("Mode:")
# print(posUSDT_01['result'][59]['data']["mode"])


################################## TEST
## To know what is the listing of the JSON
#for i in authUSDT_01['result']['USDT']['available_balance']:
#   print(i)
##
# print(session_auth_01.my_position(
#     symbol="BITUSDT"
# ))


#i = authUSDT_01['result']['USDT']
#print(i)


#array = list(range(0, 349))
#print(array)
#for i in array:



#import array as arr
#a = arr.array('i', [0, 1, 2, 3, 4, 10, 99, 100, 125, 348])
#a = arr.array('i', array)

#print(a)

# for i in a:
#     print (i)
#     for x in posUSDT_01['result'][i]['data']['symbol']:
#         print(x)

#for x in a:
#    print(posUSDT_01['result'][x]['data']['symbol'])


#for x in a:
#    for z in posUSDT_01['result'][x]['data']['symbol']:
#        print(z)
#print(posUSDT_01['result'][str(array)]['data']['symbol'])


############################################################################## FORM Bad then good
# input1 = st.number_input('Input 1', min_value=1, max_value=20, value=5)
# input2 = st.text_input('Input 2')
#
# if st.button('Generate Some Text'):
#    text = generate_text(input1, input2)
#    st.write(text)

# form = st.form(key="user_form")
# input1 = form.number_input('Input 1', min_value=1, max_value=20, value=5)
# input2 = form.text_input('Input 2')
#
# if form .form_submit_button('Generate Some Text'):
#    text = generate_text(input1, input2)
#    st.write(text)
############################################################################## FORM Bad then good


st.markdown('''# **Binance Price App**
''')

# Load market data from Binance API

#https://api.bybit.com/v2/public/tickers
#https://api.binance.com/api/v3/ticker/24hr

# Custom function for rounding values
def round_value(input_value):
    if input_value.values > 1:
        a = float(round(input_value, 2))
    else:
        a = float(round(input_value, 8))
    return a

col1, col2, col3 = st.columns(3)
#
# # Widget (Cryptocurrency selection box)
# col1_selection = st.sidebar.selectbox('Price 1', df.symbol, list(df.symbol).index('BTCUSD') )
# col2_selection = st.sidebar.selectbox('Price 2', df.symbol, list(df.symbol).index('ETHBUSD') )
# col3_selection = st.sidebar.selectbox('Price 3', df.symbol, list(df.symbol).index('BNBBUSD') )
# col4_selection = st.sidebar.selectbox('Price 4', df.symbol, list(df.symbol).index('XRPBUSD') )
# col5_selection = st.sidebar.selectbox('Price 5', df.symbol, list(df.symbol).index('ADABUSD') )
# col6_selection = st.sidebar.selectbox('Price 6', df.symbol, list(df.symbol).index('DOGEBUSD') )
# col7_selection = st.sidebar.selectbox('Price 7', df.symbol, list(df.symbol).index('SHIBBUSD') )
# col8_selection = st.sidebar.selectbox('Price 8', df.symbol, list(df.symbol).index('DOTBUSD') )
# col9_selection = st.sidebar.selectbox('Price 9', df.symbol, list(df.symbol).index('MATICBUSD') )
#
#
# # DataFrame of selected Cryptocurrency
# col1_df = df[df.symbol == col1_selection]
# col2_df = df[df.symbol == col2_selection]
# col3_df = df[df.symbol == col3_selection]
# col4_df = df[df.symbol == col4_selection]
# col5_df = df[df.symbol == col5_selection]
# col6_df = df[df.symbol == col6_selection]
# col7_df = df[df.symbol == col7_selection]
# col8_df = df[df.symbol == col8_selection]
# col9_df = df[df.symbol == col9_selection]
#
# # Apply a custom function to conditionally round values
# col1_price = round_value(col1_df.weightedAvgPrice)
# col2_price = round_value(col2_df.weightedAvgPrice)
# col3_price = round_value(col3_df.weightedAvgPrice)
# col4_price = round_value(col4_df.weightedAvgPrice)
# col5_price = round_value(col5_df.weightedAvgPrice)
# col6_price = round_value(col6_df.weightedAvgPrice)
# col7_price = round_value(col7_df.weightedAvgPrice)
# col8_price = round_value(col8_df.weightedAvgPrice)
# col9_price = round_value(col9_df.weightedAvgPrice)
#
# # Select the priceChangePercent column
# col1_percent = f'{float(col1_df.priceChangePercent)}%'
# col2_percent = f'{float(col2_df.priceChangePercent)}%'
# col3_percent = f'{float(col3_df.priceChangePercent)}%'
# col4_percent = f'{float(col4_df.priceChangePercent)}%'
# col5_percent = f'{float(col5_df.priceChangePercent)}%'
# col6_percent = f'{float(col6_df.priceChangePercent)}%'
# col7_percent = f'{float(col7_df.priceChangePercent)}%'
# col8_percent = f'{float(col8_df.priceChangePercent)}%'
# col9_percent = f'{float(col9_df.priceChangePercent)}%'
#
# # Create a metrics price box
# col1.metric(col1_selection, col1_price, col1_percent)
# col2.metric(col2_selection, col2_price, col2_percent)
# col3.metric(col3_selection, col3_price, col3_percent)
# col1.metric(col4_selection, col4_price, col4_percent)
# col2.metric(col5_selection, col5_price, col5_percent)
# col3.metric(col6_selection, col6_price, col6_percent)
# col1.metric(col7_selection, col7_price, col7_percent)
# col2.metric(col8_selection, col8_price, col8_percent)
# col3.metric(col9_selection, col9_price, col9_percent)

st.header('**All Price**')
st.dataframe(df)

st.markdown("""
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)
