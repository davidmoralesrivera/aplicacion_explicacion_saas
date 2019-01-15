sudo apt-get remove docker docker-engine docker.io

# se instalan los componentes para usar repositorios sobre https

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common


# se agrega el GPG key para el  repositorio de docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# verifica que exista la llave 
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# agregar el repositorio a local
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"


sudo apt-get update

# instalacion de docker para la version estable
sudo apt-get install docker-ce

# descarga e instala una imagen de docker que imprime hello world
sudo docker run hello-world


# instalar docker compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose