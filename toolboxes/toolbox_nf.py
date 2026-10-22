__author__ = "nfischer"
# %% importing
import numpy as np
import matplotlib as mpl
mpl.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as grid
import matplotlib.patches as mpatches
import seaborn as sns
import math
import re
import copy
import ast
import os
import pandas as pd
import h5py
import colorcet as cc
import warnings
import scipy
import skimage
import toolboxes.epi_slowwave_toolbox as epi
from PIL import Image
from scipy import ndimage, signal
from scipy.signal import wiener, vectorstrength, find_peaks
from scipy.stats import circstd, circvar, linregress, kruskal, mannwhitneyu, false_discovery_control
from scipy.optimize import curve_fit
from matplotlib.patches import FancyArrowPatch
from skimage import morphology, measure, filters, io
from mpl_toolkits.axes_grid1 import make_axes_locatable
from statsmodels.stats.proportion import proportions_ztest, proportion_effectsize
from colorama import Fore
from collections import OrderedDict
import upsetplot as upset


# function for saving data as HDF5 (stolen from David)
def save_hdf5(self, list_of_data_arrays, list_of_labels, new_directory: str, export_path: str, permission='a'):
  print('save data to ' + export_path)
  permission = permission
  with h5py.File(export_path, permission) as f:
      gr = f.create_group(new_directory)
      for i in range(len(list_of_data_arrays)):
          gr[list_of_labels[i]] = list_of_data_arrays[i]

# function to load an HDF5 file (stolen from David)
def load_hdf5(self, import_path: str):
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
def read_tif(self, path: str):
  print("load tiff: " + path)
  img = io.imread(path)
  return np.array(img)


