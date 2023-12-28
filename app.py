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

st.set_page_config(layout="centered", page_title="Forecast Chatbot")
st.header("Forecast documentation Chatbot")
st.write("---")

uploaded_files = st.file_uploader(
    "Faça o upload do documento", accept_multiple_files=True, type=["txt", "pdf"]
)
st.write("---")

if uploaded_files is None:
    st.info(f"Por favor faça o upload de um documento para analise")
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
        llm=llm, chain_type="stuff", retriever=retriever)

    st.header("Pergunte aos dados carregados")
    user_q = st.text_area("Digite suas dúvidas aqui")

    if st.button("Obtenha sua resposta"):
        try:
            with st.spinner("O modelo está trabalhando nisso..."):
                result = model({"question": user_q}, return_only_outputs=True)
                st.subheader("Resposta do chatbot:")
                st.write(result["answer"])
        except Exception as e:
            st.error(f"Ocorreu um erro: {e}")
            st.error(
                "Opsss, a resposta do modelo resultou em um erro 😞, Tente novamente com uma pergunta diferente."
            )
