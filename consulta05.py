from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from clases import Curso, Entrega
from config import cadena_base_datos

# Crear motor y sesión
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Todos los curso0
cursos = session.query(Curso).all()

# Recorro cada curso para obtener sus entregas y calcular el promedio
for curso in cursos:
    # Traigo las entregas que pertenecen a tareas de este curso
    entregas = session.query(Entrega).join(Entrega.tarea).filter_by(curso_id=curso.id).all()
    
    # Calculo el promedio de calificaciones
    if entregas:
        suma = sum([e.calificacion for e in entregas])
        promedio = round(suma / len(entregas), 2)
    else:
        promedio = "No hay entregas"
    
    print(f"Curso: {curso.titulo} - Promedio calificaciones: {promedio}")
