from kivy.app import App
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import random
from random import randint
import pandas as pd
import os
import zmq

class MainApp(App):

    def build(self): 
        try:
                    #article images
                    pic1 = Image.open('images/article_photo/pic1.png')
                    pic2 = Image.open('images/article_photo/pic2.png')
                    pic3 = Image.open('images/article_photo/pic3.jpg')
                    pic4 = Image.open('images/article_photo/pic4.jpg')

                    at20 = Image.open('images/attribute2/programmer.png')
                    at21 = Image.open('images/attribute2/istanbul.png')
                    at22 = Image.open('images/attribute2/london.png')
                    at23 = Image.open('images/attribute2/unknown.png')


                    #Stationary Elements
                    background = Image.open('images/stationary_pieces/background.png')


                    # # Loop to read in logo files and programmatically assign objects 
                    #Logo Paths 
                    path = 'images\logos'

                    files = []
                    # r=root, d=directories, f = files
                    for r, d, f in os.walk(path):
                        for file in f:
                            if '.png' in file:
                                files.append(os.path.join(r, file))

                    #Grabbing the files names
                    logo_names = files
                    logo_names = [s.replace('images\logos\\', '').replace('Algeria\\', '').replace('.png','').replace('Arab\\', '').replace('Egypt\\', '').replace('Iraq\\', '') for s in logo_names]
                    logo_names = [s.replace('Jordan\\', '').replace('Kuwait\\', '').replace('Lebanon\\', '').replace('Morocco\\', '').replace('Libya\\', '').replace('Palestine\\', '') for s in logo_names]
                    logo_names = [s.replace('Yemen\\', '').replace('Sudan\\', '').replace('Tunisia\\', '').replace('Mauritania\\', '') for s in logo_names]

                    #Pulling the images with lambda function 
                    image_loader = lambda x: Image.open(x)
                    logo_images = list(map(image_loader, files))

                    # using dictionary comprehension 
                    # to join together lists 
                    logo_dict = {logo_names[i]: logo_images[i] for i in range(len(logo_names))} 

                    at30 = Image.open('images/attribute34/at30.png')
                    at31 = Image.open('images/attribute34/at31.png')
                    at32 = Image.open('images/attribute34/at32.png')
                    at33 = Image.open('images/attribute34/at33.png')
                    at34 = Image.open('images/attribute34/at34.png')
                    at35 = Image.open('images/attribute34/at35.png')
                    at36 = Image.open('images/attribute34/at36.png')
                    at37 = Image.open('images/attribute34/at37.png')
                    at38 = Image.open('images/attribute34/at38.png')
                    at39 = Image.open('images/attribute34/at39.png')
                    at310 = Image.open('images/attribute34/at310.png')
                    at311 = Image.open('images/attribute34/at311.png')
                    at312= Image.open('images/attribute34/at312.png')
                    at313 = Image.open('images/attribute34/at313.png')
                    at314 = Image.open('images/attribute34/at314.png')
                    at315 = Image.open('images/attribute34/at315.png')


                    # # Create lists of elements 


                    article_images = []
                    article_images.append(pic1)
                    article_images.append(pic2)
                    article_images.append(pic3)
                    article_images.append(pic4)

                    attribute2s = []
                    attribute2s.append(at20)
                    attribute2s.append(at21)
                    attribute2s.append(at22)
                    attribute2s.append(at23)

                    attributes3and4 = []
                    attributes3and4.append(at30)
                    attributes3and4.append(at31)
                    attributes3and4.append(at32)
                    attributes3and4.append(at33)
                    attributes3and4.append(at34)
                    attributes3and4.append(at35)
                    attributes3and4.append(at36)
                    attributes3and4.append(at37)
                    attributes3and4.append(at38)
                    attributes3and4.append(at39)
                    attributes3and4.append(at310)
                    attributes3and4.append(at311)
                    attributes3and4.append(at312)
                    attributes3and4.append(at313)
                    attributes3and4.append(at314)
                    attributes3and4.append(at315)

                    likes = []
                    likes.append('3')
                    likes.append('102')
                    likes.append('1.1k')
                    likes.append('10.2k')

                    angries = []
                    angries.append('7')
                    angries.append('103')
                    angries.append('1.2')
                    angries.append('10.1k')

                    comments = []
                    comments.append('5')
                    comments.append('97')
                    comments.append('1.5k')
                    comments.append('9.8k')

                    shares = []
                    shares.append('1')
                    shares.append('110')
                    shares.append('1.1k')
                    shares.append('9.2k')




                    # # Randomization and pasting together 

                    # Create random number to select the element from the list and a random 6 digit number for the survey ids 
                    sid = randint(100000, 999999)
                    logo_random = random.randint(0,225)
                    article_image_random = random.randint(0,3)
                    attribute2_random = random.randint(0,3)
                    attribute3and4_random = random.randint(0,15)
                    likes_random =random.randint(0,3)
                    angries_random =random.randint(0,3)
                    comments_random =random.randint(0,3)
                    shares_random =random.randint(0,3)


                    #Create a string based on the element that was selected that will be included in the data frame
                    logo_name = (list(logo_dict.keys())[logo_random])

                    article_image_name = ('pic1' if (article_image_random == 0) else
                                            'pic2' if (article_image_random == 1) else
                                            'pic3' if (article_image_random == 2) else
                                            'pic4' if (article_image_random == 3) else
                                            'error' 
                     )

                    attribute2_name = ('unnamed capital' if (attribute2_random == 0) else
                                            'Instanbul' if (attribute2_random == 1) else
                                            'London' if (attribute2_random == 2) else
                                            'Not specified' if (attribute2_random == 3) else
                                            'error'
                     )

                    attribute3_name = ('Government official' if (attribute3and4_random == 0) else
                                            'Government official' if (attribute3and4_random == 1) else
                                            'Government official' if (attribute3and4_random == 2) else
                                            'Government official' if (attribute3and4_random == 3) else
                                            'Religious leader' if (attribute3and4_random == 4) else
                                            'Religious leader' if (attribute3and4_random == 5) else
                                            'Religious leader' if (attribute3and4_random == 6) else
                                            'Religious leader' if (attribute3and4_random == 7) else
                                            'Professor' if (attribute3and4_random == 8) else
                                            'Professor' if (attribute3and4_random == 9) else
                                            'Professor' if (attribute3and4_random == 10) else
                                            'Professor' if (attribute3and4_random == 11) else
                                            'Report' if (attribute3and4_random == 12) else
                                            'Report' if (attribute3and4_random == 13) else
                                            'Report' if (attribute3and4_random == 14) else
                                            'Report' if (attribute3and4_random == 15) else
                                            'error'
                     )

                    attribute4_name = ('animal2human' if (attribute3and4_random == 0) else
                                            'research lab' if (attribute3and4_random == 1) else
                                            'corporations' if (attribute3and4_random == 2) else
                                            'God' if (attribute3and4_random == 3) else
                                            'animal2human' if (attribute3and4_random == 4) else
                                            'research lab' if (attribute3and4_random == 5) else
                                            'corporations' if (attribute3and4_random == 6) else
                                            'God' if (attribute3and4_random == 7) else
                                            'animal2human' if (attribute3and4_random == 8) else
                                            'research lab' if (attribute3and4_random == 9) else
                                            'corporations' if (attribute3and4_random == 10) else
                                            'God' if (attribute3and4_random == 11) else
                                            'animal2human' if (attribute3and4_random == 12) else
                                            'research lab' if (attribute3and4_random == 13) else
                                            'corporations' if (attribute3and4_random == 14) else
                                            'God' if (attribute3and4_random == 15) else
                                            'error'
                     )

                    like_number = ('3' if (likes_random == 0) else
                                            '102' if (likes_random == 1) else
                                            '1100' if (likes_random == 2) else
                                            '10200' if (likes_random == 3) else
                                            'error'
                     )

                    angry_number = ('7' if (angries_random == 0) else
                                            '103' if (angries_random == 1) else
                                            '1200' if (angries_random == 2) else
                                            '10100' if (angries_random == 3) else
                                            'error'
                     )

                    comment_number = ('5' if (comments_random == 0) else
                                            '97' if (comments_random == 1) else
                                            '1500' if (comments_random == 2) else
                                            '9800' if (comments_random == 3) else
                                            'error'
                     )

                    share_number = ('1' if (shares_random == 0) else
                                            '110' if (shares_random == 1) else
                                            '1100' if (shares_random == 2) else
                                            '9200' if (shares_random == 3) else
                                            'error'
                     )


                    #Create a data frame to save the results
                    elements_data = {'Survey_ID': [sid],
                                     'Logo': [logo_name],
                                     'Article_Image': [article_image_name],
                                     'Author_Location': [attribute2_name],
                                     'Source' : [attribute3_name],
                                     'Subject' : [attribute4_name],
                                     'Likes' : [like_number],
                                     'Angries': [angry_number],
                                     'Comments': [comment_number],
                                     'Shares': [share_number]
                                    }

                    elements_data = pd.DataFrame(elements_data, columns = ['Survey_ID', 'Logo', 'Article_Image','Author_Location', 'Source', 'Subject', 'Likes', 'Angries', 'Comments', 'Shares'])

                   #Creating a copy of blank background so it is not altered
                    image = background.copy()

                    #Pasting together elements by coordinate
                    logo = list(logo_dict.values())[logo_random]
                    image.paste(logo, (15, 10))

                    article_image = article_images[article_image_random]
                    article_image = article_image.resize((625,325), Image.ANTIALIAS)
                    image.paste(article_image, (4, 120))

                    at2_image = attribute2s[attribute2_random]
                    at2_image = at2_image.resize((610,50), Image.ANTIALIAS)
                    image.paste(at2_image, (15,70))

                    at3_image = attributes3and4[attribute3and4_random]
                    at3_image = at3_image.resize((610,55), Image.ANTIALIAS)
                    image.paste(at3_image, (15, 470))

                    #Pasting text
                    draw = ImageDraw.Draw(image)

                    #font 
                    # use a truetype font
                    font = ImageFont.truetype("data/segoe-ui-regular-arabic.ttf", 16, encoding='unic')
                    like = likes[likes_random]
                    draw.text((588, 555), like, (96, 103, 112), font=font)

                    angry = angries[angries_random]
                    draw.text((510, 555), angry, (96, 103, 112), font=font)

                    font = ImageFont.truetype("data/segoe-ui.ttf", 16, encoding='unic')
                    comment = comments[comments_random]
                    draw.text((135, 557), comment, (96, 103, 112), font=font)

                    share = shares[shares_random]
                    draw.text((65, 557), share, (96, 103, 112), font=font)


                    #Savings Images and Elements CSV
                    image.save('facebook_post.png')
                    elements_data.to_csv('elements_data.csv', index=False)

        except IOError: 
            pass

if __name__ == "__main__": 
    app = MainApp()
    app.run() 



