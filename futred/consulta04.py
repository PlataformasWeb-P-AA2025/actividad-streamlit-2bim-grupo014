from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from generador_tablas import engine, Reaccion

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

# Consulta 4: Reporte de reacciones en función del número de veces que fueron usadas
conteo = session.query(
    Reaccion.tipo_emocion,
    func.count(Reaccion.id).label('cantidad')
).group_by(Reaccion.tipo_emocion).order_by(func.count(Reaccion.id).desc()).all()

for tipo, cantidad in conteo:
    print(f"- {tipo}: {cantidad} veces")
