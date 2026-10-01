import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

def make_historical_chart(stock):
    df = pd.read_csv(f"../data/stocks/{stock}.txt", sep=',')
    df.columns = df.columns.str.strip().str.replace('<','').str.replace('>','').str.title().str.replace("Vol","Volume")
    df.index = pd.to_datetime(df["Date"].astype(str), format="%Y%m%d")
    df = df[["Open","High", "Low", "Close", "Volume"]]
    df_limited = df.iloc[-500:]
    mpf.plot(df_limited, type="candle", style="yahoo", title=f"{stock} OHCL", volume=True, ylabel="Cena", ylabel_lower="Wolumen", savefig=f"../charts/{stock}.png")

make_historical_chart("xtb")
