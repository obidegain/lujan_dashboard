import pandas as pd

# Dictionary to store the manually created summary DataFrames
manual_summary_dfs = {}

# DataFrame for 'Marca temporal'
manual_summary_dfs['Marca temporal'] = pd.DataFrame({
    'Count': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'Percentage': [6.67, 6.67, 6.67, 6.67, 6.67, 6.67, 6.67, 6.67, 6.67, 6.67, 6.67, 6.67, 6.67, 6.67, 6.67]
}, index=['2025-04-23 23:56:00', '2025-04-23 23:58:11', '2025-04-23 23:58:58', '2025-04-24 00:03:12', '2025-04-24 00:04:25', '2025-04-24 00:27:32', '2025-04-24 08:24:07', '2025-04-24 08:24:51', '2025-04-24 08:55:59', '2025-04-24 16:34:50', '2025-04-24 16:37:19', '2025-04-24 16:39:46', '2025-04-24 16:56:27', '2025-04-24 17:23:40', '2025-04-24 17:30:14'])

# DataFrame for 'Dirección de correo electrónico'
manual_summary_dfs['Dirección de correo electrónico'] = pd.DataFrame({
    'Count': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'Percentage': [6.67, 6.67, 6.67, 6.67, 6.67, 6.67, 6.67, 6.67, 6.67, 6.67, 6.67, 6.67, 6.67, 6.67, 6.67]
}, index=['octa.bidegain@gmail.com', 'maguwalker19@gmail.com', 'damianponce993@gmail.com', 'cami.baiardi@gmail.com', 'gentilimauricio@gmail.com', 'ary.mdq@gmail.com', 'patriciofacciolo@gmail.com', 'gonzalobadia@gmail.com', 'augusto.borelli18@gmail.com', 'martinamedicaf@gmail.com', 'vale.trua@gmail.com', 'matipalotta@gmail.com', 'agustinalrabini@gmail.com', 'vic.mdq7@gmail.com', 'juli.castilla4@gmail.com'])

# DataFrame for 'Identificate:'
manual_summary_dfs['Identificate:'] = pd.DataFrame({
    'Count': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'Percentage': [6.25, 6.25, 6.25, 6.25, 6.25, 6.25, 6.25, 6.25, 6.25, 6.25, 6.25, 6.25, 6.25, 6.25, 6.25, 6.25]
}, index=['Octa', 'Tu señora', 'El Carava', 'Camiiiiiiii', 'El Presidente', 'Ary', 'alias el turco o el fenómeno', 'Pato 🦆', 'Marcelo moretti', 'Tito', 'Martu', 'laone', 'Pin Pin Palotin', 'Agus', 'Vicky', 'La chuli'])

# DataFrame for '¿Que infusión te gusta? Desayuno'
manual_summary_dfs['Infusión - Desayuno'] = pd.DataFrame({
    'Count': [13, 2],
    'Percentage': [86.67, 13.33]
}, index=['Mate', 'Té'])

# DataFrame for '¿Endulzas la infusión? Desayuno'
manual_summary_dfs['¿Endulzas la infusión? Desayuno'] = pd.DataFrame({
    'Count': [13, 2],
    'Percentage': [86.67, 13.33]
}, index=['No', 'Si'])

# DataFrame for '¿Le agregas lechita? Desayuno'
manual_summary_dfs['¿Le agregas lechita? Desayuno'] = pd.DataFrame({
    'Count': [15],
    'Percentage': [100.00]
}, index=['No'])

# DataFrame for '¿Qué te gusta comer a la mañana? (además de eso que ya sabemos 🍆🍑💦)'
manual_summary_dfs['Comida Desayuno'] = pd.DataFrame({
    'Count': [13, 12, 12, 9, 7, 3, 1],
    'Percentage': [22.81, 21.05, 21.05, 15.79, 12.28, 5.26, 1.75]
}, index=['Tostadas', 'Huevo', 'Queso', 'Frutas', 'Palta', 'Galletitas saladas', 'Galletitas dulces'])

