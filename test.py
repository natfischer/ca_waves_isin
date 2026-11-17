import toolboxes.toolbox_nf as nf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import h5py

from my_anaylsis import death_data

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

plt.boxplot([group_keta, group_noketa], tick_labels = ['with Ketamin', 'Control'])
plt.title('Mortality rate with and without Ketamin')
plt.ylabel('Mortality [%]')
plt.show()   # wie viele aufnahmen   LARA UNd meine daten nebeneinader ? signifikant? statistischer test welcher? anhand mortalitätsrate

#mean trace
#load single fish
import toolboxes.toolbox_nf as nf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import h5py

data_path = "A:\\shared\\iyorulmaz\\Calcium_Imaging_Aufnahmen\\Tiff\\single_fish\\single_fish_rec2_with_Ketamin\\"
fiile_name = "rec2_5_fish_50Vcm_4s_withketamine_2p5mm_fish5.tif"
reec = nf.read_tif(data_path + fiile_name)

mean_trace = []
for im in reec:
    mean_trace.append(np.mean(im))

plt.figure()
plt.plot(mean_trace)
plt.xlabel('Frames')
plt.ylabel('mean fluorescence [a.u.]')
plt.show()

#load multiple fish
import toolboxes.toolbox_nf as nf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import h5py

data_path = "A:\\shared\\iyorulmaz\\Calcium_Imaging_Aufnahmen\\Tiff\\single_fish\\single_fish_rec8_with_Ketamin\\"
file_names = ["rec8_5_fish_50Vcm_4s_withketamine_2p5mm_fish1.tif",
             "rec8_5_fish_50Vcm_4s_withketamine_2p5mm_fish2.tif",
             "rec8_5_fish_50Vcm_4s_withketamine_2p5mm_fish3.tif",
             "rec8_5_fish_50Vcm_4s_withketamine_2p5mm_fish4.tif",
             "rec8_5_fish_50Vcm_4s_withketamine_2p5mm_fish5.tif"]

fs = 0.25 #[Hz] [fps] frame per second 900/3600 = 0,25 # sampling frequency # Alle 4 Sekunden ein Bild gemacht
mean_traces = []

for file in file_names:

    rec = nf.read_tif(data_path + file)
    mean_trace = []
    for im in rec:
        mean_trace.append(np.mean(im))

    mean_traces.append(np.array(mean_trace))

t = np.linspace(0, rec.shape[0]/fs,rec.shape[0]) / 60

plt.figure()
for trace, rec in zip(mean_traces, file_names):
    plt.plot(t, trace, label=rec) # fluo-werte gegen zeit
plt.xlabel('time [min]')
plt.ylabel('mean fluorescence [a.u.]') #arbitrary units
plt.legend()
plt.show()


#mean_trace = np.zeros((900, 1)) #2D-Array (900 Zeile, 1 Spalte) Gibt ein neues Array der angegebenen Form und des angegebenen Typs zurück, das mit Nullen gefüllt ist.

#for i in range(rec.shape[0]): #rec.shape = gibt die Anzahl der Zeilen zurück = "900", range(900) = erzeugt Zahlen von 0 bis 899
#    mean_trace[i] = np.mean(rec[i])

#fig, axs = plt.subplots() # Create a figure containing a single Axes
#axs.plot(mean_trace) #stellt die Werte als Graph dar
#plt.show()

#Tot und lebende Fische in einer Grafik
import toolboxes.toolbox_nf as nf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import h5py

#Pfad zum toten Fisch
tot_fish = "A:\\shared\\iyorulmaz\\Calcium_Imaging_Aufnahmen\\Tiff\\single_fish\\single_fish_rec4_with_Ketamin\\"
loc = "rec4_5_fish_50Vcm_4s_withketamine_2p5mm_fish5.tif"

#Pfad zum überlebten Fisch
überlebter_fisch = "A:\\shared\\iyorulmaz\\Calcium_Imaging_Aufnahmen\\Tiff\\single_fish\\single_fish_rec2_with_Ketamin\\"
loc1 = "rec2_5_fish_50Vcm_4s_withketamine_2p5mm_fish1.tif"

