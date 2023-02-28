# plot_projs_topomap

Brainlife App to plot projectors in raw file using MNE-Python [raw.plot_projs_topomap](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.plot_projs_topomap).

# Documentation

#### Input files are:
* a MEG file in fif format (mne/raw).

#### Input parameters are:
* ` ch_type `:  ‘mag’ | ‘grad’ | ‘planar1’ | ‘planar2’ | ‘eeg’ | None | list ,  The channel type to plot. For 'grad', the gradiometers are collected in pairs and the RMS for each pair is plotted. If None it will return all channel types present.. If a list of ch_types is provided, it will return multiple figures. Defaults to None. 
* ` sensors `:  bool | str ,  Whether to add markers for sensor locations. If str, should be a valid matplotlib format string (e.g., 'r+' for red plusses, see the Notes section of plot()). If True (the default), black circles will be used. 
* ` show_names `:  bool | callable() ,  If True, show channel names next to each sensor marker. If callable, channel names will be formatted using the callable; e.g., to delete the prefix ‘MEG ‘ from all channel names, pass the function lambda x: x.replace('MEG ', ''). If mask is not None, only non-masked sensor names will be shown. 
* ` contours `:  int | array_like ,  The number of contour lines to draw. If 0, no contours will be drawn. If a positive integer, that number of contour levels are chosen using the matplotlib tick locator (may sometimes be inaccurate, use array for accuracy). If array-like, the array values are used as the contour levels. The values should be in µV for EEG, fT for magnetometers and fT/m for gradiometers. If colorbar=True, the colorbar will have ticks corresponding to the contour levels. Default is 6. 
* ` outlines `:  ‘head’ | dict | None ,  The outlines to be drawn. If ‘head’, the default head scheme will be drawn. If dict, each key refers to a tuple of x and y positions, the values in ‘mask_pos’ will serve as image mask. Alternatively, a matplotlib patch object can be passed for advanced masking options, either directly or as a function that returns patches (required for multi-axis plots). If None, nothing will be drawn. Defaults to ‘head’. 
* ` sphere `:  float | array_like | instance of ConductorModel | None | ‘auto’ | ‘eeglab’ ,  The sphere parameters to use for the head outline. Can be array-like of shape (4,) to give the X/Y/Z origin and radius in meters, or a single float to give just the radius (origin assumed 0, 0, 0). Can also be an instance of a spherical ConductorModel to use the origin and radius from that object. If 'auto' the sphere is fit to digitization points. If 'eeglab' the head circle is defined by EEG electrodes 'Fpz', 'Oz', 'T7', and 'T8' (if 'Fpz' is not present, it will be approximated from the coordinates of 'Oz'). None (the default) is equivalent to 'auto' when enough extra digitization points are available, and (0, 0, 0, 0.095) otherwise. 
* ` extrapolate `:  str ,  Options:
    'box'
        Extrapolate to four points placed to form a square encompassing all data points, where each side of the square is three times the range of the data in the respective dimension.
    'local' (default for MEG sensors)
        Extrapolate only to nearby points (approximately to points closer than median inter-electrode distance). This will also set the mask to be polygonal based on the convex hull of the sensors.
    'head' (default for non-MEG sensors)
        Extrapolate out to the edges of the clipping circle. This will be on the head circle when the sensors are contained within the head circle, but it can extend beyond the head when sensors are plotted outside the head circle.
    The default was changed to 'local' for MEG sensors.
    'local' was changed to use a convex hull mask
    'head' was changed to extrapolate out to the clipping circle. 
* ` border `:  float | ‘mean’ ,  Value to extrapolate to on the topomap borders. If 'mean' (default), then each extrapolated point has the average value of its neighbours. 
* ` res `:  int ,  The resolution of the topomap image (number of pixels along each side). 
* ` cmap `:  matplotlib colormap | (colormap, bool) | ‘interactive’ | None ,  Colormap to use. If tuple, the first value indicates the colormap to use and the second value is a boolean defining interactivity. In interactive mode the colors are adjustable by clicking and dragging the colorbar with left and right mouse button. Left mouse button moves the scale up and down and right mouse button adjusts the range. Hitting space bar resets the range. Up and down arrows can be used to change the colormap. If None, 'Reds' is used for data that is either all-positive or all-negative, and 'RdBu_r' is used otherwise. 'interactive' is equivalent to (None, True). Defaults to None.
Warning
Interactive mode works smoothly only for a small amount of topomaps. Interactive mode is disabled by default for more than 2 topomaps. 
* ` vlim `:  tuple of length 2 | ‘joint’ ,  Colormap limits to use. If a tuple of floats, specifies the lower and upper bounds of the colormap (in that order); providing None for either entry will set the corresponding boundary at the min/max of the data (separately for each projector). Elements of the tuple may also be callable functions which take in a NumPy array and return a scalar. If vlim='joint', will compute the colormap limits jointly across all projectors of the same channel type, using the min/max of the data for that channel type. If vlim is 'joint', info must not be None. Defaults to (None, None). 
* ` colorbar `:  bool ,  Plot a colorbar in the rightmost column of the figure. 
* ` cbar_fmt `:  str ,  Formatting string for colorbar tick labels. See Format Specification Mini-Language for details. 
* ` units `:  str | None ,  The units to use for the colorbar label. Ignored if colorbar=False. If None the label will be “AU” indicating arbitrary units. Default is None. 

#### Ouput files are:
* a figure
   

## Authors
- [Maximilien Chaumon](maximilien.chaumon@icm-institute.org)

### Funding Acknowledgement
brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your code and publications. Copy and past the following lines into your repository when using this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)

### Citations
1. Avesani, P., McPherson, B., Hayashi, S. et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). [https://doi.org/10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

