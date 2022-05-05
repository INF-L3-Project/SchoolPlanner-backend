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


## Want to use this project?

1. Clone the repositiory into your workstation (device/machine) by running the command: <br>

        git clone https://github.com/INF-L3-Project/SchoolPlanner-backend.git


2. Create and activate a virtual environment:

   ```sh
   $ python3 -m venv venv && source venv/bin/activate
   ```

3. Install the requirements:

   ```sh
   (venv)$ pip install -r requirements.txt
   ```

4. Apply the migrations:

   ```sh
   (venv)$ python manage.py migrate
   ```
6. Inside `schoolplanner/` create a file name `.env` and use the example file in `env_example` to fill it file

5. Seed the database:

   ```sh
   (venv)$ python manage.py migrate
   ```

6. Run the server:

   ```sh
   (venv)$ python manage.py runserver
   ```


7. Check the server is running by going to [localhost:8000](http://127.0.0.1:8000)
