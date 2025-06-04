from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from generador_tablas import engine, Publicacion, Usuario

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

# Consulta 6: Usuarios que han hecho más de una publicación

usuarios_multiples = session.query(
    Usuario.nombre, func.count(Publicacion.id).label("num_pub")
).join(Publicacion).group_by(Usuario.id).having(func.count(Publicacion.id) > 1).all()

for nombre, num in usuarios_multiples:
    print(f"- {nombre}: {num} publicaciones")
