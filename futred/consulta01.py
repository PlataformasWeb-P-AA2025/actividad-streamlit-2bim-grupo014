from sqlalchemy.orm import sessionmaker
from generador_tablas import engine, Usuario

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

# Consulta 1: Publicaciones de un usuario especifico

nombre_usuario = "William"
usuario = session.query(Usuario).filter_by(nombre=nombre_usuario).first()
if usuario:
    for publicacion in usuario.publicaciones:
        print(f"- {publicacion.contenido}")
else:
    print("Usuario no encontrado.")
