from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from generador_tablas import engine, Publicacion, Reaccion

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

# Consulta 8: Usuarios que reaccionaron a publicaciones de otros (no propias)

reacciones_ajenas = session.query(Reaccion).join(Publicacion).filter(
    Reaccion.usuario_id != Publicacion.usuario_id
).all()

for r in reacciones_ajenas:
    print(f"- {r.usuario.nombre} reaccionó a publicación de {r.publicacion.usuario.nombre}")
