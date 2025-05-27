from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from clases import Departamento, Curso, Tarea, Entrega
from config import cadena_base_datos

# Crear motor y sesión
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Hago la consulta desde Departamento.
# Hago una relacion con las tablas cursos, luego tareas de esos cursos, y las entregas.
# Y filtro el departamento que tiene una nota menor o igual a 0.3
departamentos = session.query(Departamento).join(Departamento.cursos).join(Curso.tareas).join(Tarea.entregas
                    ).filter(Entrega.calificacion <= 0.3).all()                  

# Uso len(dep.cursos) para poder contar el numero de cursos
for dep in departamentos:
    print(f"Departamento: {dep.nombre} - Número de cursos: {len(dep.cursos)}")
