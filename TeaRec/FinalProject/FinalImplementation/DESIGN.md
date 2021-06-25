System Description:
1. Within VSCode, user must type "flask run" into terminal.
2. USser must then click on 'http://127.0.0.1:5000/' 
3. Cite will open in Chrome. 
4. The app.py will load the index.html on the page.
5. Layout.html will refer to style.css and format index.html accordingly.
6. The user must then fill out 'name,' 'taste,' and 'effect.'
7. If user fails to fill out any 1 of the 3 fields, error.html will be triggered, and an error message will appear.
8. If all required fields are filled out, app.py will match the responses with their corresponding html page via if statements.
9. Said corresponding page will appear. Rec.css will format this page accordingly.
10. Page should load with a header, description, image, hyperlink, and a restart button.
11. The image is pulled from the 'static' folder while the other componments are found within the corresponding html pages.
12. The user's answers are also recorded during this time and stored in 'list.csv.' This process is done via list.html and app.py.
13. If the user clicks on the image, a new tab, via "target='_blank'" will appear in a third-party company will be available. This is where the images are from, and where the user can purchase said tea if so desired.
14. If the user clicks restart, an app.py path will be triggered, and steps 4-12 will be repeated. User may restart as many times as they would like.
15. If user does nothing, nothing will happen and they may close the tab.
16. To close the program in VSCode, user must press 'Ctrl+C'.

## Initial Decision
I decided to do a recommendation system because my roommates and boyfriend helped me brainstorm. I wanted to build something that could easily be incorporated into other areas, such as restaraunts, movies, music, and even friends. I thought that this project would be a good introduction into a more complex area, such as extremely complex system such as Facebook's recommendation system. We found a few movie recommendation systems online, and I took note of how they were setup. Along with that, I took inspiration from 08.ConcertRSVPJavaScript. The setup for this exercise made sense to me and it was good practice learning how to implement it into my own project. I also thought this exercise could easily be expanded upon into any area. My reasoning for choosing tea specificaly was simply because I like it. I drink a lot of it and knew it would be simpyl for me to categorize it since I  already had knowledge on the subject. In doing this project, I hope to learn more in this area and gain a deeper understanding for how other factors might be incorporated, such as machine learning and/or pre-existing data systems.

## Initial Planning
Being a relatively straight foward system, there luckily wasn't too many variable when programming this. The only parts that required a bit more planning where the recommended html pages (the collection of 'Group' folders). To approach this, I first looked up types of teas, and their characteristics. Numerous websites had cetgorial lsits. From here, I combined some of the teas and descriptions of them, such as their taste, effects, and caffeine. I then dwindled it down. I combined similar words, eliminated teas that didn't fit within any of the categorizations, and omited any descriptions that only fit with one type. Next, I made two flowcharts. The first was a web that broke the categories down by caffeine->taste->effects. I then matched up teas with said characteristics. Realizing this would result in way too many html pages, I decided to simply break them down into taste->effects. This made it easier to match up corresponding teas, and required less pages. 

## Flask
Since I wanted to record uses entries and incorporate numerous programming languages, I decided Flask would be best for this. However, when initially setting up Flask, I ran into some issues. Being on a Windows, my computer wasn't cooperating and after a week of troubleshooting, it was decided that the best approach would be to utilize a virtual environment, or an interpreter that consists mutliple packages. From there, I had to learn how to use the 'cd' command to ensure I was in the correct directoy. Once these all worked, all I had to do was type 'flask run' whenever I wanted to run my program.

## Organization
I based my organization and setup on a combination of 08.ConcertRSVPJavaScript, Flask setup, and what made sense to me. The most important, and difficult was organizing all the different recommended html pages, so I used a numerical system. When programming them into app.py, I used the same system. I was initially inspired by 08.ConcertRSVPJavaScript because I liked the setup of it, and it made sense to me. I found it easy to navigate and thus easy to incorporate into my own project. Regarding Flask, Flask requires a specific setup. Within this setup, I needed 'app.py,' 'static,' and 'templates.' 'App.py' holds all the routing thoughout the website and initializes Flask. 'Static' houses all images and CSS files. 'Templates' contains all html files. Learning how to properly route all files, such as CSS in Html and Html into app.py,' also really aided in organization. 

## Design
 I didn't have a specific design idea in mind other than clean and coherent. Therefore, I kept the CSS files relatively uncomplicated and basic looking. I wanted overall basic colors, black and white, with just a splash of color, hence the buttons and header. I incorporated in aspects such as a 'return' button, hyperlinked pictures, and a header because I found they made them easier to navigate the website cleanly while keeping all original aspects that I had hoped for. In terms of the home page, I chose to only do two preferences because I wanted to keep it simple for the sake of learning. However, I kept 'name' because I wanted to explore list.csv and wanted to understand the setup.

## List
I decided to utilize 'list.csv' because I currently work and am planning to continue working in data and analytics. I though understanding this would help introduce me to the world of data programming. If I had more time, I would have liked to implement SQLite. Despite my inability to implement it for this project, SQLite is something that I plan on exploring more for the same purpose. 