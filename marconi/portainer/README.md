# Portainer

This is a docker container that allows a gui to control your docker containers on a server 

With portnainer, we run docker on a web gui and not the terminal

## Installation

the installation guide can be found at https://docs.portainer.io/start/install-ce/server/docker/linux

We start docker

```bash
sudo systemctl start docker
```

First, create the volume that Portainer Server will use to store its database:

```bash
docker volume create portainer_data
```

Then, download and install the Portainer Server container:

```bash
docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest
```

