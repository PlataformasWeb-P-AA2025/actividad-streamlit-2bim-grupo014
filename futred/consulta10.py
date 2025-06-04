from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from generador_tablas import engine, Usuario, Publicacion, Reaccion

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

# Consulta 10: Número total de publicaciones, usuarios y reacciones

total_usuarios = session.query(Usuario).count()
total_publicaciones = session.query(Publicacion).count()
total_reacciones = session.query(Reaccion).count()
print(f"- Usuarios: {total_usuarios}")
print(f"- Publicaciones: {total_publicaciones}")
print(f"- Reacciones: {total_reacciones}")