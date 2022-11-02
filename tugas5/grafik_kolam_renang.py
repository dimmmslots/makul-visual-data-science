import matplotlib.pyplot as grafik
import pandas as pd

# data_pengunjung = np.array([3204,560,2900,2140,6679,3000,200,0,0,0,0,3518])
df = pd.read_excel('data-tugas5.xlsx', sheet_name='Sheet1')

# 12 different distinct colors
colors = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'black', 'white', 'purple', 'orange', 'brown', 'grey']
data_pengunjung = df['Kolam Renang']

bulan = df['Bulan']
bulan_short = [x[:3] for x in bulan]
print(bulan_short)


grafik.plot(bulan_short, data_pengunjung)
# anotasi di setiap titik
for a,b in zip(bulan_short, data_pengunjung): 
    grafik.text(a, b, str(b))
grafik.show()

grafik.bar(bulan_short, data_pengunjung)
# anotasi di atas tiap bar
for a,b in zip(bulan_short, data_pengunjung): 
    if b > 0:
        grafik.text(a, b, str(b))
grafik.show()

# menghitung persentase tiap data
porcent = 100.*data_pengunjung/data_pengunjung.sum()
patches = grafik.pie(data_pengunjung, shadow=True, startangle=90,colors=colors)[0]

# format label yang akan ditampilkan pada legenda
labels = ['{0} - {1:.2f} %'.format(bulan_val,porcent_val) for bulan_val,porcent_val in zip(bulan_short, porcent)]

# menampilkan legenda
grafik.legend(patches, labels, loc='best', bbox_to_anchor=(0,1),
fontsize=8)

grafik.show()

