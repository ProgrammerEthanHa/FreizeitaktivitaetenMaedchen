import streamlit as st
import pandas as pd
import altair as alt

st.header("Häufige Freizeitaktivitäten von Mädchen")
st.subheader("Was machst Du häufig in Deiner Freizeit?")

source = pd.DataFrame({
        'Prozent(%)': [79, 63, 48, 47, 36, 36, 36, 29, 26, 26],
        'Aktivitäten': ['Freunde treffen', 'Musik hören', 'Rad fahren', 'Malen, Zeichen', 'Mit Tieren beschäftigen', 'Gymnastik, Tanzen', 'Bücher lesen', 'Mit Puppen spielen', 'Hörspiele anhören', 'Schwimmen']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Prozent(%):Q',
        x='Aktivitäten:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    6-13 Jahre; Mädchen
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: Ehapa Verlag")