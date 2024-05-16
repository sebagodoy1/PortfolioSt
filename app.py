import streamlit as st
import streamlit_shadcn_ui as ui

resume_file = "assets/CV.pdf"
resume_file_name = "CV - Sebastian Godoy - Data.pdf"
profile_pic = "assets/profile.png"
css_file = "styles/main.css"

name = "Sebastián Godoy"
description = "Data Scientist con background como contador, enfocado en construir aplicaciones y automatizar procesos para facilitar tu vida."

layout = "centered"
page_title = "Portfolio | Sebastián Godoy"
page_icon = "👨‍🎓"

email = "sebajgodoy@gmail.com"
social_media = {
    "Linkedin": "https://www.linkedin.com/in/sebagodoy/",
    "Github": "https://github.com/sebagodoy1",
    "Email": "sebajgodoy@gmail.com"
}

proyectos = {
    "🏆Detección de fraude en tarjetas de crédito":"https://github.com/sebagodoy1/Credit-Card-Fraud-Detection-Model",
    "🏆E-commerce Machine Learning Analysis": "https://github.com/sebagodoy1/Project_E-commerce-ML",
    "🏆Website hecho con FastAPI y SQL en Python":"https://github.com/sebagodoy1/Project_FastAPI_Form1",
    "🏆User Cohort Retention Analysis": "https://github.com/sebagodoy1/User-cohort-retention-analysis",
}

#Conf Pag
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

#--Load CSS
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFByte = pdf_file.read()

cols = st.columns(len(social_media))
for index, (platform, link) in enumerate(social_media.items()):
    with cols[index]:
        ui.link_button(text=platform, url=link, key=f"link_btn_{platform}", class_name="custom-button")

#HEADER
col1, col2 = st.columns(2)
with col1:
    st.image(profile_pic, width=230)
 
with col2:
    st.title(name)
    st.write(description)
    st.download_button(
        label= "📥 Descargar CV",
        data=PDFByte,
        file_name=resume_file_name,
    )
    st.write("📬", email)

#--Proyectos--
st.write("##")
st.subheader("👨‍🏫 Proyectos")
st.write("---")

for project, link in proyectos.items():
    st.write(f"[{project}]({link})")

#--Habilidades Tec
st.write("##")
st.subheader("🛠️ Tech Stack")
st.write("---")
st.write("""
- 💻 Python | Numpy | Pandas | Google Sheet | SQL
- 💹 Power BI | Tableau | FastAPI | Streamlit
- 📊 Matplotlib | SK Learn | Seaborn | Machine Learning
- 🔧 Git | Jupyter Notebook | Scrum
- ☁️ GCP | Google Colab | Web Scraping 
         """
)

#--Experiencia
st.write("##")
st.subheader("Experiencia")
st.write("---")

#TRABAJO ACT
st.write("👨🏻‍💻", "**Financial Data Analyst**", "- Ingenes (México)")
st.write("08/2023 - Presente")
st.write("""
- ✅ A cargo del área de Finanzas.
- ✅ Automatización de procesos de datos utilizando Python, SQL y Google Sheets.
- ✅ Creación de Reportes en Power Bi para la toma de decisiones. 
- ✅ Bots de RPA con Pyautogui.         
                 """)

#TRABAJO 2
st.write("👨🏻‍💻", "**Backend Data Scientist**", "- Videsk (Chile)")
st.write("06/2023 - 08/2023")
st.write("""
- ✅ Realice la implementación de un sistema de mirror en streaming que replicaba datos de MongoDB (NoSQL) a BigQuery (SQL) para facilitar análisis y visualización de datos. 
- ✅ Utilizando JavaScript, Google Cloud y enfoques serverless, logramos mejorar significativamente el tiempo de procesamiento de datos, lo que resultó en análisis más eficientes y toma de decisiones más informadas. 
- ✅ Además, desarrollé habilidades en arquitectura de datos y resolución de problemas en un entorno de alto rendimiento.         
                 """)

#TRABAJO 3
st.write("👨🏻‍💻", "**Data Scientist**", "- Social Media Lab ai (España)")
st.write("05/2023 - 06/2023")
st.write("""
- ✅ ETL en Python, sobre la DB en MongoDb. 
- ✅ Dashboards en Power BI. 
- ✅ Scraping de datos con Selenium.         
                 """)