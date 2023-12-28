# Chat bot documents with LangChain and OpenAI

Link do aplicativo :

## Descrição

Este projeto consiste em um ChatBot que oferece respostas a perguntas extraídas de documentos PDF ou TXT enviados pelo usuário ao servidor. A aplicação utiliza tecnologias de um modelo de linguagem da OpenAI para processar e compreender o conteúdo do documento. O usuário recebe respostas precisas e relevantes às suas perguntas, agilizando a busca por informações específicas nos documentos.

## Funcionalidades

1. **Processamento de Documentos:** O ChatBot é capaz de processar vários documentos nos formatos PDF ou TXT, permitindo que o usuário envie textos para análise.

2. **Extração de Informações:** Utilizando um modelo de linguagem da OpenAI, o sistema extrai informações relevantes e responde a perguntas específicas feitas pelo usuário.

3. **Busca Eficiente de Conteúdo:** A aplicação realiza uma busca inteligente no documento, localizando e compreendendo o contexto para fornecer respostas precisas.

4. **Interação Amigável:** O ChatBot oferece uma experiência de usuário amigável, proporcionando respostas claras e concisas, tornando a busca por informações mais eficiente.

Este aplicativo é uma ferramenta valiosa para quem precisa extrair informações específicas de documentos extensos, proporcionando uma solução eficaz e tecnologicamente avançada para a análise de conteúdo textual.

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/RenatoDev4/chatbot_documents.git

2. **Instale as dependências:**

   ```bash
   pipenv install

3. **Configuração do Modelo de Linguagem da OpenAI:** Obtenha as credenciais ou chave de API da OpenAI e configure-as e configure-as como uma váriavel de ambiente.

4. **Execute o projeto:**

   ```bash
   streamlit run app.py

## Configuração

1. **Váriaveis de ambiente:**

   ```bash
   OPENAI_API_KEY="SuaChaveAqui"

Configure as credenciais da OpenAI como uma váriavel de ambiente, como por exemplo em um arquivo .env


## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue para discutir novas funcionalidades, relatar bugs ou enviar um pull request.

## Licença

Este projeto está licenciado sob a **Licença MIT.**
