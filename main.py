import streamlit as st

st.title('Todo concluye al fin, nada puede escapar')
st.header('Nos vemos en el próximo viaje!')

with st.expander("Desbloqueen su sorpresa:", expanded=False):
    st.header("LOS RECONTRA RE MIL CAGO AMANDO (L)")
    st.image("https://i.postimg.cc/FKq4xHjP/Whats-App-Image-2025-05-03-at-18-45-26.jpg")
with st.expander("¿Quién es Usuario X?", expanded=False):
    with st.popover("¿Quién es Usuario X?"):
        st.write("Ese boton no era.")
        if st.button("Es este (:"):
            st.balloons()
            st.image("https://i.postimg.cc/g27zgspq/Whats-App-Image-2025-04-26-at-16-13-34.jpg")