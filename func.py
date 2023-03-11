import pandas as pd
import numpy as np
import pandas_datareader as pdr
import yfinance as yf
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import stumpy


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


def pair_finder(dataframe, window_size, graph=False):
    """
    belirlenen window_size kapsamında en son oluşmuş olan paterne en çok benzeyen
    geçmişteki en iyi eşleşmeyi buur ve konumunu görsel üzerinde göstrerir.

    :param dataframe:
        zaman serisi incelemesi yapılacak veri seti.
        type: dataframe
    :param window_size:
        inceleme yapılacak patran aranacak zaman adımı mikarı
        type: integer
        +----------------------------------------------------+
        |   örn:                                             |
        |   borsa için 4 saatlik bir veri setinde bir        |
        |   haftalık bir zaman aralığına                     |
        |   en uygun eşleşmeyi bulmak istiyorsak 6*5 = 30    |
        |   adımlık inceleme subspace'i seçilmeli            |
        +----------------------------------------------------+
    :param graph:
        oluşturulan matrix profile grafiği çizilsin.
        default = False
    :return:
        grafik veya none
    """
    matrix_profile = stumpy.stump(dataframe, m=window_size)
    print("matrix profile oluşturuldu")

    # en sondaki subspacein en iyi eşleşmeye sahip oldugu
    # pair'i yakalayacagız
    print("{}. indexteki patern için en benzer durum araştırılacak".format(len(matrix_profile)-1))
    nearest_neighbor_idx = matrix_profile[len(matrix_profile)-1,1]
    print(f"en yakın komşu {nearest_neighbor_idx}. indexte tespit edildi")

    if graph:
        fig, axs = plt.subplots(2, sharex=True, gridspec_kw={'hspace': 0})
        plt.suptitle('Motif (Pattern) Discovery', fontsize='30')


        axs[0].plot(dataframe.values)
        axs[0].set_ylabel('Türk Lirası', fontsize='20')
        rect = Rectangle((len(matrix_profile)-1, 0), 30, 40, facecolor='lightgrey')
        axs[0].add_patch(rect)
        rect = Rectangle((nearest_neighbor_idx, 0), 30, 40, facecolor='green')
        axs[0].add_patch(rect)
        axs[1].set_xlabel('Time', fontsize='20')
        axs[1].set_ylabel('Matrix Profile', fontsize='20')
        axs[1].axvline(x=len(matrix_profile)-1, linestyle="dashed")
        axs[1].axvline(x=nearest_neighbor_idx, linestyle="dashed")
        axs[1].plot(matrix_profile[:, 0])
        plt.show()


