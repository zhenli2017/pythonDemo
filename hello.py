#!/usr/bin/env python
# -*- coding:utf-8 -*-

 
from flask import Flask,render_template
import requests
import logger
from flask import request
import logging
import json





logger = logging.getLogger(__name__)

 
app = Flask(__name__)
 
@app.route('/')
def index():
     return "hello,world"
 
@app.route("/testget",methods=["get"])
def testget():
	logger.info("this is testget")
	dicttest = {"a":100,"b":"this is testget"}
	return json.dumps(dicttest)
	#return "testget"


@app.route("/avalue",methods=["get"])
def testget2():
	name = request.args.get("name")
	print name
	return "%s is server response !" % name
	#不能返回int类型
	#return 100

@app.route("/test_post",methods=["post"])
def testPost():
	logger.info("method = ",request.method)
	a = request.get_data()
	print (a)
	name = request.form.get("name")
	age = request.form.get("age")

#	b = json.loads(a)
#	print (b)
	d =  {}
	d["name"]=name
	d["age"]=age
	result = dict(code=200,data=d,msg="OK")
	return json.dumps(result)

@app.route("/testpostjson",methods=["post"])
def testpostjson():
	testjson = request.get_json()
	logger.info(testjson)
	name = testjson["name"]
	age = testjson["age"]
	result = dict(code =200,msg="OK",data=testjson)
	return json.dumps(result)

@app.route("/upload",methods=["post"])
def testpostUpload():
	filetest = request.files.get("file")
	print filetest
	filename = secure_filename(filetest.filename)
	logger.info(filename)
	f.save("/root/test/"+str(filename))
	result = dict(code=200,msg="OK")
	return json.dumps(result)


@app.route("/testpostimage",methods=["post"])
def postimage():
    print ("postImage")
    pass

if __name__ == '__main__':
	app.run()
