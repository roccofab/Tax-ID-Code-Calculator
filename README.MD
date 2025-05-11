# TAX CODE CALCULATOR
### Python GUI application to calculate italian tax code based on the basic rules for calculating the italian tax code.The program includes concepts such as Data Structure and Algorithms, regex/String manipulation, GUI with tkinter, object-oriented programming, files handling, database storage...

## REQUIREMENTS:
- Python 3.x or later
- IDE(optional)
- Windows/Linux/macOS

## DOWNLOAD AND SETUP ENVIROMENT:
- Zip the file or clone the repository using GIT.
- Make sure all files including gi_comuni.csv are in the same directory.
- Download MySQL and setup the enviroment:
   
   1. **Choose a password for the root user**, the root user is automatically created by MySQL and has all the permissions such as create database, create tables,modify databases and tables create new users, modify users permissions...

   2. After you have installed and you have registered open MySQL workbench and click on  'local instance'.

   3. Click on **"File"->"Open SQL Script"**.

   4. Select the **'setup.sql'** file into the project directory.

   5. Run the content of the file, it will automatically create the database tax_id_code.

- **Setup enviroment variables for your MySQL database(Windows):**

   1. Type environment variables from the start menu.

   2. Select edit environment variables.

   3. Create a new User variable **DB_USERNAME** with your mySQL database username.

   4. Create a new User variable **DB_PASSWORD** with your mySQL database password.

   5. Type OK to save the new User Variables.

   6. Open your CMD and verify that variables are set correctly by typing:

            echo %DB_USERNAME%  

            echo %DB_PASSWORD% 

      if you are a user with environment variables that are already set up and with different names change the name of the environment variables or change the name of the environment variables in the DatabaseConnection.py file


## HOW TO RUN:
- Open your command line and navigate to the directory that contains the program files.
- Type:
      
      python Main.py

## HOW TO USE:
### Enter your **name,surname,Date of Birth(gg-mm-aaaa), Gender(M/F) and your municipality** . Click on 'GENERATE' button and the program will show a message box that contains the generated tax code. Click on 'SAVE' and the program will show a message box that contains the generate tax code and then save data into MySQL database.

## PREVIEW:

<img src = "screenshots\Screenshot 2025-05-11 155325.png">

<img src = "screenshots\Screenshot 2025-05-11 155352.png">