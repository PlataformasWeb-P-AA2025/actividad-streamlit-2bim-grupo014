from sqlalchemy.orm import sessionmaker
from generador_tablas import engine, Usuario

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

# Consulta 3: Publicaciones en las que reaccionó un usuario

nombre_usuario = "Shelley"
usuario = session.query(Usuario).filter_by(nombre=nombre_usuario).first()
if usuario:
    for reaccion in usuario.reacciones:
        print(f"- {reaccion.publicacion.contenido} ({reaccion.tipo_emocion})")
else:
    print("Usuario no encontrado.")
