# flask_e2e_project

## 1. Flask Application
My Flask application serves as a platform for presenting information about doctors affiliated with a hospital. The application displays personal information such as their first name, last name, date of birth, address, phone number, and specialization. The data is generated using the Faker package and is stored in tables created within the MySQL Workbench. In addition, my Flask backend includes an API service with a single endpoint capable of retrieving various doctor tables.

**Flask application link:** https://beckieflaskapp.azurewebsites.net

## 2. Technologies Used
- **API Service:** Backend
- **Docker:** Containerization
- **.Env:** Environment variables
- **Flask:** Frontend and backend
- **Github:** Version control
- **Google OAuth:** Authorization
- **Microsoft Azure:** Deployment 
- **MySQL Workbench:** Database via Azure
- **Sentry.io:** Debugging and logging
- **Tailwind:**: Frontend styling

## 3. Template of .Env File

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
- Create a Docker file within your app folder and name it `Dockerfile`. Copy [this code](https://github.com/Beczheng/flask_e2e_project/blob/main/app/dockerfile).
- Lastly, create a text file and name it `requirements.txt`. Copy [this code](https://github.com/Beczheng/flask_e2e_project/blob/main/app/requirements.txt).
- In your Cloud Shell terminal, type `docker build -t <name of image> .`. This will build an image.
- Type `docker images`. This will show a list of your images.
- Type `docker run -d -p <port1>:<port2> <name of image>`. This will run your image in a container. 
- To preview your image, make sure to change your port to port 1 in Cloud Shell.
- Type `docker ps`. This will show a list of your containers.
- Type `docker stop <container ID>`. This will stop your container.
- Type `docker rm <container ID>`. This will remove your container.
- Type `docker system prune -a -f`. This will clean and remove everything.

## 5. Deployment on Azure App Service (Steps)
- In your Cloud Shell terminal, type `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`. This will install the Azure CLI.
- Type `az` to check if Azure CLI is installed.
- Type `az login --use-device-code`. A link with a code will appear. Click on the link and enter the code. Then, login to your Microsoft Azure account. This will give Cloud Shell permission to access your Azure account.
- Type `az account list --output table`. Make sure that you are using the correct subscription. If not, type `az account set --subscription <SubscriptionId>` to change it.
- Type `az group list` to double check everything.
- Type `az webapp up --name <app name> --runtime PYTHON:3.9 --sku B1 --resource-group <name of resource group`. This will create a webapp for your Flask app.

## 6. Errors
I encountered difficulties deploying the Flask application. When accessing the Flask application's URL, only the home page and contact page are visible by directly typing in their routes. Unfortunately, the doctors page is only accessible locally and is not visible on the deployed site. To view the screenshots of my Flask application, click [here](https://github.com/Beczheng/flask_e2e_project/tree/main/docs).

Once you've logged in through Google, it will bring you to this page:

![Screenshot 2023-12-18 224934](https://github.com/Beczheng/flask_e2e_project/assets/123920253/1437a162-b7b5-4738-a74c-6f2637e85ade)

Then, on this page, enter the following routes:
- https://beckieflaskapp.azurewebsites.net/home (does work)
- https://beckieflaskapp.azurewebsites.net/doctors (does not work, only works locally)
- https://beckieflaskapp.azurewebsites.net/contact (does work)
- https://beckieflaskapp.azurewebsites.net/api?specialization=doctors_cardiology (does not work, only works locally)