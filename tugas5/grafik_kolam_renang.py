import matplotlib.pyplot as grafik
import numpy as np

data_pengunjung = np.array([3204,560,2900,2140,6679,3000,200,0,0,0,0,3518])

bulan =np.char.array(['Jan','Feb','Mar','Apr','Mei','Jun','Jul','Agu','Sep','Okt','Nov','Des'])

grafik.plot(bulan, data_pengunjung)
# anotasi di setiap titik
for a,b in zip(bulan, data_pengunjung): 
    grafik.text(a, b, str(b))
grafik.show()

grafik.bar(bulan, data_pengunjung)
# anotasi di atas tiap bar
for a,b in zip(bulan, data_pengunjung): 
    if b > 0:
        grafik.text(a, b, str(b))
grafik.show()

# menghitung persentase tiap data
porcent = 100.*data_pengunjung/data_pengunjung.sum()
patches = grafik.pie(data_pengunjung, shadow=True, startangle=90)[0]

# format label yang akan ditampilkan pada legenda
labels = ['{0} - {1:.2f} %'.format(bulan_val,porcent_val) for bulan_val,porcent_val in zip(bulan, porcent)]

# menampilkan legenda
grafik.legend(patches, labels, loc='best', bbox_to_anchor=(-0.1, 1.),
fontsize=8)

grafik.show()