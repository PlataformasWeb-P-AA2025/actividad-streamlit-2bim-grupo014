from sqlalchemy.orm import sessionmaker
from generador_tablas import engine, Publicacion

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

# Consulta 2: Reacciones a una publicación
contenido_publicacion = "Bruno Fernandes del Liverpool fue expulsado por doble amarilla en el debut de la temporada."

publicacion = session.query(Publicacion).filter_by(contenido=contenido_publicacion).first()
if publicacion:
    for reaccion in publicacion.reacciones:
        print(f"- {reaccion.usuario.nombre}: {reaccion.tipo_emocion}")
else:
    print("Publicación no encontrada.")
