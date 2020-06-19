import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg 
from PIL import Image, ImageDraw, ImageFilter
import random


alarabiya = Image.open('images/alarabiya.png') 
lbc = Image.open('images/lbc.png') 
tele = Image.open('images/tele_liban.png')
future = Image.open('images/future_tv.png') 
aljadeed = Image.open('images/aljadeed.png') 
cover_ala = Image.open('images/coverphoto_alarabiya.png')
blank = Image.open('images/blank.png')

list = []
list.append(alarabiya)
list.append(aljadeed)
list.append(future)
list.append(lbc)
list.append(tele)

logo_random = random.randint(0,4)
back_im = blank.copy()
back_im.paste(list[logo_random], (1000, 50))
back_im.paste(cover_ala, (100, 50))
back_im