#Toter Fisch laden
rec = nf.read_tif(tot_fish + loc)

mean_trace_tot = []
for im in rec:
    mean_trace_tot.append(np.mean(im))

#Überlebender Fisch laden
rec = nf.read_tif(überlebter_fisch + loc1)

mean_trace_überlebend = []
for im in rec:
    mean_trace_überlebend.append(np.mean(im))

plt.figure()
plt.plot(mean_trace_tot , label = "Dead Fish")
plt.plot(mean_trace_überlebend , label = "Alive Fish")
plt.xlabel('Frames')
plt.ylabel('Mean fluorescence [a.u.]')
plt.legend()
plt.show()

#Boxplot mine and Lara next to each other
import pandas as pd
import matplotlib.pyplot as plt

death_data_isin = pd.read_csv("A:\\shared\\iyorulmaz\\Isins_Excel_Chart.csv", delimiter=';')
death_data_lara =pd.read_csv("A:\\shared\\iyorulmaz\\from_natalie\\lara_ullmann_recordings\\ketamine_shock_screening_results.csv" , delimiter=';')
group_isin= death_data_isin.groupby("recording")["dead_next_day"].mean()*100
group_lara = death_data_lara.groupby("recording")["dead_next_day"].mean()*100
print(group_isin)
print(group_lara)

plt.boxplot([group_isin, group_lara], tick_labels = ['Isins Data with Ketamin', 'Laras Data with Ketamin'])
plt.title('Mortality rate with Ketamin')
plt.ylabel('Mortality [%]')
plt.show()

#Boxplot Natalies, meine, laras nebeneinander

import pandas as pd
import matplotlib.pyplot as plt

death_data_natalie = pd.read_csv("A:\\shared\\iyorulmaz\\screening_results_von_Natalie.csv", delimiter=';')
death_data_isin = pd.read_csv("A:\\shared\\iyorulmaz\\Isins_Excel_Chart.csv", delimiter=';')
death_data_lara =pd.read_csv("A:\\shared\\iyorulmaz\\from_natalie\\lara_ullmann_recordings\\ketamine_shock_screening_results.csv" , delimiter=';')
group_natalie = death_data_natalie.groupby("recording")["dead_next_day"].mean()*100
group_isin= death_data_isin.groupby("recording")["dead_next_day"].mean()*100
group_lara = death_data_lara.groupby("recording")["dead_next_day"].mean()*100

print(group_natalie)
print(group_isin)
print(group_lara)

plt.boxplot([group_natalie, group_isin, group_lara], tick_labels = ['Control Group (n = 6)', 'Isins Data with Ketamin (n = 11)', 'Laras Data with Ketamin (n = 6)'])
plt.title('Mortality rate')
plt.ylabel('Mortality [%]')
plt.show()

#load multiple fish
import toolboxes.toolbox_nf as nf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import h5py

data_path = "A:\\shared\\iyorulmaz\\Calcium_Imaging_Aufnahmen\\Tiff\\single_fish\\Testordner_python\\"
file_names = ["rec1_5_fish_50Vcm_4s_withketamine_2p5mm_fish1.tif",
             "rec1_5_fish_50Vcm_4s_withketamine_2p5mm_fish3.tif",
             "rec1_5_fish_50Vcm_4s_withketamine_2p5mm_fish4.tif",
             "rec2_5_fish_50Vcm_4s_withketamine_2p5mm_fish1.tif",
             "rec2_5_fish_50Vcm_4s_withketamine_2p5mm_fish2.tif",
              "rec2_5_fish_50Vcm_4s_withketamine_2p5mm_fish3.tif",
              "rec2_5_fish_50Vcm_4s_withketamine_2p5mm_fish4.tif",
              "rec2_5_fish_50Vcm_4s_withketamine_2p5mm_fish5.tif",
              "rec3_5_fish_50Vcm_4s_withketamine_2p5mm_fish1.tif",
              "rec3_5_fish_50Vcm_4s_withketamine_2p5mm_fish2.tif",
              "rec3_5_fish_50Vcm_4s_withketamine_2p5mm_fish3.tif",
              "rec3_5_fish_50Vcm_4s_withketamine_2p5mm_fish5.tif",
              "rec4_5_fish_50Vcm_4s_withketamine_2p5mm_fish1.tif",
              "rec4_5_fish_50Vcm_4s_withketamine_2p5mm_fish1.tif",
              "rec4_5_fish_50Vcm_4s_withketamine_2p5mm_fish2.tif",
              "rec4_5_fish_50Vcm_4s_withketamine_2p5mm_fish4.tif",
              "rec4_5_fish_50Vcm_4s_withketamine_2p5mm_fish5.tif"]

