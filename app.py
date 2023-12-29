import os
import sys

import streamlit as st
from dotenv import load_dotenv
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain_community.chat_models import ChatOpenAI

from read_and_textify_doc import read_and_textify

load_dotenv()
os.getenv("OPENAI_API_KEY")

__import__("pysqlite3")
sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")

st.set_page_config(
    layout="wide",
    page_title="Forecast Chatbot",
    page_icon=":robot_face:",
)

st.sidebar.header("Sobre o desenvolvedor")
nome = "Renato Moraes"
titulo = "Cientista de Dados"
linkedin_url = "https://linkedin.com/in/renato-moraes-11b546272"
github_url = "https://github.com/RenatoDev4"
github_projeto = "https://github.com/RenatoDev4/chatbot_documents"

st.sidebar.text(f"Nome: {nome}")
st.sidebar.text(f"Cargo: {titulo}")
st.sidebar.header("Redes sociais")
st.sidebar.markdown(
    f"**[LinkedIn]({linkedin_url})** | **[GitHub]({github_url})**"
)  # noqa
st.sidebar.header("GitHub do projeto")
st.sidebar.markdown(f"**[Link]({github_projeto})**")

st.sidebar.markdown("***")

st.sidebar.header("Sobre o Projeto")
st.sidebar.info(
    "Este projeto consiste em um ChatBot que oferece respostas a perguntas extraídas de documentos PDF ou TXT enviados pelo usuário ao servidor. A aplicação utiliza tecnologias de um modelo de linguagem da OpenAI para processar e compreender o conteúdo do documento. O usuário recebe respostas precisas e relevantes às suas perguntas, agilizando a busca por informações específicas nos documentos."
)


st.markdown(
    "<h1 style='text-align: center;'>Forecast documentation Chatbot</h1>",
    unsafe_allow_html=True,
)
st.write("---")

uploaded_files = st.file_uploader(
    "Faça o upload do documento", accept_multiple_files=True, type=["txt", "pdf"]
)
st.write("---")

if uploaded_files is None:
    st.info(f"Por favor faça o upload de um documento para análise")
elif uploaded_files:
    st.write(str(len(uploaded_files)) + " documento(s) carregados..")

    textify_output = read_and_textify(uploaded_files)

    documents = textify_output[0]
    sources = textify_output[1]

    embeddings = OpenAIEmbeddings()

    vStore = Chroma.from_texts(
        documents, embeddings, metadatas=[{"source": s} for s in sources]
    )

    retriever = vStore.as_retriever()
    retriever.search_kwargs = {"k": 2}

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", streaming=True)
    model = RetrievalQAWithSourcesChain.from_chain_type(
        llm=llm, chain_type="stuff", retriever=retriever
    )

    st.markdown("<h2>Pergunte aos dados carregados</h2>", unsafe_allow_html=True)
    user_q = st.text_area("Digite suas dúvidas aqui")

    if st.button("Obtenha sua resposta"):
        try:
            with st.spinner("O modelo está trabalhando nisso..."):
                result = model({"question": user_q}, return_only_outputs=True)
                st.markdown("<h3>Resposta do chatbot:</h3>", unsafe_allow_html=True)
                st.write(result["answer"])
        except Exception as e:
            st.error(f"Ocorreu um erro: {e}")
            st.error(
                "Opsss, a resposta do modelo resultou em um erro 😞, Tente novamente com uma pergunta diferente."
            )
