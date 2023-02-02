# weatherApp
This is a web application to find the weather of a given city. This applications have 2 microservices, the first one gives you a zip codes of the given city name and the second microservice gives weather of the city which gives zip code as input. 

Highlevel design of the microservices: service1(zipcode-microservice) and service2(weather-microservice)

![hw1_microservices-1](https://user-images.githubusercontent.com/102093437/216417100-fb57fb36-bf54-4120-a0cc-ed1d4c449e5e.png)

This application uses 2 public API's to get the zipcode of a city and weather of a city by using zipcode.

For zipcode: http://api.zippopotam.us/us/{state}/{city}

For weather: http://api.openweathermap.org/data/2.5/weather?q={zipcode},us&appid=2e1abf2d92294ee4d9726bded5f32d05

Each service is considered as seperate programs, and this can have seperate docker files. We are going to build the images and run the containers seperately.

<ins><strong> Build the docker images for the zipcode-microservice and start the service inside a container: </strong></ins>

1) Build the docker image
<img width="497" alt="Screenshot 2023-02-02 at 11 46 54 AM" src="https://user-images.githubusercontent.com/102093437/216434464-760c7fd0-5270-4beb-bf0c-bf96f354d62f.png">

this creates a docker image:

<img width="928" alt="Screenshot 2023-02-02 at 11 49 05 AM" src="https://user-images.githubusercontent.com/102093437/216434727-c0c50fb1-a9e8-44d8-bb75-ebacfdc59468.png">

2) Run the image and it's starts a conatiner:

<img width="725" alt="Screenshot 2023-02-02 at 11 50 43 AM" src="https://user-images.githubusercontent.com/102093437/216435073-21137d4f-3924-4b58-8e26-3d0a58d08cd9.png">

this creates and starts a new container:

<img width="932" alt="Screenshot 2023-02-02 at 11 52 03 AM" src="https://user-images.githubusercontent.com/102093437/216435305-7abfa2e7-ec58-47ac-b51b-f999d6179ac6.png">

Now the service will be available with the API http://127.0.0.1:5001/zipcode?state=ca&city=fremont

<ins><strong> Build the docker images for the weather-microservice and start the service inside a container: </strong></ins>

1) Build the docker image

<img width="581" alt="Screenshot 2023-02-02 at 11 58 42 AM" src="https://user-images.githubusercontent.com/102093437/216436694-40d787cf-feed-4686-9f32-19bfd234257d.png">

this creates a docker image:

<img width="931" alt="Screenshot 2023-02-02 at 11 59 36 AM" src="https://user-images.githubusercontent.com/102093437/216436882-19727e8d-a2bf-4d27-858d-e8d5b5856e4e.png">

2) Run the image and it's starts a conatiner:

<img width="823" alt="Screenshot 2023-02-02 at 12 01 12 PM" src="https://user-images.githubusercontent.com/102093437/216437209-4138c6d3-884e-4f41-89ba-a8fb355a02fb.png">

this creates and starts a new container:

<img width="930" alt="Screenshot 2023-02-02 at 12 02 19 PM" src="https://user-images.githubusercontent.com/102093437/216437390-fef02aa9-233e-4d75-bd72-bc704ed5b350.png">

Now the service will be available with the API http://127.0.0.1:5002/weather?zipcode=94539
