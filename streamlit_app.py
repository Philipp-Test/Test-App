import streamlit as st

import streamlit as st
from pathlib import Path

def get_file_content_as_bytes(file_path):
    with open(file_path, "rb") as file:
        return file.read()

# Pfad zur PDF-Datei
file_path = 'Lisa Bauer.pdf'

# Lese den Inhalt der PDF-Datei als Bytes
file_bytes = get_file_content_as_bytes(file_path)


left, right = st.columns([3,3], gap="medium")

image_url = "profile-pic2.png"

st.markdown("<style> .stAppHeader {display:none;} ul {list-style-type: none; } </style>", unsafe_allow_html=True)

with left:
    st.image(image_url, width=200)

with right:
    st.title("Lisa Bauer", anchor=None)
    st.markdown(f"""<em> <p>"Ich bin IT-Enthusiastin und Programmiererin, <br> die in dem Bereich eine echte Expertin werden möchte und gespannt auf die Zukunft ist."</p> </em>""", unsafe_allow_html=True)
    # Der Download-Button, der die Datei zur Verfügung stellt
    st.download_button(
        label="📄 Download CV",
        data=file_bytes,
        file_name=file_path,
        mime='application/pdf'
    )
    st.write("📩", "lisa.bauer@gmx.at")

st.write("\n")

st.header("IT-Kompetenzen", anchor=False, divider="blue")
st.markdown("""
- 🌍 **Webentwicklung:** Fundierte Grundkenntnisse in HTML, CSS und Streamlit (Fullstack-Framework)
- 💻 **Programmierung:** Praktische Erfahrung in Python, Entwicklung kleiner Anwendungen und Skripte
- 📊 **Office-Suite:** Versierter Umgang mit Microsoft Word, Excel und PowerPoint
- 🚀 **Eigene Projekte:** Konzeption und Umsetzung verschiedener Projekte inklusive Hosting
- 🎓 **Schulprojekte:** Erstellung datenbasierter Präsentationen und interaktiver Tabellenkalkulationen
""")

st.header("Schulbildung", anchor=False, divider="blue")
st.subheader("Fachmittelschule Schaumburgergasse, Wien")
st.markdown("""
- ► **Schwerpunkt:** Intensive IT-Spezialisierung, Fokus auf modernen Webtechnologien und Wirtschaft
- ► **Zeitraum:** September 2024 - Juli 2025
- ► **Derzeitiger Notenschnitt:** 1,5
""")

st.subheader("Mittelschule Kayniongasse, Wien")
st.markdown("""
- ► **Zeitraum:** September 2020 – Juli 2024
- ► **Abschluss-Notendurchschnitt:** 1,7
""")

st.header("Arbeitserfahrung", anchor=False, divider="blue")
st.markdown("""
- **💼 Berufspraktische Tage 1:** Bei XYZ von 18. bis 22. Nov. 2024
- **💼 Berufspraktische Tage 2:** Bei XYZ von 24. bis 28. Feb. 2025
""")

st.header("Zusätzliche Qualifikationen", anchor=False, divider="blue")
st.markdown("""
- ✨ **Schnelle Auffassungsgabe** für neue Softwareanwendungen und Technologien
- ✨ **Großes Interesse** an der kontinuierlichen Weiterentwicklung im IT-Bereich
- ✨ **Teamfähigkeit und Kommunikationsstärke** bei gemeinsamen Coding-Projekten
""")

st.header("Interessen und Hobbys", anchor=False, divider="blue")
st.markdown("""
- 🎈 **Fußball:** Mitglied in einem Fußball-Klub
- 🎈 **Lesen:** Begeisterte Leserin verschiedenster Literatur
- 🎈 **Schach:** Engagiert im Schachklub
""")