# DataFrame for '¿Que infusión te gusta? Merienda'
manual_summary_dfs['Infusión Merienda'] = pd.DataFrame({
    'Count': [15, 5, 3],
    'Percentage': [65.22, 21.74, 13.04]
}, index=['Mate', 'Cafe', 'Té'])

# DataFrame for '¿Endulzas la infusión? Merienda'
manual_summary_dfs['¿Endulzas la infusión? Merienda'] = pd.DataFrame({
    'Count': [13, 2],
    'Percentage': [86.67, 13.33]
}, index=['No', 'Si'])

# DataFrame for '¿Le agregas lechita? Merienda'
manual_summary_dfs['¿Le agregas lechita? Merienda'] = pd.DataFrame({
    'Count': [13, 2],
    'Percentage': [86.67, 13.33]
}, index=['No', 'Si'])

# DataFrame for '¿Qué te gusta comer después de la siestita? (además de eso que ya sabemos 🍆🍑💦)'
manual_summary_dfs['Comida Merienda'] = pd.DataFrame({
    'Count': [10, 9, 8, 8, 7, 6, 5],
    'Percentage': [18.87, 16.98, 15.09, 15.09, 13.21, 11.32, 9.43]
}, index=['Tostadas', 'Queso', 'Huevo', 'Frutas', 'Galletitas dulces', 'Galletitas saladas', 'Palta'])

# DataFrame for 'Asado: Preferentemente, ¿Qué comés? (además de eso que ya sabemos todo, golos@)'
manual_summary_dfs['Asado'] = pd.DataFrame({
    'Count': [15, 11, 10, 9, 9, 8, 7, 7, 3, 3, 1],
    'Percentage': [18.07, 13.25, 12.05, 10.84, 10.84, 9.64, 8.43, 8.43, 3.61, 3.61, 1.20]
}, index=['Vacio', 'Asado', 'Chorizo', 'Tapa de asado', 'Bondiola', 'Morcilla', 'Salchicha parrillera', 'Matambres', 'Pata muslo', 'Pechuga', 'Todo lo que pueda entrar en una parrilla. bicho que camine se come'])

# DataFrame for '¿Con qué acompañas el asadito?'
manual_summary_dfs['¿Con qué acompañas el asadito?'] = pd.DataFrame({
    'Count': [12, 12, 12, 12, 11, 4],
    'Percentage': [19.05, 19.05, 19.05, 19.05, 17.46, 6.35]
}, index=['Ensalada básica (lechuga', 'tomate', 'zanahoria', 'huevo)', 'Papa y huevo', 'Ensalada premium (con palta) (todo bien con que seas puto pero no seas trolo man)'])

# DataFrame for 'Mira como esta el diaaaaaa, ¿De qué preferis el guisito?'
manual_summary_dfs['Guiso'] = pd.DataFrame({
    'Count': [12, 3,],
    'Percentage': [80.00, 20.00, ]
}, index=['Lentejas', 'Fideo moñito',])

# DataFrame for 'A la pasta, ¿Qué salsita le ponemos?'
manual_summary_dfs['Pasta'] = pd.DataFrame({
    'Count': [9, 9, 3, 1],
    'Percentage': [40.91, 40.91, 13.64, 4.55]
}, index=['Bolognesa', 'Rosa', 'Fileto', 'Solo crema'])

# DataFrame for 'Comes...'
manual_summary_dfs['Queso - Pasta'] = pd.DataFrame({
    'Count': [9, 6],
    'Percentage': [60.00, 40.00]
}, index=['Queso con pastas', 'Pastas con queso'])

# DataFrame for 'Te gusta mojar el pancito en la salcita????'
manual_summary_dfs['Pancito - Pasta'] = pd.DataFrame({
    'Count': [14, 1],
    'Percentage': [93.33, 6.67]
}, index=['Si', 'No'])

