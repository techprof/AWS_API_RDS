# AWS_API_RDS


Building Microservice API on AWS:



In this test, I am using the chalice command line utility to create and deploy a basic REST API. First, you’ll need to install chalice. Using a virtualenv is recommended:
$ pip install virtualenv
$ virtualenv ~/.virtualenvs/chalice-demo
$ source ~/.virtualenvs/chalice-demo/bin/activate
Note: make sure you are using python2.7, python3.6, or python3.7. These are the only python versions currently supported by AWS Lambda so they are also the only versions supported by the chalice CLI and chalice python package. You can find the latest versions of python on the Python download page. You can check the version of python in your virtualenv by running:

# Double check you have a supported python version in your virtualenv
$ python -V
Next, in your virtualenv, install chalice:

$ pip install chalice
You can verify you have chalice installed by running:

$ chalice --help
Usage: chalice [OPTIONS] COMMAND [ARGS]...
...
Credentials
Before you can deploy an application, be sure you have credentials configured. If you have previously configured your machine to run boto3 (the AWS SDK for Python) or the AWS CLI then you can skip this section.

If this is your first time configuring credentials for AWS you can follow these steps to quickly get started:

$ mkdir ~/.aws
$ cat >> ~/.aws/config
[default]
aws_access_key_id=YOUR_ACCESS_KEY_HERE
aws_secret_access_key=YOUR_SECRET_ACCESS_KEY
region=YOUR_REGION (such as us-west-2, us-west-1, etc)
If you want more information on all the supported methods for configuring credentials, see the boto3 docs.

Creating Your Project
The next thing we’ll do is use the chalice command to create a new project:

$ chalice new-project helloworld
This will create a helloworld directory. Cd into this directory. You’ll see several files have been created for you:

$ cd helloworld
$ ls -la
drwxr-xr-x   .chalice
-rw-r--r--   app.py
-rw-r--r--   requirements.txt
You can ignore the .chalice directory for now, the two main files we’ll focus on is app.py and requirements.txt.

Let’s take a look at the app.py file:
from chalice import Chalice
import psycopg2

#app = Chalice(app_name='helloworld')

app = Chalice(app_name='helloworld')
db_user = 'test'
db_pass = 'password'
db_host = 'https://.....'
db_port = 5432

@app.route('/get_data')
def get_data():
    with psycopg2.connect(user=db_user, password=db_pass, ...) as conn:
        with conn.cursor() as cur:    
            cur.execute("SELECT user_name, DOB FROM test")

@app.route('/')
def index():
    return {'hello': 'world': 'cur'}
The new-project command created a sample app that defines a single view, /, that when called will return the JSON body {"hello": "world"}.

Deploying
Let’s deploy this app. Make sure you’re in the helloworld directory and run chalice deploy:

$ chalice deploy
...
Initiating first time deployment...
https://qxea58oupc.execute-api.us-west-2.amazonaws.com/api/
You now have an API up and running using API Gateway and Lambda:

$ curl https://qxea58oupc.execute-api.us-west-2.amazonaws.com/api/
{"hello": "world":"John 12-July-2019"}
Try making a change to the returned dictionary from the index() function. You can then redeploy your changes by running chalice deploy.

Further Testing needed above code..!
