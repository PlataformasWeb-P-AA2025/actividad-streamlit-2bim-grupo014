from sqlalchemy.orm import sessionmaker
from generador_tablas import engine, Reaccion, Usuario

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

# Consulta 5: Reacciones de tipo "alegre", "enojado", "pensativo" 
#de usuarios que NO inicien con vocal
emociones = ["alegre", "enojado", "pensativo"]
reacciones_filtradas = (session.query(Reaccion).join(Usuario)
                                               .filter(Reaccion.tipo_emocion.in_(emociones),Usuario.nombre.op('REGEXP')('^[^aeiouAEIOU]'))
                                               .all())

for r in reacciones_filtradas:
    print(f"- {r.usuario.nombre}: {r.tipo_emocion} en '{r.publicacion.contenido}'")
