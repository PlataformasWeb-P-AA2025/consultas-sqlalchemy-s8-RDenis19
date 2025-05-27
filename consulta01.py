from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from clases import Entrega, Tarea, Estudiante, Curso, Instructor, Departamento
from config import cadena_base_datos

# Crear motor y sesión
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

entregas = session.query(Entrega,Tarea.titulo,Estudiante.nombre,Entrega.calificacion,Instructor.nombre,
                         Departamento.nombre).join(Entrega.tarea).join(Tarea.curso).join(Curso.departamento
                        ).join(Curso.instructor).join(Entrega.estudiante).filter(Departamento.nombre == 'Arte').all()

# Mostrar resultados
for entrega, titulo, estudiante_nombre, calificacion, instructor_nombre, departamento_nombre in entregas:
    print(f"Tarea: {titulo}, Estudiante: {estudiante_nombre}, Calificación: {calificacion}, Instructor: {instructor_nombre}, Departamento: {departamento_nombre}")
