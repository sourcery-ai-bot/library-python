# Docker Commands

## [System Commands](https://docs.docker.com/engine/reference/commandline/system/)

### Check Status of All Images, Containers and Volumes

$ `docker system df -v`

### Check Network Settings

$ `docker network inspect bridge`

### Remove All Stopped Containers, Dangling Images, and Unused Networks

$ `docker system prune`

$ `docker system prune --volumes`    (NOTE: includes the removal of all unused volumes)

## [Container Commands](https://docs.docker.com/engine/reference/commandline/container/)

### Stop All Running Containers

$ `docker stop $(docker ps -a -q)`

### Remove a Specific Container

$ `docker container rm <container-name-or-id>`

### Remove Stopped Containers

$ `docker container prune`

### Remove All Containers

$ `docker rm -f $(docker ps -a -q)`

## [Image Commands](https://docs.docker.com/engine/reference/commandline/image/)

### Remove a Specific Image

$ `docker image rmi <image-name-or-id>`

### Remove All Images

$ `docker rmi -f $(docker images -a -q)`

### Remove Dangling Images

$ `docker rmi -f $(docker images -f "dangling=true" -q)`

You can also use the far simpler command:

$ `docker image prune`

## [Volume Commands](https://docs.docker.com/engine/reference/commandline/volume_prune/)

### Remove All Volumes Not Attached to a Running Container

$ `docker volume prune`

### Remove Dangling Volumes

$ `docker volume rm docker volume ls -q -f dangling=true`

## Sources

Useful Link: <https://linuxize.com/post/how-to-remove-docker-images-containers-volumes-and-networks/>
