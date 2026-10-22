import toolboxes.toolbox_nf as nf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import h5py

#%%

data_path = "A:\\shared\\iyorulmaz\\Calcium-imaging Aufnahmen\\Tiff\\single_fish\\"

file_name = "rec1_5_fish_50Vcm_4s_withketamine_2p5mm_fish_5.tif"

# load single fish

rec = nf.read_tif(data_path + file_name)    #

mean_trace = np.zeros((900, 1))

for i in range(rec.shape[0]):
    mean_trace[i] = np.mean(rec[i])

fig, axs = plt.subplots()
axs.plot(mean_trace)
plt.show()

plt.savefig("A:\\shared\\iyorulmaz\\figures\\test.png", dpi=300)

death_data = pd.read_csv("A:\\shared\\iyorulmaz\\screening_results.csv", delimiter=';')


