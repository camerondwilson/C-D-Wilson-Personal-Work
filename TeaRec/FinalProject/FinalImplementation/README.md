# LMSC-261-ProblemSets
### Project Name

Final Project-Tea Recommendation System

### Submitted by

Cameron Wilson

### For Course

LMSC-261

### Due Date

01:13:00 AM on 5/05/2021

### Submission Date

3:59:00 PM on 5/05/2021

### Files Included

        _pycache_
        - app.cpython-39.pyc

        Static
            Styles
            - res.css
            - style.min.css
        - black.jpg
        - chai.jpg
        - chamomile.jpg
        - ginger.jpg
        - green.jpg
        - hibiscus.jpg
        - matcha. jpg
        - mint.jpg
        - oolong.jpg
        - rooibos. jpg
        - white.jpg

        templates
            Group_1_Flowers
            - 1.1fl_ne.html
            - 1.2fl_sto.html
            - 1.3fl_co.html
            - 1.4fl_bp.html
            - 1.5fl_w.html
            Group_2_Sweet
            - 2.1swe_ne.html
            - 2.2swe_sto.html
            - 2.3swe_co.html
            - 2.4swe_bp.html
            - 2.5swe_w.html
            Group_3_Herbal
            - 3.1herb_ne.html
            - 3.2herb_sto.html
            - 3.3herb_co.html
            - 3.4herb_bp.html
            - 3.5herb_w.html
            Group_4_Spicy
            - 4.1spi_ne.html
            - 4.2spi_sto.html
            - 4.3spi_co.html
            - 4.4spi_bp.html
            - 4.5spi_w.html
            Group_5_Earthy
            - 5.1ear_ne.html
            - 5.2ear_sto.html
            - 5.3ear_co.html
            - 5.4ear_bp.html
            - 5.5ear_w.html
            Group_6_Fruity
            - 4.1fru_ne.html
            - 4.2fru_sto.html
            - 4.3fru_co.html
            - 4.4fru_bp.html
            - 4.5fru_w.html
        - error.html
        - index.html
        - layout.html
        - list.html
    - app.py
    - list.csv
    - README.md

### Purpose

The purpose of this was to implement all lessons and skills obtained this semester into a personal project. 

### Description

#### Create and activate virtual environment (Python 3.4 and above):
   
 Windows:
- To run 'FinalImplementation,' user might have to create a virtual environment. To do so, create a project folder and a venv folder within said folder, then type '$ python -m venv [directory]' into the terminal.' From there, in order to activate the environment, 'C:\> env\Scripts\activate.bat' must be typed into the terminal. If the user is in wrong directory, user will have to use the 'cd ..' and 'cd .' commands to find the right directory. 

Mac:
 - To run 'FinalImplementation,' user might have to create a virtual environment. To do so, create a project folder and a venv folder within said folder, then type '$ python -m venv [directory]' into the terminal.' From there, in order to activate the environment, '$ source myvenv/bin/activate' must be typed into the terminal. If the user is in wrong directory, user will have to use the 'cd ..' and 'cd .' commands to find the right directory. 



#### Install flask:
    
Windows and Mac:
- Once user establishes if they need a virtual envirnoment or not, user must ensure that they have Flask on their computer. If they do not, they must type in '$ pip install Flask'. From there, they will only need to type 'flask run'.
- User should then see this link, 'http://127.0.0.1:5000'. Click on it, and the cite will be opened on Chrome.

The following is a user manual. The user manual is meant to help the user navigate and understand the cite. It is imperative that the user is able to use Flask when using this recommendation system. If the user does not have Flask, instructions on how to install and activate are above. User might need to utilize a virtual environment, more on that can be found above. This cite is generally self-explanable though. It is a tea recommendation system meant to recommend a certain type depending on certain criteria. Once the user enters in their name, they will be able to choose one option from each drop-down lists, there are 2 in total. If the user fails to fill in all fields, an error message will appear. If the user fills in all fields, they will be redirected to a recommendation page. Here they will find their recommendations! Along with name and descriptions, the user will also have the choice to purchase a certain tea, restart the system, or simply close it out. By clicking on the image, they will be redirected 'https://www.teaforte.com/', where they can purchase said tea. If they instead click on the 'restart' button, they will be redirected back to the home page. They can use the system as many times as they would like and may close it out whenever they would like. All answers, included name, are recorded into list.csv. 

#### User Manual:
1. Within VSCode, user must type "flask run" into terminal.
2. Ctrl+Click 'http://127.0.0.1:5000'
3. Cite will open up in Chrome.
4. User fills in given fields.
5. If name is not filled out->Error message will pop up.
6. If at least 1 preference is not selected from the drop-downs->Error message will pop up.
7. If all fields are filled out, the corresponding recommended page will appear.
8. User's data will automatically be stored in list.csv.
9. User will have the choice to click restart, click on the embedded link (within the image), or do nothing.
10. If user clicks on the 'restart' button, steps 1-6 will repeat.
11. If user clicks on the link, a new tab open on purchasing website->https://www.teaforte.com/
12. If user does nothing, nothing will happen. 
13. To close out of the program in VSCode, simply type 'Crtl+C'.

### Build and Run Commands (If applicable)
#### Possibly Needed-Create and Activate Virtual Environment (Pythom 3.4 or higher):
    
Windows:
- $ python -m venv [directory]
- C:\> env\Scripts\activate.bat
- cd .. 
- cd .

Mac:
- $ python -m venv [directory]
- $ source myvenv/bin/activate
- cd .. 
- cd .

Install Flask:
- $ pip install Flask

Running Flask:
- flask run

Opening Program:
- Click 'http://127.0.0.1:5000'

### Acknowledgement
Inspiration:
- Movie Recommendation System: https://medium.com/analytics-vidhya/movie-recommendation-system-python-flask-web-application-heroku-deployment-7e39492b640c
- Firstleaf-A wine recommendation company: https://www.firstleaf.club/
- Tea Quiz: https://www.artoftea.com/pages/tea-quiz
- 08.ConcertRSVPJavaScript

To help get Flask working:
- How to Install and Use Flask on Windows for Beginners (2019): https://www.youtube.com/watch?v=QjtW-wnXlUY
- flask.palletprojects.com: https://flask.palletsprojects.com/
- How To Change Directory in Powershell | Change directory in Powershell #Powershell: https://www.youtube.com/watch?v=UhpH6JTr2tM
- python.land: https://python.land/virtual-environments/virtualenv
- Akito van Troyer

To help set-up some aspects, I used the following:
- Incorporating CSS: https://pythonhow.com/add-css-to-flask-website/
- Incorporating Pictures: https://kanchanardj.medium.com/how-to-add-images-to-html-in-a-flask-app-4dbcc92e3aeb
- Back Button: https://kanchanardj.medium.com/redirecting-to-another-page-with-button-click-in-python-flask-c112a2a2304c
- Linking Image: https://www.tutorialspoint.com/How-to-use-an-image-as-a-link-in-HTML
- Header Banner: https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_sticky_header

Pictures & Information:
- Pictures+Tea Information: https://www.teaforte.com/
- Tea Information: https://line.17qq.com/articles/ccnnllddpv_p6.html


