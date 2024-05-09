# How to install and work with Docker container

We need Lenix to run docker
First we need to activate to options from control panel.

1. Enable WSL & Virtulization
   Open "Turn Window on or off" from start search
   activate "Virtual Machine Plateform" and "Windows subsystem for linux"

2. Install Docker for Windows (Version 2)

3. Sign up on Dockers

4. First create a project as we create in poetry, to check it is working perfectly or not

5. Then Check docker version to confirm, it is installed or not

   - docker version

6. Then create a file named "Dockerfile"

7. Write instruction in that file

8. Build/create a docker image with following command:

   - docker build -f Dockerfile -t [image_name] .
   - i.e. docker build -f Dockerfile -t my-fst-dckr-image .

   [If we somethng new in "Dockerfile" we will have to re-build the whole image again]

9. Check images with following command:

   - docker images

10. Once the image is created, next we have to run a container for development:
    docker run -d --name [container_name] -p 8000:8000 my-dev-image

    - -d = detacher, mean the terminal will be free after running the localhost
    - -p = port

11. Now open localhost to check either it is working or not.

12. To exit the process simply press "exit" command.

## Useful commands

1. Checking to see if Docker is running:

   - docker version

2. Building the Image for Dev:

   - docker build -f Dockerfile -t my-dev-image .

3. Check Images:

   - docker images

4. Verify the config:

   - docker inspect my-dev-image

5. Running the Container for Dev:

   - docker run -d --name dev-cont1 -p 8000:8000 my-dev-image

6. Check in browser:

   - [localhost](http://localhost:8000/)

7. container logs

   - docker logs dev-cont1

8. Test the Container:

   - docker run -it --rm my-dev-image /bin/bash -c "poetry run pytest"

9. List Running Containers

```bash
docker ps
```

10. List all Containers

- docker ps -a

11. Intract with the Container:

- docker exec -it dev-cont1 /bin/bash

12. Exit from the container shell

- exit
