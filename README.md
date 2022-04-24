# <b>SCHOOL PLANNER</b>
## <b>Overview</b>
This is  a web application that allows school administrators to easily manage their schedules.
<br>
![Website overview](./core/static/images/overview.png)



## **Some features** 

- Authentication 

- Add, modify, delete a class,
- Add a teacher and his schedule
- Associate subjects to a teacher or a class
- Associate classes to rooms
- Generate the timetable according to a teacher, a class, a room
- Graphical mode with drag and drop to easily position classes at selected times on the timetable



## Some pictures

![Website overview](./screenshots/overview.png)

![Website overview](./screenshots/overview.png)

## <b>Project setup</b>

1. Clone the repositiory into your workstation (device/machine) by running the command: <br>

        git clone https://github.com/INF-L3-Project/SchoolPlanner-backend.git

2. Place yourself at the root of the project. <br>
   
        C:\Users\...\SchoolPlanner-backend\

### Before executing the following commands, always make sure you are at the root of the project.

3. Setup the virtual environment for the project at its root by running the following commands: <br>
    `Creation/Installation`

        1. pip install virtualenv
        2. virtualenv .env
   
    `Activation on Windows`
    
        3. .env\Scripts\activate
   
    `Activation on Linux/MacOS`
    
        3. source .env/bin/activate

    To deactivate the already activated virtual environment, simply type `deactivate` in the terminal, if not run the following command: <br>

    `Deactivation on Windows`

        .env\Scripts\deactivate

    `Deactivation on Linux/MacOS`

        source .env/bin/deactivate

4. Inside the created and activated virtual environment, `Install` the required packages from [requirements.txt](./requirements.txt) by running the command: <br>

        pip install -r requirements.txt

6. Inside *schoolplanner/* create a file name *.env* and use the example file in *env_example* to fill it file

## <b>Launching of the project</b>

### Before executing the following commands, always make sure you are at the root of the project.

5. Migrate the data to the database (`Sqllite` by default): <br>

        python manage.py migrate

6. Run the project using the command: <br>

        python manage.py runserver

7. Check the server is running by going to [localhost:8000](http://127.0.0.1:8000)
