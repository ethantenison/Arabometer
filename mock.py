import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg 
from PIL import Image, ImageDraw, ImageFilter
import random
from random import randint
import pandas as pd

def main(): 
    try:
        alarabiya = Image.open('./images/alarabiya.png') 
        lbc = Image.open('./images/lbc.png') 
        tele = Image.open('./images/tele_liban.png')
        future = Image.open('./images/future_tv.png') 
        aljadeed = Image.open('./images/aljadeed.png') 
        cover_ala = Image.open('./images/coverphoto_alarabiya.png')
        blank = Image.open('./images/blank.png')

        list = []
        list.append(alarabiya)
        list.append(aljadeed)
        list.append(future)
        list.append(lbc)
        list.append(tele)

       # Create random number to select the element from the list and a random 6 digit number for the survey ids 
        logo_random = random.randint(0,4)
        sid = randint(100000, 999999)

        #Create a string based on the element that was selected that will be included in the data frame
        logo_name = ('Al Arabiya' if (logo_random == 0) else
                      'Al Jadeed' if (logo_random == 1) else
                      'Future' if (logo_random == 2) else
                      'LBC' if (logo_random == 3) else
                      'Tele Liban'
         )

        #Create a data frame to save the results
        elements_data = {'Survey_ID': [sid],
                         'Logo': [logo_name]
                        }

        elements_data = pd.DataFrame(elements_data, columns = ['Survey_ID', 'Logo'])

        #Creating a copy of blank background so it is not altered
        back_im = blank.copy()

        #Pasting together elements by coordinates
        back_im.paste(list[logo_random], (1000, 50))
        back_im.paste(cover_ala, (100, 50))

        #Savings Images and Elements CSV
        back_im.save('mock.png')
        elements_data.to_csv('elements_data.csv')
        
    except IOError: 
        pass
        
if __name__ == "__main__": 
    main() 
