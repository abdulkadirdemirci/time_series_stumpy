import pandas as pd
import numpy as np
import pandas_datareader as pdr
import yfinance as yf
import matplotlib.pyplot as plt
import plotly.graph_objects as go


# belirtilen zaman aralıgındaki veriyi görselleştir.

def subseq_vis(data, deger, starts_, ends_, both=False, candle=False):
    """
    veri sertini candle stick formatında görselleştirmek veya
    high, low, open, close parametrelerinden birini çizgi grafigi ile
    veya birden fazlasını çizgi grafiği ile görselleştirmek için kullanılır.

    çizgi grafikleri matplotlib kütüphanesi ile görselleştirilir.
    candle stick grafiği ise mplfinance kütüphanesi ile görselleştirilir.

    :param data:
        veri seti.
        type = dataframe
    :param deger:
        candle= false old. durumda hangi koonun görselleştirileceği (high, low, open, close)
        type = string or list
    :param starts_:
        görselleştirmenin yapılacacı başlangıç tarihi
        type = string
    :param ends_:
        görselleştirmenin yapılacacı bitiş tarihi
        type = string
    :param both:
        birden fazla parametre görselleştirilecegi zaman True yap.
        default = False
    :param candle:
        candle stick görselleştirmsi yapmak için.
        default = False
    :return:
    """

    starts = starts_ + " 00:00:00+03:00"
    ends = ends_ + " 00:00:00+03:00"
    print("BAŞLANGIÇ: ", starts, "\nBİTİŞ: ", ends)

    if candle:
        mpl.plot(data[(data.index >= starts) & (data.index < ends)],
                 type="candle",
                 title=f"{starts_} - {ends_} candle stick graph",
                 style="yahoo")

    if both:
        for item in deger:
            plt.plot(data[(data.index >= starts) & (data.index < ends)].index,
                     data[(data.index >= starts) & (data.index < ends)][item], label=item)
            plt.legend()
            plt.title(f"{starts_} - {ends_} line graph")
            plt.xticks(rotation=45)
        plt.show()

    else:
        plt.plot(data[(data.index >= starts) & (data.index < ends)].index,
                 data[(data.index >= starts) & (data.index < ends)]["Open"])
        plt.xticks(rotation=45)
        plt.title(f"{starts_} - {ends_} line graph")
        plt.show()
