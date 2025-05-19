import streamlit as st
import pandas as pd

st.set_page_config(page_title="Comparador de Lentes de Contacto", layout="wide")

st.title("💡 Comparador de Lentes de Contacto")

# Leer CSV desde Google Sheets
csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ9t9T7xMOSNhffl_rYHM1LSE6ovS2_W76QQH2q0U1Xl-tnS_2WmM9w5avocMDvfA/pub?gid=413765965&single=true&output=csv"
df = pd.read_csv(csv_url)


# Calcular precios por lente
df['precio_unitario_sin_descuento'] = df.apply(
    lambda row: float(row['price_without_discount']) / float(row['quantity_per_package'])
    if row['price_without_discount'] and row['quantity_per_package'] else None, axis=1
)
df['precio_unitario_con_descuento'] = df.apply(
    lambda row: float(row['price_with_discount']) / float(row['quantity_per_package'])
    if row['price_with_discount'] and row['quantity_per_package'] else None, axis=1
)


st.write(f"Se tiene información de {len(df['Store Name'].unique())} ópticas y {len(df)} lentes diferentes.")

with st.expander("👓 Ver todos los lentes de una óptica", expanded=False):
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        optica_seleccionada = st.selectbox("Seleccioná una óptica:", df['Store Name'].unique())

    if optica_seleccionada:
        df_filtrado = df[df['Store Name'] == optica_seleccionada]

        st.markdown("### Lentes Scrappeados de una óptica")
        st.write(f"Se encontraron {len(df_filtrado)} coincidencias")

        df['price_without_discount'] = df['price_without_discount'].astype(float)
        st.markdown(f"**Nombre de la óptica:** {df_filtrado['Store Name'].values[0]}")
        st.markdown(f"**Nro Cuenta:** {df_filtrado['Nro Cuenta'].values[0]}")
        st.markdown(f"**Es Cliente Vitolen LC?:** {df_filtrado['Es Cliente Vitolen LC?'].values[0]}")
        st.markdown(f"**Link a la óptica:** {df_filtrado['URL'].values[0]}")

        st.dataframe(
            df_filtrado,
            column_order=['image_url', 'title', 'price_without_discount', 'precio_unitario_sin_descuento', 'discount_percentage', 'price_with_discount', 'extra_discounts', 'quantity_per_package', 'package_type', 'description'],
            column_config={
                'image_url': st.column_config.ImageColumn("Imagen", width="100px"),
                'title': st.column_config.TextColumn("Título"),
                'price_without_discount': st.column_config.NumberColumn("Precio sin descuento", format="$%.2f"),
                'precio_unitario_sin_descuento': st.column_config.NumberColumn("Precio unitario sin descuento", format="$%.2f"),
                'discount_percentage': st.column_config.NumberColumn("Descuento (%)"),
                'price_with_discount': st.column_config.NumberColumn("Precio con descuento", format="$%.2f"),
                'extra_discounts': st.column_config.TextColumn("Descuentos adicionales"),
                'quantity_per_package': st.column_config.NumberColumn("Cantidad por paquete"),
                'package_type': st.column_config.TextColumn("Tipo de paquete"),
                'description': st.column_config.TextColumn("Descripción")
            },
            hide_index=True,
        )
    else:
        st.warning("Por favor selecciona una óptica para ver los detalles.")


with st.expander("📊 Ver todos los lentes scrappeados", expanded=False):
    st.markdown("### Todos los lentes scrappeados")
    st.dataframe(
        df,
        column_order=['Store Name', 'Nro Cuenta', 'Es Cliente Vitolen LC?', 'image_url', 'title', 'price_without_discount', 'discount_percentage', 'price_with_discount', 'extra_discounts', 'quantity_per_package', 'package_type', 'description'],
        column_config={
            'image_url': st.column_config.ImageColumn("Imagen", width="100px"),
            'title': st.column_config.TextColumn("Título"),
            'price_without_discount': st.column_config.NumberColumn("Precio sin descuento", format="$%.2f"),
            'discount_percentage': st.column_config.NumberColumn("Descuento (%)"),
            'price_with_discount': st.column_config.NumberColumn("Precio con descuento", format="$%.2f"),
            'extra_discounts': st.column_config.TextColumn("Descuentos adicionales"),
            'quantity_per_package': st.column_config.NumberColumn("Cantidad por paquete"),
            'package_type': st.column_config.TextColumn("Tipo de paquete"),
            'description': st.column_config.TextColumn("Descripción"),
            'Es Cliente Vitolen LC?': st.column_config.TextColumn("Cliente Vitolen"),
        },
        hide_index=True,
    )