# DataFrame for 'La picadita va a estar, asique esta no es una pregunta. Escribí lo que quieras'
manual_summary_dfs['Picada'] = pd.DataFrame({
    'Count': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'Percentage': [6.67, 6.67, 6.67, 6.67, 6.67, 6.67, 6.67, 6.67, 6.67, 6.67, 6.67, 6.67, 6.67, 6.67, 6.67]
}, index=['Que buen forms la re puta madre', 'A vos te quiero', 'Con todos los embutidos que puedan tapar arterias. Soy fan de los quesos', 'Y acá te regalaste jajaja', 'Val sigue enojada', 'Me hiciste reír mucho hdp jaja', 'Salamin y queso fuerte al medio', 'Tito termo asqueroso', 'Hola', 'Silicon Valley', 'papitas coto', 'Ever Bush', 'Nos vemo el sabadoooo', '🙌🏻🙌🏻🙌🏻', 'Así me gusta'])

# DataFrame for 'Momento más esperado: Las pippppppshas. Elegí tus gustitos'
manual_summary_dfs['Pizzas'] = pd.DataFrame({
    'Count': [11, 10, 10, 9, 8, 8, 8, 5, 1],
    'Percentage': [15.71, 14.29, 14.29, 12.86, 11.43, 11.43, 11.43, 7.14, 1.43]
}, index=['Jamon y morron', 'Muzza', 'Rucula y Jamon Crudo', 'Champi', 'Jamon y huevo', 'Napo (con poco ajo', 'je)', '4 quesos', 'Todo excepto agregarle ananá. Es de trolo'])

# DataFrame for '¿Que talco un arroz con poio?'
manual_summary_dfs['Arroz con pollo'] = pd.DataFrame({
    'Count': [13, 2],
    'Percentage': [86.67, 13.33]
}, index=['Sí', 'No'])

# DataFrame for '¿Qué te gustaría tomar? (No vale 🥛🐮)'
manual_summary_dfs['Bebidas'] = pd.DataFrame({
    'Count': [12, 12, 11, 5, 5, 4, 1, 1, 1],
    'Percentage': [23.08, 23.08, 21.15, 9.62, 9.62, 7.69, 1.92, 1.92, 1.92]
}, index=['Vino tinto', 'Vermú', 'Fernet con coca', 'Fernet con pomelo', 'Birra cualquiera', 'Birra solo ipa', 'Vino blanco', 'Falopa', 'Gin tonic / pomelic'])

# DataFrame for 'Si no tomás alcohol o queres tomar algo solo...'
manual_summary_dfs['Bebidas sin alcohol'] = pd.DataFrame({
    'Count': [11, 5, 2, 2, 1, 1, 1, 1],
    'Percentage': [45.83, 20.83, 8.33, 8.33, 4.17, 4.17, 4.17, 4.17]
}, index=['Agua', 'Coca', 'Pomelo', 'Sprite', 'Cocaina', 'COCA ZERO', 'Aire fresco', 'Malas decisiones'])

# DataFrame for '¿Qué te gusta meterte en la boca?'
manual_summary_dfs['Dulces'] = pd.DataFrame({
    'Count': [11, 11, 7, 5, 5],
    'Percentage': [28.21, 28.21, 17.95, 12.82, 12.82]
}, index=['Gomitas', 'Chocolate', 'Caramelos', 'Chocotorta', 'Alfajores'])

# DataFrame for 'Va a haber panaderia, elegí bien:'
manual_summary_dfs['Panaderia'] = pd.DataFrame({
    'Count': [13, 12, 8, 5, 4],
    'Percentage': [30.95, 28.57, 19.05, 11.90, 9.52]
}, index=['Chipa', 'Pasta frola', 'Pepas', 'Palmeritas', 'Cuernitos'])

