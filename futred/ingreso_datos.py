import csv
from sqlalchemy.orm import sessionmaker
from generador_tablas import Usuario, Publicacion, Reaccion, engine

# Crear la sesión
Session = sessionmaker(bind=engine)
session = Session()

# Cargar usuarios desde usuarios_red_x.csv
with open('../DATA/usuarios_red_x.csv', newline='', encoding='utf-8') as archivo:
    reader = csv.DictReader(archivo)
    for fila in reader:
        nombre_usuario = fila['usuario']
        if not session.query(Usuario).filter_by(nombre=nombre_usuario).first():
            session.add(Usuario(nombre=nombre_usuario))

# Cargar publicaciones desde usuarios_publicaciones.csv
with open('../DATA/usuarios_publicaciones.csv', newline='', encoding='utf-8') as archivo:
    reader = csv.DictReader(archivo, delimiter='|')
    for fila in reader:
        nombre_usuario = fila['usuario']
        contenido = fila['publicacion']
        usuario = session.query(Usuario).filter_by(nombre=nombre_usuario).first()
        if usuario:
            if not session.query(Publicacion).filter_by(contenido=contenido).first():
                session.add(Publicacion(contenido=contenido, usuario=usuario))

session.commit()

# Cargar reacciones desde usuario_publicacion_emocion.csv
with open('../DATA/usuario_publicacion_emocion.csv', newline='', encoding='utf-8') as archivo:
    reader = csv.DictReader(archivo, delimiter='|')
    for fila in reader:
        nombre_usuario = fila['Usuario']
        comentario = fila['comentario']
        emocion = fila['tipo emocion']

        usuario = session.query(Usuario).filter_by(nombre=nombre_usuario).first()
        publicacion = session.query(Publicacion).filter_by(contenido=comentario).first()

        if usuario and publicacion:
            if not session.query(Reaccion).filter_by(usuario=usuario, publicacion=publicacion).first():
                session.add(Reaccion(tipo_emocion=emocion, usuario=usuario, publicacion=publicacion))

session.commit()
session.close()