from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from generador_tablas import engine, Usuario, Reaccion

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

# Consulta 9: Emoción más común por usuario

subquery = session.query(
    Reaccion.usuario_id,
    Reaccion.tipo_emocion,
    func.count(Reaccion.id).label("conteo")
).group_by(Reaccion.usuario_id, Reaccion.tipo_emocion).subquery()

usuarios = session.query(Usuario).all()
for u in usuarios:
    emocion_dominante = session.query(
        subquery.c.tipo_emocion
    ).filter(subquery.c.usuario_id == u.id).order_by(subquery.c.conteo.desc()).first()
    if emocion_dominante:
        print(f"- {u.nombre}: emoción más común = {emocion_dominante[0]}")
