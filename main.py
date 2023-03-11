# imports
import pandas as pd
import numpy as np
import pandas_datareader as pdr
import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance as mpl
import datetime as dt
import stumpy
from matplotlib.patches import Rectangle

pd.set_option("display.max_columns", None)

data = yf.Ticker("ISCTR.IS").history(period="5y")

# matrix profile oluşturuldu
matrix_profile = stumpy.stump(data["Open"], m=30)

# hesaplanan tüm equlidian distancelar
matrix_profile[:, 0]

# uzaklıkları küçükten biyige sıralayıp en küçük uzaklığı bulucaz
# amacımız en iyi eşleşmenin oldugu çifti belirlemek hangi iki kısım
# bir motif oluşturmuş. argsort'un docstringini oku. küçükten buyuge sırlar ama
# değerleri değil index bilgisini yansıtır.
motif_idx = np.argsort(matrix_profile[:, 0])


# en küçüğü
motif_idx = np.argsort(matrix_profile[:, 0])[0]
print(f"The motif is located at index {motif_idx}")

# motifin oluştugu yeri bulduk şimdi hangi indexteki paterm ile çift oluğunu bulucaz
nearest_neighbor_idx = matrix_profile[motif_idx, 1]
print(f"The nearest neighbor is located at index {nearest_neighbor_idx}")



nearest_neighbor_idx = matrix_profile[len(matrix_profile)-1, 1]
# grafik üzerinde görselleştirme
fig, axs = plt.subplots(2, sharex=True, gridspec_kw={'hspace': 0})
plt.suptitle('Motif (Pattern) Discovery', fontsize='30')

axs[0].plot(data["Open"].values)
axs[0].set_ylabel('açılış fiyatı', fontsize='20')
rect = Rectangle((len(matrix_profile)-1, 0), 30, 40, facecolor='lightgrey')
axs[0].add_patch(rect)
rect = Rectangle((nearest_neighbor_idx, 0), 30, 40, facecolor='green')
axs[0].add_patch(rect)

axs[1].set_xlabel('Time', fontsize ='20')
axs[1].set_ylabel('Matrix Profile', fontsize='20')
axs[1].axvline(x=len(matrix_profile)-1, linestyle="dashed")
axs[1].axvline(x=nearest_neighbor_idx, linestyle="dashed")
axs[1].plot(matrix_profile[:, 0])
plt.show()