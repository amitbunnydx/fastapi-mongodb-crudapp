#import statement
from fastapi import APIRouter
from models.student import Student
from config.database import connection
from schemas.student import studentEntity,listOfStudentEntity
from bson import ObjectId

student_router=APIRouter()

@student_router.get('/hello')
async def hello_world():
    return "hello world"

#getting all students
@student_router.get('/students')
async def find_all_students():
    return listOfStudentEntity(connection.local.student.find())

#getting one students
@student_router.get('/students/{studentId}')
async def find_one_student(studentId):
    return studentEntity(connection.local.student.find_one({'_id':ObjectId(studentId)}))

#creating a student
@student_router.post('/students')
async def create_student(student:Student):
    connection.local.student.insert_one(dict(student))
    return listOfStudentEntity(connection.local.student.find())

@student_router.put('/student/{studentId}')
async def update_student(studentId,student:Student):
    #find the studend then update it with new student data
    connection.local.student.find_one_and_update(
        {'_id':ObjectId(studentId)},
        {'$set':dict(student)}
    )
    return studentEntity(connection.local.student.find_one({'_id':ObjectId(studentId)}))

@student_router.delete('/student/{studentId}')
async def delete_student(studentId):
    # find the student delete it and also return the same student object
    return studentEntity(connection.local.student.find_one_and_delete({'_id': ObjectId(studentId)}))

