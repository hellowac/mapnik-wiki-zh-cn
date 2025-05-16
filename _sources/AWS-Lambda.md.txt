# AWS Lambda

## Developing with `mapnik`+`node-mapnik` for AWS Lambda locally

### Prerequisite

Working `docker` - consult your OS specific guide on how to install and run docker

On `Ubuntu` follow instructions on <https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/#if-you-need-to-use-aufs>

`sudo service docker start|stop|restart`

### Install docker-lambda (<https://github.com/lambci/docker-lambda>)

`git clone git@github.com:lambci/docker-lambda.git`

`cd docker-lambda`

### Run interactive session

`sudo docker run -it lambci/lambda:build bash`

### Install node-mapnik

See <https://github.com/mapnik/node-mapnik/issues/863>
