import streamlit as st
import yfinance as yf
import pandas as pd
# Create a text input box and assign its value to a variable
s1 = st.text_input("Please enter the ticker of your first Stock (s1)")

s2 = st.text_input("Please enter the ticker of your second Stock (s2)")

days=st.text_input('How Many Days To include')

tickerH = yf.Ticker(s1)

HBABA = tickerH.history(period=f"{days}d")

HBABA=HBABA[['Open','Close']]

save_s1=HBABA

tickerU = yf.Ticker(s2)

UBABA = tickerU.history(period=f"{days}d")

UBABA=UBABA[['Open','Close']]

save_s2=UBABA

HBABA['%ChangeS1']=(HBABA['Close']-HBABA['Open'])/HBABA['Open']

UBABA['%ChangeS2']=(UBABA['Close']-UBABA['Open'])/UBABA['Open']

UBABA=UBABA.reset_index(drop=False)
HBABA=HBABA.reset_index(drop=False)

UBABA=UBABA[['%ChangeS2']]


HBABA=HBABA[['%ChangeS1']]

com=HBABA.join(UBABA)

corr=com['%ChangeS1'].corr(com['%ChangeS2'])

save_s1.index=save_s1.index.astype(str)
save_s2.index=save_s2.index.astype(str)


save_s1.index=save_s1.index.map(lambda x:x.split()[0])
save_s2.index=save_s2.index.map(lambda x:x.split()[0])



# Display the input value
st.write(f'The correlation between {s1} and {s2} is {corr}')

if st.checkbox('Show Daily Percentage Change'):
    st.dataframe(com)
    
if st.checkbox('Show Full Data'):
    col1, col2 = st.columns(2)
    col1.dataframe(save_s1)
    col2.dataframe(save_s2)
    