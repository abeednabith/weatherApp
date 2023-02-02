# weatherApp
This is a web application to find the weather of a given city. This applications have 2 microservices, the first one gives you a zip codes of the given city name and the second microservice gives weather of the city which gives zip code as input. 

Highlevel design of the microservices: service1(zipcode-microservice) and service2(weather-microservice)

![hw1_microservices-1](https://user-images.githubusercontent.com/102093437/216417100-fb57fb36-bf54-4120-a0cc-ed1d4c449e5e.png)

Each service is considered as seperate programs, and this can have seperate docker files. We are going to build the images and run the containers seperately.

Firstly, build the docker images for the manifest in zipcode-microservice:

<img width="497" alt="Screenshot 2023-02-02 at 11 46 54 AM" src="https://user-images.githubusercontent.com/102093437/216434464-760c7fd0-5270-4beb-bf0c-bf96f354d62f.png">

this creates a docker image:

<img width="928" alt="Screenshot 2023-02-02 at 11 49 05 AM" src="https://user-images.githubusercontent.com/102093437/216434727-c0c50fb1-a9e8-44d8-bb75-ebacfdc59468.png">

then, run the image and it's starts a conatiner:

<img width="725" alt="Screenshot 2023-02-02 at 11 50 43 AM" src="https://user-images.githubusercontent.com/102093437/216435073-21137d4f-3924-4b58-8e26-3d0a58d08cd9.png">

this creates and starts a new container:

<img width="932" alt="Screenshot 2023-02-02 at 11 52 03 AM" src="https://user-images.githubusercontent.com/102093437/216435305-7abfa2e7-ec58-47ac-b51b-f999d6179ac6.png">
