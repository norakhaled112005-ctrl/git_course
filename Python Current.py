

import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# إعداد واجهة المستخدم (Requirements 8)
st.title("Stock Market Analysis System")
st.write("Developed for Dr. Khalaf's Project")

# مدخلات المستخدم (Functional Requirements 4)
symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, MSFT):", "AAPL")

if symbol:
    try:
        # جلب البيانات (System Workflow 7)
        data = yf.Ticker(symbol)
        df = data.history(period="1mo")
        
        if not df.empty:
            # عرض السعر الحالي
            st.subheader(f"Data for {symbol.upper()}")
            st.metric("Current Price", f"${df['Close'].iloc[-1]:.2f}")
            
            # عرض جدول البيانات (Historical data)
            st.write("Historical Data (Last 7 Days)")
            st.dataframe(df.tail(7))

            # رسم الرسم البياني (Visualization Requirement 4)
            fig = go.Figure(data=[go.Scatter(x=df.index, y=df['Close'], mode='lines')])
            fig.update_layout(title="Stock Price Trend", xaxis_title="Date", yaxis_title="Price")
            st.plotly_chart(fig)
        else:
            st.error("Invalid symbol. Please enter a valid stock symbol.")
    except Exception as e:
        st.error(f"Error: {e}")




