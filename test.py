import toolboxes.toolbox_nf as nf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import h5py

#mean trace

data_path = "A:\\shared\\iyorulmaz\\Calcium_Imaging_Aufnahmen\\Tiff\\single_fish\\single_fish_rec1_with_Ketamin\\"

file_name = "rec1_5_fish_50Vcm_4s_withketamine_2p5mm_fish4.tif"

# load single fish

rec = nf.read_tif(data_path + file_name)

mean_trace = np.zeros((900, 1)) #2D-Array (900 Zeile, 1 Spalte)

for i in range(rec.shape[0]): #rec.shape = gibt die Anzahl der Zeilen zurück = "900", range(900) = erzeugt Zahlen von 0 bis 899
    mean_trace[i] = np.mean(rec[i])

fig, axs = plt.subplots() #mehrere Diagramme in einer Abbildung darstellen
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

print(death_data_wketamin.iloc[:, 0]) # Alle Reihen aber mit bestimmter Spalte

#len() function returns the number of elements in the list.

#Hab zufälligerweise mean-wert von allen Recordings berechnet
import pandas as pd
death_data_wketamin = pd.read_csv("A:\\shared\\iyorulmaz\\Isins_Excel_Chart.csv", delimiter=';')
group_all = death_data_wketamin.groupby("recording")["dead_next_day"].mean()*100
print(group_all)


#death_data_wketamin.shape -> (25,15) = 25 Reihen , 15 Spalten

#Mortalitätsrate von rec1
mort_rate_rec1 = rec1["dead_next_day"].mean()*100
print(mort_rate_rec1)

#death_data_wketamin[death_data_wketamin['recording'] == '1']

#Loopen
import pandas as pd
import matplotlib.pyplot as plt
death_data_wketamin = pd.read_csv("A:\\shared\\iyorulmaz\\Isins_Excel_Chart.csv", delimiter=';')

recording = death_data_wketamin["recording"]
for i in range(len(recording)): #len zählt wie viele unterschiedliche rec
    rec = recording.iloc[i] #greift aufs element position i
    data = death_data_wketamin[death_data_wketamin["recording"] == rec] # behält die zeilen, die True ist
    mortality =data["dead_next_day"].mean()*100
    print(rec,mortality)

#Boxplot
fig, axs = plt.subplots()
ax.boxplot(...)

ax.set.xlabel("")
ax.set.ylabel("")
plt.show()

# Boxplot nur Ketamin
import pandas as pd
import matplotlib.pyplot as plt
death_data_wketamin = pd.read_csv("A:\\shared\\iyorulmaz\\Isins_Excel_Chart.csv", delimiter=';')
group_all = death_data_wketamin.groupby("recording")["dead_next_day"].mean()*100
print(group_all)

plt.boxplot(group_all)
plt.title('Mortalityrate with Ketamin')
plt.ylabel('Mortalityrate %')
plt.xlabel('Recordings')
plt.show()

# Boxplot w.Ketamin and wo.Ketamin next to each other
import pandas as pd
import matplotlib.pyplot as plt

death_data_wketamin = pd.read_csv("A:\\shared\\iyorulmaz\\Isins_Excel_Chart.csv", delimiter=';')
death_data_woketamin =pd.read_csv("A:\\shared\\iyorulmaz\\screening_results_von_Natalie.csv" , delimiter=';')
group_keta = death_data_wketamin.groupby("recording")["dead_next_day"].mean()*100
group_noketa = death_data_woketamin.groupby("recording")["dead_next_day"].mean()*100
print(group_keta)
print(group_noketa)

plt.boxplot([group_keta, group_noketa], tick_labels = ['with Ketamin', 'without Ketamin'])
plt.title('Mortality rate with Ketamin and without Ketamin')
plt.ylabel('Mortality rate %')
plt.show()

import toolboxes.toolbox_nf as nf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import h5py

#mean trace

data_path = "A:\\shared\\iyorulmaz\\Calcium_Imaging_Aufnahmen\\Tiff\\single_fish\\single_fish_rec1_with_Ketamin\\"

file_name = "rec1_5_fish_50Vcm_4s_withketamine_2p5mm_fish4.tif"

# load single fish

rec = nf.read_tif(data_path + file_name)

mean_trace = np.zeros((900, 1)) #2D-Array (900 Zeile, 1 Spalte)

for i in range(rec.shape[0]): #rec.shape = gibt die Anzahl der Zeilen zurück = "900", range(900) = erzeugt Zahlen von 0 bis 899
    mean_trace[i] = np.mean(rec[i])

fig, axs = plt.subplots() #mehrere Diagramme in einer Abbildung darstellen
axs.plot(mean_trace) #stellt die Werte als Graph dar
plt.show()