# DataFrame for 'Alguna comida que no se mencionó y te gustaría?'
manual_summary_dfs['Comidas extras'] = pd.DataFrame({
    'Count': [2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'Percentage': [11.76, 11.76, 5.88, 5.88, 5.88, 5.88, 5.88, 5.88, 5.88, 5.88, 5.88, 5.88, 5.88, 5.88, 5.88]
}, index=['Hamburguesas', '-', 'Nada en especial', 'Esa que vos conoces 🍆🍑💦', 'Tamosok', 'Fatay', 'burger (paty sino Val se enoja)', 'Falopa', 'Pancheaux', 'No', 'Yuyi', 'ositos haribo', 'Fajitas', 'Panchitossss', 'Panchitos'])

groups = {
    'desayuno': ['¿Que infusión te gusta? Desayuno', '¿Endulzas la infusión? Desayuno', '¿Le agregas lechita? Desayuno', 'Comida Desayuno'],
    'merienda': ['¿Que infusión te gusta? Merienda', '¿Endulzas la infusión? Merienda', '¿Le agregas lechita? Merienda', 'Comida Merienda'],
    'comidas': {
        'asado': ['Asado', '¿Con qué acompañas el asadito?'],
        'picadita': ['Picada'],
        'pizzas': ['Pizzas'],
        'pasta': ['Pasta', 'Queso - Pasta', 'Pancito - Pasta'],
        'guisito': ['Guiso'],
        'arroz': ['Arroz con pollo'],
        'extras': ['Comidas extras'],
    },
    'bebidas': ['Bebidas', 'Bebidas sin alcohol'],
    'snacks': ['Dulces'],
    'panaderia': ['Panaderia'],
}

summary_paragraphs = {
    'desayuno': "En el desayuno, la gran mayoría prefiere Mate como infusión (86.67%), y la mayoría no la endulza (86.67%) ni le agrega leche (100%). Para comer a la mañana, las opciones más populares son Tostadas, Huevo y Queso, todas con más del 21% de preferencia. Frutas y Palta también son opciones consideradas por una parte importante del grupo.",
    'merienda': "Para la merienda, el Mate sigue siendo la infusión predilecta (65.22%), aunque el Cafe y el Té también tienen sus adeptos. Al igual que en el desayuno, la mayoría no endulza la infusión (86.67%) ni le agrega leche (86.67%). En cuanto a qué comer, las Tostadas, el Queso, el Huevo y las Frutas son las opciones más elegidas, todas superando el 15% de preferencia.",
    'comidas': "Aquí se detallan las preferencias para las comidas principales, incluyendo asado, picadita, pizzas, pasta, guisito, arroz y extras.",
    'asado': "En cuanto al asado, el Vacío es la opción más popular (18.07%), seguido por Asado, Chorizo y Tapa de asado/Bondiola (todas superando el 10%). La mayoría prefiere acompañarlo con Ensalada básica y Papa y huevo.",
    'picadita': "La sección de la picadita muestra una variedad de comentarios y preferencias libres por parte de los participantes.",
    'pizzas': "Las pippppppshas más esperadas son las de Jamón y morrón, Muzza y Rúcula con jamón crudo, que lideran las preferencias del grupo.",
    'pasta': "En pastas, las salsas Bolognesa y Rosa tienen la misma popularidad (40.91% cada una). La mayoría come Pastas con queso y casi todos disfrutan de mojar el pancito en la salcita (93.33%).",
    'guisito': "Para el guiso, la Lentejas son las claras favoritas (66.67%).",
    'arroz': "La gran mayoría (86.67%) está de acuerdo con un arroz con poio.",
    'extras': "La sección de 'Alguna comida que no se mencionó' muestra una variedad de sugerencias individuales.",
    'bebidas': "Para tomar con alcohol, el Vino tinto y el Vermú son los más elegidos, seguidos de cerca por Fernet con coca. Para opciones sin alcohol, el Agua es la preferida (45.83%), seguida por la Coca (20.83%).",
    'snacks': "Entre los gustos para 'meterse en la boca', las Gomitas y el Chocolate son los favoritos (ambos 28.21%).",
    'panaderia': "Finalmente, en panadería, el Chipa es el más votado (30.95%), seguido por Pasta frola (28.57%) y Pepas (19.05%)."
}

columns_to_exclude_from_plot = ['Marca temporal', 'Dirección de correo electrónico', 'Identificate:',]
