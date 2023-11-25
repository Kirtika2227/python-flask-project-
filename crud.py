from flask import Flask, jsonify, request
#from flask_restful import Resource, Api
from  flask_cors import CORS
import mysql.connector

app = Flask(__name__)

#api= Api(app)

cors = CORS(app, support_credentials=True)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="esd_fa"
)

# Define routes for managing students
@app.route('/students', methods=['GET'])
def get_students():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Student_info")
    results = cursor.fetchall()
    students = []
    for row in results:
        student = {
            'student_id': row[0],
            'name': row[1],
            'email': row[2],
            'phone': row[3],
            'selected_course': row[4]
        }
        students.append(student)
    return jsonify(students), 200

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student_by_id(student_id):
    cursor = db.cursor()
    query = "SELECT * FROM Student_info where student_id = %s"
    values = (student_id,)
    cursor.execute(query, values)
    results = cursor.fetchall()
    students = []
    for row in results:
        student = {
            'student_id': row[0],
            'name': row[1],
            'email': row[2],
            'phone': row[3],
            'selected_course': row[4]
        }
        students.append(student)
    return jsonify(students), 200
    
@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    cursor = db.cursor()
    query = "INSERT INTO Student_info (Name, Email_id, phone_No, selected_course) VALUES (%s, %s, %s, %s)"
    values = (data['name'], data['email'], data['phone'], data['selected_course'])
    cursor.execute(query, values)
    db.commit()
    return jsonify({'message': 'Student created successfully'}), 201
@app.route('/students', methods=['PUT'])
def update_student():
    data = request.get_json()
    cursor = db.cursor()
    query = "UPDATE Student_info SET Name = %s, Email_id = %s, phone_No = %s, selected_course = %s WHERE student_id = %s"
    values = (data['name'], data['email'], data['phone'], data['selected_course'], data["student_id"])
    cursor.execute(query, values)
    db.commit()
    return jsonify({'message': 'Student updated successfully'}), 200

@app.route('/students', methods=['DELETE'])
def delete_student():
    data = request.get_json()
    cursor = db.cursor()
    query = "DELETE FROM Student_info WHERE student_id = %s"
    values = (data["student_id"],)
    cursor.execute(query, values)
    db.commit()
    return jsonify({'message': 'Student deleted successfully'}), 200

@app.route('/courses', methods=['GET'])
def get_courses():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Course_info")
    results = cursor.fetchall()
    courses = []
    for row in results:
        course = {
        'student_id': row[0],
        'name': row[1],
        'duration': row[2],
        'fees': row[3],
        'certification': row[4]
        }
        courses.append(course)
    return jsonify(courses), 200

@app.route('/courses', methods=['POST'])
def create_course():
    data = request.get_json()
    cursor = db.cursor()
    query = "INSERT INTO Course_info (student_id, Course_name, Course_duration, Course_fees, Certification) VALUES (%s, %s, %s, %s, %s)"
    values = (data['student_id'], data['name'], data['duration'], data['fees'], data['certification'])
    cursor.execute(query, values)
    db.commit()
    return jsonify({'message': 'Course created successfully'}), 201

@app.route('/updatecourses', methods=['PUT'])
def update_course():
    data = request.get_json()
    cursor = db.cursor()
    query = "UPDATE Course_info SET Course_name = %s, Course_duration = %s, Course_fees = %s, Certification = %s WHERE student_id = %s"
    values = (data['name'], data['duration'], data['fees'], data['certification'], data["student_id"])
    cursor.execute(query, values)
    db.commit()
    return jsonify({'message': 'Course updated successfully'}), 200

@app.route('/deletecourses', methods=['DELETE'])
def delete_course():
    data = request.get_json()

    cursor = db.cursor()
    query = "DELETE FROM Course_info WHERE student_id = %s"
    values = (data["student_id"],)
    cursor.execute(query, values)
    db.commit()
    return jsonify({'message': 'Course deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True,port =8080)

