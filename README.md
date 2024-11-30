# Weather App

A simple weather application that fetches real-time weather data using an external API.

## Features
- Real-time weather updates
- Search by city or location
- Responsive and user-friendly UI


## Prerequisite
### Generate API key
To use the Weather App, you’ll need an API key from a weather data provider. Here’s a step-by-step guide to help you get one.

1. Sign Up in the OpenWeather map website following the link: https://home.openweathermap.org/
2. If you do not have an account, click on Create an account and provide the required details. Complete any required verification process (e.g., email verification).
3. After successful registration, login with your credentials.
![](images/login.png)
4. After successful login, click on your username and click **My API Keys**
![](images/myapi.png)
5. There will be an API key generated for you, Copy the key. If you want you can generate as many keys as possible.
![](images/apikey2.png)
6. create a file called **api_key.txt** in your local machine and paste the API key copied in the above step.

### Clone repository
1. Clone the Github repository.
2. In the folder where you have cloned the repo, move the **api_key.txt** file created in step.6 in **Generate API Key section**.

### Packages
1. Make sure you have latest version of python installed. If not download the latest version by following the link: https://www.python.org/downloads/ 
2. Install Requests module following the link: https://pypi.org/project/requests/ 

## Run Application
1. Open terminal or command prompt based on the operating system.
2. Navigate to the folder where you have kept the code.
3. Run the below command
    ```
    python weatherApp.py

    ```
4. Enter the name of the city for which you want to check weather. press **Enter**.
5. Provide the unit celcius or Farenhite for the temperature. press **Enter**
6. The application will display the current weather.

## Troubleshooting
1. If you get any error related to **API key not found**. Make sure you keep the **api_key.txt** in the root of the directory where you have the weatherApp.py file.
