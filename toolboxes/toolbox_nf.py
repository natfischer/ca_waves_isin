__author__ = "nfischer"
# %% importing
import numpy as np
import matplotlib as mpl
mpl.use("TkAgg")
import matplotlib.pyplot as plt
import os
import pandas as pd
import h5py
import scipy
from skimage import io
import upsetplot as upset

# function for saving data as HDF5 (stolen from David)
def save_hdf5(list_of_data_arrays, list_of_labels, new_directory: str, export_path: str, permission='a'):
  print('save data to ' + export_path)
  permission = permission
  with h5py.File(export_path, permission) as f:
      gr = f.create_group(new_directory)
      for i in range(len(list_of_data_arrays)):
          gr[list_of_labels[i]] = list_of_data_arrays[i]

# function to load an HDF5 file (stolen from David)
def load_hdf5(import_path: str):
  print('load from HDF5...')
  data_dict = {}
  f = h5py.File(import_path, 'r')
  for group in f.keys():
      print(group)
      data_dict[group] = {}
      for dset in f[group].keys():
          if group == "waves":
              data_dict[group][dset] = {}
              for ddset in f[group][dset].keys():
                  data_dict[group][dset][ddset] = f[group][dset][ddset][()]
          else:
              data_dict[group][dset] = f[group][dset][()]
  f.close()
  return data_dict

# load tif files
def read_tif(path: str):
  print("load tiff: " + path)
  img = io.imread(path)
  return np.array(img)


