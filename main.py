import os
import numpy as np
import mne
import json
import helper
from mne_bids.write import _events_tsv
import shutil
import re

#workaround for -- _tkinter.TclError: invalid command name ".!canvas"
# import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt

with open('config.json') as config_json:
    config = helper.convert_parameters_to_None(json.load(config_json))


data_file = config['mne']

raw = mne.io.read_raw_fif(data_file,verbose=False)

raw.plot_projs_topomap(ch_type=config['ch_type'],
sensors=config['sensors'],
show_names=config['show_names'],
contours=config['contours'],
outlines=config['outlines'],
sphere=config['sphere'],
image_interp=config['image_interp'],
extrapolate=config['extrapolate'],
border=config['border'],
res=config['res'],
size=config['size'],
cmap=config['cmap'],
vlim=config['vlim'],
cnorm=config['cnorm'],
colorbar=config['colorbar'],
cbar_fmt=config['cbar_fmt'],
units=config['units'])


