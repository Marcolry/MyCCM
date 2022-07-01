import streamlit as st
import pandas as pd
import config
import bybit
from pybit import usdt_perpetual
import time
TX = 0.3

st.markdown('''# **AlgoFinance Dashboard**
''')

##################################

st.header('**Summary**')


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
############################################## Refresh


################################################LIMIT

RATELIMIT_USDT = authUSDT['rate_limit']
STATELIMIT_USDT = authUSDT['rate_limit_status']
RESETLIMIT_USDT = authUSDT['rate_limit_reset_ms']

print(RATELIMIT_USDT)
print(STATELIMIT_USDT)
print(RESETLIMIT_USDT)

# import datetime
# timestamp = datetime.datetime.fromtimestamp(1656637052)
# print(timestamp.strftime('%Y-%m-%d %H:%M:%S'))

#st.write(str(STATELIMIT_USDT) + ' requests left on ' + str(RATELIMIT_USDT))

###################################################

import streamlit as st
from streamlit_autorefresh import st_autorefresh

# Run the autorefresh about every 2000 milliseconds (2 seconds) and stop
# after it's been refreshed 100 times.
count = st_autorefresh(interval=10000, limit=100, key="FizzBuzz")

# The function returns a counter for number of refreshes. This allows the
# ability to make special requests at different intervals based on the count
if count == 0:
    st.write("Count is zero")
elif count % 3 == 0 and count % 5 == 0:
    st.write(f"Count: {count}/100")
elif count % 3 == 0:
    st.write(f"Count: {count}/100" + ' and ' + str(STATELIMIT_USDT) + '/' + str(RATELIMIT_USDT))
elif count % 5 == 0:
    st.write(f"Count: {count}/100" + ' and ' + str(STATELIMIT_USDT) + '/' + str(RATELIMIT_USDT))
else:
    st.write(f"Count: {count}/100" + ' and ' + str(STATELIMIT_USDT) + '/' + str(RATELIMIT_USDT))



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




##################################

EQUITY_USDT = authUSDT['result']['USDT']['equity']
NRZ_USDT = authUSDT['result']['USDT']['unrealised_pnl']
PERF_USDT = authUSDT['result']['USDT']['cum_realised_pnl']



#for i in RATELIMIT_USDT:
#   print(i)

print('EQUITY: ' + str(EQUITY_USDT))
print('NOT REALIZED: ' + str(NRZ_USDT))
print('PERFORMANCE: ' + str(PERF_USDT))

Math = EQUITY_USDT - NRZ_USDT - PERF_USDT
print('TOTAL: ' + str(round(Math)))

TAXABLE = NRZ_USDT + PERF_USDT
print('TO TAX: ' + str(TAXABLE))

COMMISSION = TAXABLE * TX
if TAXABLE > 0:
    print('COMMISSION: ' + str(COMMISSION))
if TAXABLE < 0:
    print('COMMISSION: 0')


############################################################################################# END


# Load market data from Binance API
#df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')

# Custom function for rounding values
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

PNL100 = (round(EQUITY_USDT/round(Math),4)-1)*100

for i in range(len(crpytoList.keys())):
    # selected_crypto_label = list(crpytoList.keys())[i]
    # selected_crypto_index = list(df.symbol).index(crpytoList[selected_crypto_label])
    # selected_crypto = st.sidebar.selectbox(selected_crypto_label, df.symbol, selected_crypto_index, key = str(i))
    # col_df = df[df.symbol == selected_crypto]
    # col_price = round_value(col_df.weightedAvgPrice)
    # col_percent = f'{float(col_df.priceChangePercent)}%'

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


####################################################
# st.info('DEPOSIT: ' + str(round(Math)))
# st.info('EQUITY: ' + str(round(EQUITY_USDT,2)))
#
# PNL100 = (round(EQUITY_USDT/round(Math),4)-1)*100
# st.info('PERFORMANCE: ' + str(round(PNL100,2)) +'%')
# # st.info('NOT REALIZED: ' + str(NRZ_USDT))
# # st.info('PERFORMANCE: ' + str(PERF_USDT))
#
# st.info('TAXABLE: ' + str(round(TAXABLE,2)))
# st.info('COMMISSION: ' + str(round(COMMISSION,2)))

#########

#st.metric(selected_crypto, col_price, col_percent)
#st.header('**All Price**')
#st.dataframe(df)

#print(df)

