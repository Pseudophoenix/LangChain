# Recursive character text splitting
# Define some separators like for paragraphs-> \n\n, for lines-> \n, and for sentences->" "
from langchain.text_splitter import RecursiveCharacterTextSplitter
text="""
Introduction
In the realm of Large Language Models (LLMs), Ollama and LangChain emerge as powerful tools for developers and researchers. Ollama provides a seamless way to run open-source LLMs locally, while LangChain offers a flexible framework for integrating these models into applications. This article will guide you through the process of setting up and utilizing Ollama and LangChain, enabling you to harness the power of LLMs for your projects.

Zoom image will be displayed


Installation and Configuration
To start using Ollama, you first need to install it on your system. For macOS users, Homebrew simplifies this process:

brew install ollama
brew services start ollama
After installation, Ollama listens on port 11434 for incoming requests. You can verify its operation by navigating to `http://localhost:11434/` in your browser. The next step involves selecting the LLM you wish to run locally. For instance, to run the `llama2`, `mistral` etc model, execute:

ollama pull mistral
This command downloads the model, optimizing setup and configuration details, including GPU usage.
"""
splitter=RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=0
)
chunks=splitter.split_text(text)
print(len(chunks))
print(chunks)