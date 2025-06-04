from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)

    publicaciones = relationship('Publicacion', back_populates='usuario')
    reacciones = relationship('Reaccion', back_populates='usuario')

class Publicacion(Base):
    __tablename__ = 'publicaciones'
    id = Column(Integer, primary_key=True)
    contenido = Column(String, nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))

    usuario = relationship('Usuario', back_populates='publicaciones')
    reacciones = relationship('Reaccion', back_populates='publicacion')

class Reaccion(Base):
    __tablename__ = 'reacciones'
    id = Column(Integer, primary_key=True)
    tipo_emocion = Column(String, nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    publicacion_id = Column(Integer, ForeignKey('publicaciones.id'))

    usuario = relationship('Usuario', back_populates='reacciones')
    publicacion = relationship('Publicacion', back_populates='reacciones')

    __table_args__ = (
        UniqueConstraint('usuario_id', 'publicacion_id', name='uq_usuario_publicacion'),
    )

Base.metadata.create_all(engine)
