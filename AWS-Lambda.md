## Developing with `mapnik`+`node-mapnik` for AWS Lambda locally

Current AWS Lambda image comes with outdated versions of c++ compiler, linker and runtime. To install and test `mapnik` and `node-mapnik` follow the steps below: 

#### Prerequisite

Working `docker` - consult your OS specific guide on how to install and run docker

On `Ubuntu` follow instructions on https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/#if-you-need-to-use-aufs

`sudo service docker start|stop|restart`

#### Install docker-lambda (https://github.com/lambci/docker-lambda)

`git clone git@github.com:lambci/docker-lambda.git`

`cd docker-lambda`

#### Run interactive session

`sudo docker run -it lambci/lambda:build bash`

#### Install `mason` and build `mapnik` from source

`git clone https://github.com/mapbox/mason.git`

`cd mason`

`export CXX=/usr/bin/c++`

`export CC=/usr/bin/cc`

(^ FIXME: those shouldn't be necessary)

`./mason build mapnik 3.0.17`

#### Install `node-mapnik`

`git clone https://github.com/mapnik/node-mapnik.git`

`cd  node-mapnik`
 
`git checkout clang-5`

~~`git submodule update`~~ (!)

`make`

^ command above will fail after a while with errors in wagyu. This is expected, follow next steps to remedy

#####  Checkout g++-4.8 branch of wagyu 
`cd deps/wagyu`

`git checkout g++-4.8`

`cd ../../` 

#####  Replace mapnik mason package with symlink to previosly locally built mapnik (via mason) 

`rm -rf ./mason_packages/linux-x86_64/mapnik`

`ln -s /var/task/mason/mason_packages/linux-x86_64/mapnik ./mason_packages/linux-x86_64/mapnik`

##### Run make again

`make` 

##### Complete installation by running tests 

`make test`

Congrats! you have a working copy of node-mapnik/mapnik suitable for deploying on AWS Lambda








