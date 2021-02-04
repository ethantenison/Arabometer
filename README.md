# Arab Barometer - COVID Survey App 


<br />

This project was conducted in conjunction with Princeton University's Arab Barometer and Statistics Netherlands. 
Originally designed to capture public opinion about fake news in the Middle East, the survey objective goals were changed dramatically as a result of COVID-19. 
This portion of the project entailed creating an application to create randomized Facebook images to use during a survey. Each time enumerators give the survey,
a different image is displayed with randomized elements including title, author, location, article introduction, and number of likes. Those variables are then stored in a csv that will be saved along with 
the respondents survey answers. 
<br />


![Example of Randomized Image](facebook_post.png)
<br />
### How was it created? 
Two apps were created, one for Windows and one for Android. Virtual environments were used throughout the project to minimize the file size and speed up the execution process. 
For Windows, the package Pyinstaller was used to convert prototype4.py to prototype4.exe. In order to compile the program use the commands **pipenv run pyinstaller --onefile --debug=imports -w prototype4.py**
Once compiled, the exe file is automatically stored in the dist folder. Note, in order for the executable to work the images and data folder must be present in the same directory as the exe file.  
<br />

The apk compilation process for Android was more complicated. First, prototype4.py was modified in order to create a Kivy app. 
Naming conventions for Kivy require the python file be named main.py. The styling file is labeled main.kv, which has been left blank but is required for the compilation process. 
Because I used a windows machine, I had to create a linux virtual machine with [Digital Ocean](https://www.digitalocean.com). After setting up the virtual environment, buildozer was used to convert the necessary files to apk. 
For a tutorial on how to convert main.py and main.kv to an apk you can check out the tutorial [here](https://www.youtube.com/watch?v=kcte8vcGMSU). 
Just as with the windows application, the images and data folders must be in the same directory as the apk file for it to work.  
<br />



### What should be the results? 
After the prototype6.apk or prototype4.exe are initialized, they will create two outputs to be used by Blaise, elements_data.csv and facebook_post.png. The image will be displayed during survey administration and the csv will be saved along with the survey responses. 

