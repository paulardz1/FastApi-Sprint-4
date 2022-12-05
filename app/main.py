from fastapi import FastAPI
from pydantic import BaseModel
#from typing import List
from uuid import uuid4

app= FastAPI()#contruir una aplicacion de tipo api que se llama app
#Get obtener datos del servidor 


@app.get ("/")#respuesta que va a dar el servidor a solicitud del usuario RUTA DE URL 
def root():
  return {"message": "Hola MisionTIC 2022"}
  
@app.get("/usuarios/{user_id}")#url con parametros
def mensaje(user_id:int):
  return f"El usuario es: {user_id}"

cursos=[{"cursos":"programacion basica"},{"cursos":"software"},{"cursos":"Sistemas"},{"cursos":"Desarrollo web"}]

@app.get("/cursos")
def leer_cursos(skip:int=0, limit: int=10): # el skip es para saber cuantos cursos quiero visualisar es como si fuera un ciclo y limit es i  
  return cursos[skip:skip+limit] # retorna desde cero hasta 10

class Student(BaseModel):
    id: str
    name: str
    lastname: str
    #skills: List[str] = []

students = []

@app.get("/estudiantes")
def get_students():
    return students

@app.post("/estudiantes")
def save_student(student: Student):
    student.id = str(uuid4())
    students.append(student.dict())
    return "Estudiante registrado"

@app.put("/estudiantes/{id}")
def update_student(updated_updated: Student, id:str):
    for student in students:
        if student["id"] == id:
            student["name"] = updated_updated.name
            student["lastname"] = updated_updated.lastname
            
            return "Estudiante modificado"
    return "No existe el estudiante"

@app.delete("/estudiantes/{id}")
def delete_student(id:str):
  for student in students:
      if  student["id"]==id:
        students.remove(student)
        return "estudiante eliminado"
  return "no existe el estudiante"