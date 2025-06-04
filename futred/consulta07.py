from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from generador_tablas import engine, Reaccion, Publicacion

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

# Consulta 7: Publicaciones sin ninguna reacción

publicaciones_sin_reaccion = session.query(Publicacion).outerjoin(Reaccion).filter(
    Reaccion.id == None
).all()

for p in publicaciones_sin_reaccion:
    print(f"- {p.contenido} (Autor: {p.usuario.nombre})")
