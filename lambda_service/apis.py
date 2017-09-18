#chnages in a file
from flask import Flask, flash, redirect, render_template, request, session, abort,jsonify
import json
import docker
import fileinput
import os

#global object cretaion
app = Flask(__name__)
client = docker.DockerClient(base_url='unix://var/run/docker.sock')

#global variable declaration
port = 9055

@app.route('/lambda/genarate',methods = ['post'])
def generate_new_function():
    #get the request data
    data = json.loads(request.data)

    #create a new container
    global port
    port = port+1

    container = client.containers.run("python_base", detach=True, restart_policy={"Name": "always"}, ports={"80/tcp":port})
    #get containerID
    containerid = container.short_id

    #create a copy of template file
    os.system("cp template.py /tmp/"+ containerid +".py")

    # Read in the file
    with open("/tmp/"+ containerid +".py", 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('%FUNCTIONDATA%', data["function"])
    filedata = filedata.replace('%API_URL%', '"'+data["endpointname"]+'"')
    filedata = filedata.replace('%METHOD%', '"'+data["method"]+'"')

    # Write the file out again
    with open("/tmp/"+ containerid +".py", 'w') as file:
        file.write(filedata)

    #copy file in a docker container
    os.system("docker cp /tmp/"+containerid+".py "+ containerid+":/python_code/index.py")

    #restart container
    container.restart()

    #return url
    returnurl = "http://localhost:" + str(port)+""+data['endpointname']

    return json.dumps({"status":"success","url":returnurl}) 

#curl -X POST http://10.103.3.186:8090/lambda/genarate
@app.route('/lambda/update',methods = ['put'])
def update_function():
    
    return 'Existing comtainer updated'

#curl -X POST http://10.103.3.186:8090/lambda/genarate
@app.route('/lambda/status',methods = ['get'])
def status_function():
    
    return 'Status of the existing container'

#curl -X POST http://10.103.3.186:8090/lambda/genarate
@app.route('/lambda/delete',methods = ['delete'])
def delete_function():
    
    return 'Delete container'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8090,debug = True)



