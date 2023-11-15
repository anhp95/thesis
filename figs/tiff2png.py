#%%
from PIL import Image, ImageSequence
import os
import os.path
import glob

def tiff_2_png(folder):

    files = glob.glob(f"{folder}/*.tiff")

    for file in files:
        
        im = Image.open(file)
        im.save(file.replace("tiff", "png"), dpi=(600, 600))
# %%
