import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="Streamlit Component Showcase", layout="wide")

# Título e Introdução
st.title("🔗 Streamlit Component Showcase")
st.markdown("Explore os principais componentes do Streamlit com exemplos interativos.")

# 1. Text Components
st.header("📝 Text Components")
st.subheader("1. st.write")
st.write("Streamlit é uma ferramenta incrível para criar aplicações web com Python!")
st.text("Texto simples sem formatação.")
st.markdown("**Markdown** é muito útil para formatação.")
st.code("st.write('Hello, Streamlit!')", language="python")

# 2. Media Components
st.header("🖼️ Media Components")
st.subheader("2. st.image")
st.image("data:image/png;base64,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", caption="Imagem do google", use_container_width=True)

st.subheader("3. st.video")
st.video("https://www.youtube.com/watch?v=JM6pDH9udCQ&t=751s")

st.subheader("4. st.audio")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3")

# 3. Data Display Components
st.header("📊 Analises de Tabelas")
st.subheader("5. st.dataframe")
data = pd.DataFrame(np.random.randn(10, 5), columns=[f'Col {i}' for i in range(1, 6)])
st.dataframe(data)

st.subheader("6. st.table")
st.table(data.head())

st.subheader("7. st.metric")
st.metric(label="Temperatura", value="25 °C", delta="-2 °C")

# 4. Input Components
st.header("📝 Input Components")
st.subheader("8. st.text_input")
name = st.text_input("Digite seu nome:")
st.write(f"Olá, {name}!")

st.subheader("9. st.text_area")
feedback = st.text_area("Deixe seu feedback:")
st.write(f"Feedback recebido: {feedback}")

st.subheader("10. st.number_input")
number = st.number_input("Escolha um número", min_value=0, max_value=100, step=1)
st.write(f"Você escolheu: {number}")

st.subheader("11. st.slider")
slide_value = st.slider("Ajuste o valor", 0, 100, 50)
st.write(f"Valor do slider: {slide_value}")

st.subheader("12. st.selectbox")
option = st.selectbox("Escolha uma linguagem de programação", ["Python", "JavaScript", "C#", "Ruby"])
st.write(f"Você escolheu: {option}")

st.subheader("13. st.checkbox")
checkbox = st.checkbox("Marque para confirmar")
st.write(f"Checkbox marcado: {checkbox}")

st.subheader("14. st.radio")
radio = st.radio("Escolha uma cor", ["Vermelho", "Verde", "Azul"])
st.write(f"Cor escolhida: {radio}")

st.subheader("15. st.button")
if st.button("Clique aqui"):
    st.write("Você clicou no botão!")

# 5. Visualization Components
st.header("📊 Visualization Components")
st.subheader("16. st.line_chart")
st.line_chart(data)

st.subheader("17. st.bar_chart")
st.bar_chart(data)

st.subheader("18. st.pyplot")
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
ax.set_title("Gráfico com Matplotlib")
st.pyplot(fig)

# 6. Status Components
st.header("🕒 Status Componentes")
st.subheader("19. st.progress")
progress = st.progress(0)
for i in range(100):
    time.sleep(0.05)
    progress.progress(i + 1)

st.subheader("20. st.spinner")
with st.spinner("Carregando..."):
    time.sleep(2)
st.success("Carregamento concluído!")

# Footer
st.markdown("---")
st.markdown("Feito com 💙 por Michael Oliveira - Aluno da Jornanda de Dados com Luciano Vasconcelos")