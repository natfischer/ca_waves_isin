import toolboxes.toolbox_nf as nf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import h5py

#mean trace

data_path = "A:\\shared\\iyorulmaz\\Calcium_Imaging_Aufnahmen\\Tiff\\single_fish\\single_fish_rec1_with_Ketamin\\"

file_name = "rec1_5_fish_50Vcm_4s_withketamine_2p5mm_fish3.tif"

# load single fish

rec = nf.read_tif(data_path + file_name)

mean_trace = np.zeros((900, 1)) #2D-Array (900 Zeile, 1 Spalte)

for i in range(rec.shape[0]):
    mean_trace[i] = np.mean(rec[i])

fig, axs = plt.subplots()
axs.plot(mean_trace)
plt.show()

plt.savefig("A:\\shared\\iyorulmaz\\figures\\test.png", dpi=300)

#CSV datei einlesen
import pandas as pd
death_data_wketamin = pd.read_csv("A:\\shared\\iyorulmaz\\Isins_Excel_Chart.csv", delimiter=';')
death_data_woketamin = pd.read_csv("A:\\shared\\iyorulmaz\\screening_results_von_Natalie.csv", delimiter=';')

print(death_data_wketamin.head()) #liefert erste 5 Reihe raus
print(death_data_woketamin.head())

#Nur zwei Spalten von CSV einlesen
Auswahl = death_data_wketamin[["recording" , "dead_next_day"]]
print(Auswahl)

print(death_data_wketamin.iloc[:, 1])

