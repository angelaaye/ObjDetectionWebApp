# assignment-1

Google doc link:
https://docs.google.com/document/d/1tXsjnKTAvbaIt3HoFy2Hb7Ln5krJ6E2Mr0ybT6ZzAFE/edit?usp=sharing





## Frontend File Structure

```
opencv-app
├── README.md
├── babel.config.js
├── dist
├── node_modules
├── package-lock.json
├── package.json
├── public
│   └── index.html
└── src
    ├── App.vue
    ├── assets
    │   └── global.css
    ├── components
    │   ├── ImageUpload.vue
    │   ├── LoginStatus.vue
    │   ├── NavBar.vue
    │   └── Welcome.vue
    ├── main.js
    ├── router
    │   └── index.js
    └── views
        ├── Home.vue
        ├── Login.vue
        ├── Register.vue
        ├── Thumbnails.vue
        └── Upload.vue
```





## Backend File Structure

```
app.py
config.py
api/
  endpoints/
  helpers.py
  parsers.py
  restplus.py
  serializers.py
  yolo.py
database/
  __init__.py
  models.py
helpers/
migrations/
uploads/
```

|                |                                                              |
| -------------- | ------------------------------------------------------------ |
| app.py         | The entry point file that initializes flask server and database |
| config.py      | Loads .env file with variables based on ENV and populates the config object that can be imported in other files |
| api/           | Folder containing API logic                                  |
| endpoints/     | Folder for files for API endpoints. Each file should be names the same as the url namespace. |
| helpers.py     | File that contains most logic and communication with the DB. |
| parsers.py     | Parsers are the structure templates for body data used in POST or PUT requests. |
| serializers.py | Similar to parsers, serializers define the (JSON) structure of outputted data returned from endpoints |
| yolo.py        | File that contains code for performing object detection using YOLOv3. |
| database/      | Folder for database settings and models                      |
| __init__.py    | Creates a database instance that can be imported from other files |
| models.py      | SQLAlchemy Representations of database tables                |
| migrations/    | Database migration versions generated by flask db init and manually edited to reflect the database structure |
| uploads/       | Folder for storing photos on the local file system.          |