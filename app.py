from flask import Flask, escape, request,jsonify
import json
import random
import time
import math

app = Flask(__name__)

students=[]
classes=[]

@app.route('/students/<int:id>',methods=["GET"])
def getStudents(id):
	for s in students:
		if s.get("student_id")==id:
			return jsonify(s)

@app.route('/students/get/',methods=["GET"])
def getAllStudents():
	return jsonify({'students : ':students})

@app.route('/students',methods=["POST"])
def createStudent():
	new_student={}
	new_student['student_id']=get_new_id()			
	new_student['name']=get_data_from_input(request.data.decode('utf8'),'name')
	students.append(new_student)
	return jsonify(new_student),201


@app.route('/classes',methods=["POST"])
def post_a_class():
	new_class={}
	new_class['class_id']=get_new_id()
	new_class['name']=get_data_from_input(request.data.decode('utf8'),'name')
	new_class['students']=[]
	classes.append(new_class)
	return jsonify(new_class),201

@app.route('/classes/<int:id>',methods=["GET"])
def getClass(id):
	for c in classes:
		if c.get("class_id")==id:
			return jsonify(c)

@app.route('/classes/<int:input_class_id>',methods=["PATCH"])
def update_the_class(input_class_id):
	index=-1
	curr_class={}
	stu_id=int(get_data_from_input(request.data.decode('utf8'),'student_id'))
	for i in range(0,len(students)):
		if (students[i]).get('student_id')==stu_id:
			index=i
			break
	if index==-1:
		print('No student with the id')
	else:	
		for i in range(0,len(classes)):
			if (classes[i]).get('class_id')==input_class_id:
				(classes[i]).get('students').append(students[index])
				curr_class=classes[i]
				break		
	return jsonify(curr_class)			
	

def get_data_from_input(input_data,s):
	new_dict=json.loads(input_data)
	return new_dict.get(s)

def get_new_id():
	new_id=int(time.time())
	new_id=math.trunc(new_id)
	return new_id

    
if __name__=="__main__":
	app.run(Debug=True,port=8080)
