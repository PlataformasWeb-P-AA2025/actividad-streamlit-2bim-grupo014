# streamlit_explorar.py

import streamlit as st
from db import get_session

# Importa las clases que definiste en clases.py
from generador_tablas import  Usuario, Publicacion, Reaccion


st.set_page_config(page_title="Explorador de objetos SQLAlchemy", layout="wide")


def listar_usuarios():
    """
    Muestra todos los usuarios y, en un expander, sus cursos con título y profesor.
    """
    st.header("Usuarios")
    session = get_session()
    usuarios = session.query(Usuario).all()


    if not usuarios:
        st.info("No hay registros en 'usuario'.")
        session.close()
        return


    session.close()


def listar_publicacion():
    """
    Muestra todas las publicaciones con detalle de curso e instructor.
    """
    st.header("Publicacion")
    session = get_session()
    publicaciones = session.query(Publicacion).all()

    if not publicaciones:
        st.info("No hay registros en 'publicaciones'.")
        session.close()
        return

    filas = []
    for p in publicaciones:
        filas.append({
            "Contenido" : p.contenido,
            "Usuario" : p.usuario_id
            
        })
    st.table(filas)
    session.close()

def listar_reaccion():
    """
    Muestra todas las reacciones
    """
    st.header("Reacciones")
    session = get_session()
    reac = session.query(Reaccion).all()

    if not reac:
        st.info("No hay registros en 'reaccion'.")
        session.close()


    for r in reac:
        with st.expander(f"ID {r.id} → {r.tipo_emocion }", expanded=False):
            st.write(f"**ID:** {r.id}")
            st.write(f"**Nombre Emocion:** {r.tipo_emocion}")

            # Inscripciones publicacion_id
            if r.publicaciones:
                st.write("**Publicaciones:**")
                filas_ins = []
                for pub in r.publicaciones:
                    filas_ins.append({
                        "Curso ID": pub.publicacion.id,
                        "Título curso": pub.publicacion.contenido
                    })
                st.table(filas_ins)
            else:
                st.write("_El estudiante no está inscrito en ningún curso._")


    session.close()



def main():
    st.title("Explorador de objetos SQLAlchemy en Streamlit")

    entidad = st.sidebar.selectbox(
        "Elija la entidad que desea explorar:",
        (
            "Usuarios",
            "Publicacion",
            "Reaccion",
        ),
    )

    if entidad == "Usuario":
        listar_usuarios()
    elif entidad == "Publicacion":
        listar_publicacion()
    elif entidad == "Reaccion":
        listar_reaccion()



if __name__ == "__main__":
    main()
