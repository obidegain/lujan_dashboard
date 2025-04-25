from data import manual_summary_dfs, groups, summary_paragraphs, columns_to_exclude_from_plot
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

st.title('Informe de Preferencias para el Viaje a Luján')
st.header('Introducción')
st.write("""
La emoción se siente en el aire mientras nos preparamos para este tan esperado viaje de parejas amigas a una casa quinta en Luján.
Dejando atrás la rutina, nos aventuramos en esta escapada con la promesa de risas, buena compañía y momentos inolvidables.
Para asegurar que cada detalle de nuestra convivencia sea perfecto y que todos disfrutemos al máximo, hemos recopilado las preferencias a través de un formulario.
Este informe detalla las respuestas obtenidas, brindándonos una guía para organizar desde las comidas hasta los pequeños gustos que harán de este viaje una experiencia espectacular.
¡Prepárense para la diversión y el disfrute en Luján!
""")

# Create tabs for each main group
tab_titles = list(groups.keys())
tabs = st.tabs([title.capitalize() for title in tab_titles])

# Populate each tab
for i, tab in enumerate(tabs):
    with tab:
        group_title = tab_titles[i]
        st.header(group_title.capitalize())
        st.write(summary_paragraphs.get(group_title, "No hay resumen disponible para esta sección."))

        if isinstance(groups[group_title], list):
            # Handle simple groups (lists of columns)
            if len(groups[group_title]) > 1:
                # If the group has more than one column, put each column in an expander
                for column in groups[group_title]:
                    if column in manual_summary_dfs:
                        with st.expander(f'{column}'):
                            st.dataframe(manual_summary_dfs[column])

                            if column not in columns_to_exclude_from_plot and not manual_summary_dfs[column].empty and len(manual_summary_dfs[column]) <= 15:
                                fig, ax = plt.subplots()
                                ax.pie(manual_summary_dfs[column]['Count'], labels=manual_summary_dfs[column].index, autopct='%1.1f%%', startangle=140)
                                ax.set_title(f'Distribución de respuestas para "{column}"')
                                ax.axis('equal')
                                st.pyplot(fig)
                                plt.close(fig)
            else:
                # If the group has only one column, display it directly
                 for column in groups[group_title]:
                    if column in manual_summary_dfs:
                        st.subheader(f'{column}')
                        st.dataframe(manual_summary_dfs[column])

                        if column not in columns_to_exclude_from_plot and not manual_summary_dfs[column].empty and len(manual_summary_dfs[column]) <= 15:
                            fig, ax = plt.subplots()
                            ax.pie(manual_summary_dfs[column]['Count'], labels=manual_summary_dfs[column].index, autopct='%1.1f%%', startangle=140)
                            ax.set_title(f'Distribución de respuestas para "{column}"')
                            ax.axis('equal')
                            st.pyplot(fig)
                            plt.close(fig)

        else:
            # Handle nested groups (like 'comidas') using expanders for sub-groups
            for sub_group_title, sub_group_columns in groups[group_title].items():
                with st.expander(sub_group_title.capitalize()):
                    st.write(summary_paragraphs.get(sub_group_title, "No hay resumen disponible para esta sub-sección."))
                    for column in sub_group_columns:
                        if column in manual_summary_dfs:
                            st.markdown(f"**{column}**") # Use markdown for column names within sub-groups
                            st.dataframe(manual_summary_dfs[column])

                            if column not in columns_to_exclude_from_plot and not manual_summary_dfs[column].empty and len(manual_summary_dfs[column]) <= 15:
                                fig, ax = plt.subplots()
                                ax.pie(manual_summary_dfs[column]['Count'], labels=manual_summary_dfs[column].index, autopct='%1.1f%%', startangle=140)
                                ax.set_title(f'Distribución de respuestas para "{column}"')
                                ax.axis('equal')
                                st.pyplot(fig)
                                plt.close(fig)


# Note about excluded columns
st.sidebar.header("Columnas no graficadas")
st.sidebar.write("Las siguientes columnas no fueron graficadas debido a su naturaleza (identificadores) o a la gran cantidad de respuestas únicas:")
for col in columns_to_exclude_from_plot:
    st.sidebar.write(f"- {col}")