fs = 0.25 #[Hz] [fps] frame per second 900/3600 = 0,25 # sampling frequency # Alle 4 Sekunden ein Bild gemacht
mean_traces = []

for file in file_names:

    rec = nf.read_tif(data_path + file)
    mean_trace = []
    for im in rec:
        mean_trace.append(np.mean(im))

    mean_traces.append(np.array(mean_trace))

t = np.linspace(0, rec.shape[0]/fs,rec.shape[0]) / 60

plt.figure()
for trace, rec in zip(mean_traces, file_names):
    plt.plot(t, trace, label=rec) # fluo-werte gegen zeit
plt.xlabel('time [min]')
plt.ylabel('mean fluorescence [a.u.]') #arbitrary units
plt.legend()
plt.show()

#BULLSHIT
import toolboxes.toolbox_nf as nf
import matplotlib.pyplot as plt
import numpy as np

data_path = "A:\\shared\\iyorulmaz\\Calcium_Imaging_Aufnahmen\\Tiff\\single_fish\\Testordner_python\\"

recordings ={
    "Recording 1": [
        "rec1_5_fish_50Vcm_4s_withketamine_2p5mm_fish1.tif",
        "rec1_5_fish_50Vcm_4s_withketamine_2p5mm_fish3.tif",
        "rec1_5_fish_50Vcm_4s_withketamine_2p5mm_fish4.tif"
    ],

    "Recording 2": [
        "rec2_5_fish_50Vcm_4s_withketamine_2p5mm_fish1.tif",
        "rec2_5_fish_50Vcm_4s_withketamine_2p5mm_fish2.tif",
        "rec2_5_fish_50Vcm_4s_withketamine_2p5mm_fish3.tif",
        "rec2_5_fish_50Vcm_4s_withketamine_2p5mm_fish4.tif",
        "rec2_5_fish_50Vcm_4s_withketamine_2p5mm_fish5.tif"
    ],

    "Recording 3": [
        "rec3_5_fish_50Vcm_4s_withketamine_2p5mm_fish1.tif",
        "rec3_5_fish_50Vcm_4s_withketamine_2p5mm_fish2.tif",
        "rec3_5_fish_50Vcm_4s_withketamine_2p5mm_fish3.tif",
        "rec3_5_fish_50Vcm_4s_withketamine_2p5mm_fish5.tif"
    ],

    "Recording 4": [
        "rec4_5_fish_50Vcm_4s_withketamine_2p5mm_fish1.tif",
        "rec4_5_fish_50Vcm_4s_withketamine_2p5mm_fish2.tif",
        "rec4_5_fish_50Vcm_4s_withketamine_2p5mm_fish4.tif",
        "rec4_5_fish_50Vcm_4s_withketamine_2p5mm_fish5.tif"
    ],
    "Recording 5": [
        "rec5_5_fish_50Vcm_4s_withketamine_2p5mm_fish1.tif",
        "rec5_5_fish_50Vcm_4s_withketamine_2p5mm_fish2.tif",
        "rec5_5_fish_50Vcm_4s_withketamine_2p5mm_fish4.tif",
        "rec5_5_fish_50Vcm_4s_withketamine_2p5mm_fish5.tif"
    ],
    "Recording 6": [
        "rec6_5_fish_50Vcm_4s_withketamine_2p5mm_fish1.tif",
        "rec6_5_fish_50Vcm_4s_withketamine_2p5mm_fish2.tif",
        "rec6_5_fish_50Vcm_4s_withketamine_2p5mm_fish3.tif",
        "rec6_5_fish_50Vcm_4s_withketamine_2p5mm_fish4.tif",
        "rec6_5_fish_50Vcm_4s_withketamine_2p5mm_fish5.tif"
    ],
    "Recording 7": [
        "rec7_5_fish_50Vcm_4s_withketamine_2p5mm_fish1.tif",
        "rec7_5_fish_50Vcm_4s_withketamine_2p5mm_fish2.tif",
        "rec7_5_fish_50Vcm_4s_withketamine_2p5mm_fish3.tif",
        "rec7_5_fish_50Vcm_4s_withketamine_2p5mm_fish4.tif",
        "rec7_5_fish_50Vcm_4s_withketamine_2p5mm_fish5.tif"
    ],
    "Recording 8": [
        "rec8_5_fish_50Vcm_4s_withketamine_2p5mm_fish1.tif",
        "rec8_5_fish_50Vcm_4s_withketamine_2p5mm_fish2.tif",
        "rec8_5_fish_50Vcm_4s_withketamine_2p5mm_fish3.tif",
        "rec8_5_fish_50Vcm_4s_withketamine_2p5mm_fish5.tif"
    ],
    "Recording 9": [
        "rec9_4_fish_50Vcm_4s_withketamine_2p5mm_fish1.tif",
        "rec9_4_fish_50Vcm_4s_withketamine_2p5mm_fish3.tif",
        "rec9_4_fish_50Vcm_4s_withketamine_2p5mm_fish4.tif"
    ],
    "Recording 10": [
        "rec10_5_fish_50Vcm_4s_withketamine_2p5mm_fish3.tif",
        "rec10_5_fish_50Vcm_4s_withketamine_2p5mm_fish4.tif",
        "rec10_5_fish_50Vcm_4s_withketamine_2p5mm_fish5.tif"
    ],
    "Recording 11": [
        "rec11_5_fish_50Vcm_4s_withketamine_2p5mm_fish1.tif",
        "rec11_5_fish_50Vcm_4s_withketamine_2p5mm_fish2.tif",
        "rec11_5_fish_50Vcm_4s_withketamine_2p5mm_fish3.tif"]
}

