from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from clases import Entrega, Tarea, Estudiante, Curso, Instructor, Departamento
from config import cadena_base_datos

# Crear motor y sesión
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

entregas = session.query(Entrega).join(Entrega.tarea).join(Tarea.curso).join(Curso.departamento
              ).join(Curso.instructor).join(Entrega.estudiante).filter(Departamento.nombre == 'Arte').all()


# Mostrar resultados
for en in entregas:
    print(f"Tarea: {en.tarea.titulo}, "
          f"Estudiante: {en.estudiante.nombre}, "
          f"Calificación: {en.calificacion}, "
          f"Instructor: {en.tarea.curso.instructor.nombre}, "
          f"Departamento: {en.tarea.curso.departamento.nombre}")
