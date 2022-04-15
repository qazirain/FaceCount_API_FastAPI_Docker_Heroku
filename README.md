## Dockerized webapp hosted on Heroku written with FastAPI which can extract faces from images

A POC RestAPI based on FastAPI Docker and hosted on Heroku

The API returns the number of faces in an image in json format!


Below are instructions to implement in in your local system using a separate development environment using the [Conda](http://conda.pydata.org/docs/index.html) package management system which comes bundled with the Anaconda Python distribution provided by Continuum Analytics.

### Step 1:
[Fork and clone](https://github.com/siddharthksah/FastAPI_Docker_Heroku) a copy of this repository on to your local machine.

### Step 2:
Create a `conda` environment called `faces-api` and install all the necessary dependencies, the environment.yml file is uploaded in the repo for ease:

    $ conda env create -n faces-api python=3.8 -y
    
### Step 3:
Install the extra dependencies, it is not required but helps in making sure the jupyter notebook is running in the right conda env:

    $ pip install -r requirement.txt
    $ conda install nb_conda

### Step 4:
Activate the `faces-api' environment:

    $ source activate faces-api

To confirm that everything has installed correctly, type

    $ which pip

at the terminal prompt. You should see something like the following:

    $ ~/anaconda/envs/faces-api/bin/pip

which indicates that you are using the version of `pip` that is installed inside the `faces-api` Conda environment and not the system-wide version of `pip` that you would normally use to install Python packages.

### Step 5:
Change into your local copy of the this repo:

    $ cd FastAPI_Docker_Heroku


