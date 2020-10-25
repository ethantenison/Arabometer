# Arab Barometer - COVID Survey App 


<br />

This project was conducted in conjunction with Princeton University's Arab Barometer and Statistical Netherlands. 
Originally designed to capture public opinion about fake news in the Middle East, the survey objective goals were changed dramatically as a result of COVID-19. 
My portion of the project entailed creating an application to create randomized Facebook images to use during the survey. Each time enumerators give the survey
a different image is displayed with randomized elements including title, author, location, and message. Those variables are then stored in a csv that will be saved along with 
the respondents survey answers. 
<br />


![Example of Randomized Image](facebook_post.png)
<br />

Two apps were created, one for Windows and one for Android. Virtual environments were used throughout the project. For Windows, the package Pyinstaller was used to convert prototype4.py to prototype4.exe. 
Once compiled, the exe file is automatically stored in the dist folder. 
<br />

The apk compilation process for Android was more complicated. First, prototype4.py was modified in order to create a Kivy app. 
Naming conventions for Kivy require the python file to be named main.py. The styling file is labeled main.kv, which has been left blank. 
It is not possible to convert Python scripts to apk in Windows, so a linux virtual machine was created using [Digital Ocean](https://www.digitalocean.com). 
After setting up the virtual environment, buildozer was used to convert the necessary files to apk. 
