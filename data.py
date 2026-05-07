import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web
from datetime import date

start = "2026-01-01"
end =  date.today()

#treasury yields
series = {
    "3M": "DGS3MO",
    "6M": "DGS6MO",
    "1Y": "DGS1",
    "2Y": "DGS2",
    "5Y": "DGS5",
    "10Y": "DGS10"

}

df = pd.DataFrame()

for label, code in series.items():
    df[label] = web.DataReader(code,"fred",start, end)


df = df.dropna()

df = df.iloc[-1]



# forming the curve

curve = pd.DataFrame({
    "tenor_years" : [0.25, 0.5, 1, 2, 5, 10],
    "yield_pct" : [
        df["3M"], df["6M"], df["1Y"], df["2Y"], df["5Y"], df["10Y"]
    ]
})

curve["r"]  = curve["yield_pct"]  /100     # converting to raw values from pct


# discount factor

curve["discount_factor"] = np.exp(-curve["r"] * curve["tenor_years"])


# zero curve

curve["zero_rate"] = -np.log(curve["discount_factor"])/ curve["tenor_years"]

print(curve)


