import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as stats
from scipy.stats.mstats import winsorize

import warnings


ogrenciler = pd.read_csv("StudentsPerformance.csv")
ogrenciler.columns = ['cinsiyet', 'koken', 'aile_egt_seviyesi', 'ogle_yemegi',
                              'hazirlik_kursu', 'matematik_notu', 'okuma_notu', 'yazma_notu']


#Sınavlardaki performans cinsiyete, kökene ve anne-baba eğitim durumuna göre değişiklik göstermekte midir?
#
# plt.figure(figsize=(14,9))
#
# plt.subplot(3,3,1)
# sns.barplot(ogrenciler["cinsiyet"], ogrenciler["matematik_notu"])
# plt.title("Math-cinsiyet")
#
# plt.subplot(3,3,2)
# sns.barplot(ogrenciler["koken"], ogrenciler["matematik_notu"])
# plt.title("Math-Koken")
#
# plt.subplot(3,3,3)
# # draw the heatmap using seaborn.
# sns.barplot(ogrenciler["aile_egt_seviyesi"], ogrenciler["matematik_notu"])
# plt.title("Math-Aile eğitimi")
#
# plt.subplot(3,3,4)
# sns.barplot(ogrenciler["cinsiyet"], ogrenciler["okuma_notu"])
# plt.title("Okuma-cinsiyet")
#
# plt.subplot(3,3,5)
# sns.barplot(ogrenciler["koken"], ogrenciler["okuma_notu"])
# plt.title("Okuma-Koken")
#
# plt.subplot(3,3,6)
# # draw the heatmap using seaborn.
# sns.barplot(ogrenciler["aile_egt_seviyesi"], ogrenciler["okuma_notu"])
# plt.title("Okuma-Aile eğitimi")
#
#
# plt.subplot(3,3,7)
# sns.barplot(ogrenciler["cinsiyet"], ogrenciler["yazma_notu"])
# plt.title("Yazma-cinsiyet")
#
# plt.subplot(3,3,8)
# sns.barplot(ogrenciler["koken"], ogrenciler["yazma_notu"])
# plt.title("Yazma-Koken")
#
# plt.subplot(3,3,9)
# # draw the heatmap using seaborn.
# sns.barplot(ogrenciler["aile_egt_seviyesi"], ogrenciler["yazma_notu"])
# plt.title("Yazma-Aile eğitimi")
#
# plt.tight_layout()
#
# plt.show()

## koken ve aile eğitimine göre değişiklik var


##------------------------------------------------------------------------------------

#Öğle yemek tipinin sınav performansları ile bir ilişkisi var mı? Varsa bunu nasıl açıklayabilirsiniz?

# plt.figure(figsize=(14,7))
#
# plt.subplot(1,3,1)
# sns.barplot(ogrenciler["ogle_yemegi"], ogrenciler["matematik_notu"])
# plt.title("Matematik")
#
# plt.subplot(1,3,2)
# sns.barplot(ogrenciler["ogle_yemegi"], ogrenciler["okuma_notu"])
# plt.title("Okuma")
#
# plt.subplot(1,3,3)
# # draw the heatmap using seaborn.
# sns.barplot(ogrenciler["ogle_yemegi"], ogrenciler["yazma_notu"])
# plt.title("Yazma")
#
# plt.show()
#
#
# oglen_yemegi_yiyenler = ogrenciler[ogrenciler["ogle_yemegi"] == "standard"]
# oglen_yemegi_yemeyenler = ogrenciler[ogrenciler["ogle_yemegi"] == "free/reduced"]
# print("Öğle yemeği yiyenler:\n",oglen_yemegi_yiyenler.mean())
# print("Öğle yemeği yemeyenler:\n",oglen_yemegi_yemeyenler.mean())

##----------------------------------------------------------------------------------------

#azırlık kurslarının sonav performansı üzerinde bir etkisi var mı?

# plt.figure(figsize=(14,7))
#
# plt.subplot(1,3,1)
# sns.barplot(ogrenciler["hazirlik_kursu"], ogrenciler["matematik_notu"])
# plt.title("Matematik")
#
# plt.subplot(1,3,2)
# sns.barplot(ogrenciler["hazirlik_kursu"], ogrenciler["okuma_notu"])
# plt.title("Okuma")
#
# plt.subplot(1,3,3)
# # draw the heatmap using seaborn.
# sns.barplot(ogrenciler["hazirlik_kursu"], ogrenciler["yazma_notu"])
# plt.title("Yazma")
#
# plt.show()

##----------------------------------------------------------------------

##Birbiriyle korelasyonu en fazla olan dersler hangisidir?

# print(ogrenciler.corr())
# print("En çok okuma ve yazma birbiriyle alakalı")
#
# sns.heatmap(ogrenciler.corr(), square=True, annot=True, linewidths=.5, vmin=0, vmax=1, cmap='viridis')
# plt.title("Korelasyon Matrisi ")
# plt.show()