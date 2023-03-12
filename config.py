# veri setinde aranacak paternin uzunluğu
"""
elimizdeki borsa verisinin saatlik mi dakikalık mı
yoksa günlük mü oldugunua göre mantıklı bir deger secilmeli
örneğin:
4 saatlik bir borsa verisi bir günde 6 kez ölçüm yapar, 1 hafta
için 6*5= 30 birim uzunluktaki paternler incelenmeli
(hafta sonları işlem yok 7 değil 5 gün)
"""
window_size=42
stock_name= "ISCTR.IS"
period = "5y"