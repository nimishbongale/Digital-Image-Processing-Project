# -*- coding: utf-8 -*-
"""octavemagic_extension.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gKkzdaVQHmGNAQhh0IXG_LO4Mmk9vooC

# Coffee Bean Health Detection using Ocatve in ipynb.

## Installation
"""

!apt-get update
!apt install octave

# Commented out IPython magic to ensure Python compatibility.
!apt-get install liboctave-dev
!pip install oct2py
# %reload_ext oct2py.ipython

# Commented out IPython magic to ensure Python compatibility.
# %%octave
# pkg install -forge image
# pkg load image

"""## Overview

When using the cell magic, `%%octave` (note the double `%`), multiple lines of Octave can be executed together.  Unlike
with the single cell magic, no value is returned, so we use the `-i` and `-o` flags to specify input and output variables.  Also note the use of the semicolon to suppress the Octave output.

## Imaging

Image output is automatically captured and displayed, and using the `-f` flag you may choose its format (currently, `png` and `svg` are supported).

The width or the height can be specified to constrain the image while maintaining the original aspect ratio.

Multiple figures can be drawn.  Note that when using imshow the image will be created as a PNG with the raw
image dimensions.

Plots can be drawn inline (default) or bring up the Octave plotting GUI by using the -g (or --gui) flag:
"""

import requests

img_data = requests.get('https://i.ibb.co/hd7gxky/IMG-5694.jpg').content
with open('coffee.jpg', 'wb') as handler:
    handler.write(img_data)

from google.colab import drive
drive.mount('/content/gdrive')

!cd gdrive

!ls

# Commented out IPython magic to ensure Python compatibility.
# %%octave -s 1200,400 -f png
# a = imshow('coffee.jpg')

# Commented out IPython magic to ensure Python compatibility.
# %%octave -s 600,200 -f png
# bw_img = rgb2gray(imread('coffee.jpg'));
# figure
# imshow(bw_img)

# Commented out IPython magic to ensure Python compatibility.
# %%octave -s 600,200 -f png
# bin_img = imclearborder(imcomplement(im2bw(rgb2gray(imread('coffee.jpg')),0.5)));
# figure
# imshow(bin_img)

# Commented out IPython magic to ensure Python compatibility.
# %%octave
#  I = max (phantom (), 0);
#  figure; imshow (bw_img);
#  title ("Original image");
#  h = imhist (bw_img);
#  t = otsuthresh (h);
#  J = im2bw (imsmooth(bw_img, "Gaussian"));
#  figure; imshow (J);
#  title_line = sprintf ("Black and white image after thresholding, t=%g",
#                        t*255);
#  title (title_line);

# Commented out IPython magic to ensure Python compatibility.
# %%octave -s 600,200 -f png
# new_bin_img = imclearborder(imcomplement(J));
# figure
# imshow(new_bin_img)

# Commented out IPython magic to ensure Python compatibility.
# %%octave
# thresharea = bwarea(bin_img)
# 
# otsuarea = bwarea(new_bin_img)

# Commented out IPython magic to ensure Python compatibility.
# %%octave
# c = [1,12,146,410];
# r = [1,104,156,129];
# pixels = impixel(imread('coffee.jpg'),c,r)
# for i = 1:rows(pixels)
# disp(pixels(i,1)+pixels(i,2)+pixels(i,3))
# endfor

# Commented out IPython magic to ensure Python compatibility.
# %%octave -s 600,200 -f png
# dil_img = imdilate(imdilate(imdilate(bin_img,[1,1,1]),[1,1,1]),[1,1,1]);
# figure
# imshow(dil_img)

# Commented out IPython magic to ensure Python compatibility.
# %%octave -s 600,200 -f png
# erod_img = imerode(dil_img,[1,1,1]);
# figure
# imshow(erod_img)

# Commented out IPython magic to ensure Python compatibility.
# %%octave -s 600,200 -f png
# imshow(dil_img-erod_img)

# Commented out IPython magic to ensure Python compatibility.
# %%octave
# whos a

# Commented out IPython magic to ensure Python compatibility.
# %%octave
# t=imshow(edge(bw_img, "Sobel"))

# Commented out IPython magic to ensure Python compatibility.
# %%octave
# t=imshow(edge(bw_img, "Roberts"))

# Commented out IPython magic to ensure Python compatibility.
# %%octave
# t=imshow(edge(bw_img, "Prewitt"))

# Commented out IPython magic to ensure Python compatibility.
# %%octave
# k=imhist(g)
# length(k)

!sudo apt-get install octave-image

# Commented out IPython magic to ensure Python compatibility.
# %%octave
# pkg load image
# pkg list

# Commented out IPython magic to ensure Python compatibility.
# %%octave
#  BW = imnoise (g, "salt & pepper");
#  figure ();
#  imshow (BW);
#  title ("BW");
#  [H, theta, rho] = hough (BW);
#  H /= max (H(:));
#  figure ();
#  imshow (H, "XData", theta, "YData", rho);
#  title ("hough transform of BW");
#  axis on;
#  xlabel ("angle \\theta [degrees]");
#  ylabel ("distance \\rho to origin [pixels]");

!pip install fastai

!ls

from google.colab import drive
drive.mount('/content/drive')

from fastai.vision import *

path = Path('/content/drive/My Drive/DIP')

folder = ['super_inferior_batch', 'inferior_batch', 'mediocre_batch', 'superior_batch', 'super_superior_batch']
files = [x + '-coffee.csv' for x in folder]

ls

cd drive

cd My\ Drive

cd DIP

ls

for x in folder:
  path1 = Path('./')
  dest = path1/x
  dest.mkdir(parents=True, exist_ok=True)

classes =  ['super_inferior_batch', 'inferior_batch', 'mediocre_batch', 'superior_batch', 'super_superior_batch']

np.random.seed(42)
data = ImageDataBunch.from_folder(path, train=".", valid_pct=0.2,
        ds_tfms=get_transforms(), size=150, num_workers=4).normalize(imagenet_stats)

data.classes

data.show_batch(rows=3, figsize=(7,8))

learn = cnn_learner(data, models.resnet50, metrics=error_rate)

learn.fit_one_cycle(4)

learn.fit_one_cycle(5, max_lr=slice(1e-4,1e-3))

interp = ClassificationInterpretation.from_learner(learn)

interp.plot_confusion_matrix()