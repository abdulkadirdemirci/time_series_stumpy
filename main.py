# imports
import pandas as pd
import numpy as np
import pandas_datareader as pdr
import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance as mpl

import datetime as dt

pd.set_option("display.max_columns",None)

data = yf.Ticker("ISCTR.IS").history(period="5y")