fs = 0.25

average_traces = {}

for recording, files in recordings.items(): #wird items() verwendet, um alle Schlüssel-Wert-Paare aus einem Wörterbuch abzurufen.

    mean_traces = []
    average_trace = ()

    for file in files:

        rec = nf.read_tif(data_path + file)

        mean_trace = []

        for im in rec:
            mean_trace.append(np.mean(im))

        mean_traces.append(np.array(mean_trace))

    mean_traces = np.array(mean_traces)

    # Average across fish
    average_trace = np.mean(mean_traces, axis=0)

    average_traces[recording] = average_trace
    #print(average_trace)

    #print(recording, mean_traces.shape, average_trace.shape)

# Plot all average recordings
plt.figure()

for recording, trace in average_traces.items():

    t = np.arange(len(trace)) / fs / 60

    plt.plot(t, trace, label=recording)

plt.xlabel("Time [min]")
plt.ylabel("Mean fluorescence [a.u.]")
plt.title("Average fluorescence traces per recording")
plt.legend()
plt.show()

#Mean trace mit und ohne ketamin

#mean trace
#CLOSEUP RECORDING
import toolboxes.toolbox_nf as nf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import h5py

data_path = "A:\\shared\\iyorulmaz\\Calcium_Imaging_Aufnahmen\\Tiff\\"
close_name = "rec12_1_fish_50Vcm_32s_withketamine_2p5mm_closeup.(green).tif"
aufnahme = nf.read_tif(data_path + close_name)

mean_trace = []
for im in aufnahme:
    mean_trace.append(np.mean(im))

plt.figure()
plt.plot(mean_trace)
plt.xlabel('Frames')
plt.ylabel('mean fluorescence [a.u.]')
plt.show()
