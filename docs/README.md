# flask_e2e_project

## 1. Flask Application
My Flask application serves as a platform for presenting information about doctors affiliated with a hospital. The application displays personal information such as their first name, last name, date of birth, address, phone number, and specialization. The data is generated using the Faker package and is stored in tables created within the MySQL Workbench database.

## 2. Technologies Used
- **API Service:** Backend
- **Docker:**: Containerization
- **.Env:** Environment variables
- **Flask:** Frontend and backend
- **Github:** Version control
- **Google OAuth:** Authorization
- **Microsoft Azure:** Deployment
- **MySQL Workbench:** Database via Azure
- **Sentry.io:** Debugging and logging
- **Tailwind:**: Frontend styling

## 3. Template of .Env 

```
DB_URL = 
DB_HOST =
DB_DATABASE =
DB_USERNAME = 
DB_PASSWORD = 
DB_PORT = 
DB_CHARSET = 

GOOGLE_CLIENT_ID = 
GOOGLE_CLIENT_SECRET = 
```

## 4. Docker (Steps)
- Create a Docker file within your app folder and name it `Dockerfile`. Copy [this code]().
- Lastly, create a text file and name it `requirements.txt`. Copy [this code]().
- In your Cloud Shell terminal, type `docker build -t <name of image> .`. This will build an image.
- Type `docker images`. This will show a list of your images.
- Type `docker run -d -p <port1>:<port2> <name of image>`. This will run your image in a container. 
- To preview your image, make sure to change your port to port 1 in Cloud Shell.
- Type `docker ps`. This will show a list of your containers.
- Type `docker stop <container ID>`. This will stop your container.
- Type `docker rm <container ID>`. This will remove your container.
- Type `docker system prune -a -f`. This will clean and remove everything.