from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from clases import Entrega, Tarea, Estudiante, Curso, Instructor, Departamento
from config import cadena_base_datos

# Crear motor y sesión
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()


# Hacemos una consulta que obtiene todas las entregas
# de estudiantes que pertenecen a cursos del departamento "Arte"
entregas = session.query(Entrega).join(Entrega.tarea).join(Tarea.curso).join(Curso.departamento
              ).join(Curso.instructor).join(Entrega.estudiante).filter(Departamento.nombre == 'Arte').all()


# Recorremos los resultados para mostrarlos por pantalla
for en in entregas:
     # Accedemos a los datos relacionados
    print(f"Tarea: {en.tarea.titulo}, "
          f"Estudiante: {en.estudiante.nombre}, "
          f"Calificación: {en.calificacion}, "
          f"Instructor: {en.tarea.curso.instructor.nombre}, "
          f"Departamento: {en.tarea.curso.departamento.nombre}")
