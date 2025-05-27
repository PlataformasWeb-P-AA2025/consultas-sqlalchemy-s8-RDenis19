from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from clases import Departamento, Curso, Tarea, Entrega, Estudiante  # <-- aquí agregas Estudiante
from config import cadena_base_datos

# Crear motor y sesión
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Lista con los nombres de los estudiantes
nombres_estudiantes = ['Jennifer Bolton', 'Elaine Perez', 'Heather Henderson', 'Charles Harris']

# Hago la consulta para obtener las tareas que tienen entregas 
# Primero consulto desde Tarea, luego hago joins para llegar a Entrega y Estudiante
# Después filtro para que solo para entregas de los estudiantes que estan en la lista
tareas = session.query(Tarea).join(Tarea.entregas).join(Entrega.estudiante).filter(Estudiante.nombre.in_(nombres_estudiantes)).all()

for tarea in tareas:
    print(f"Tarea: {tarea.titulo}, Número de entregas: {len(tarea.entregas)}")
