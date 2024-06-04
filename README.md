# AI-SSTANT
## Overview

Local Multimodal AI Chat is a hands-on project aimed at learning how to build a multimodal chat application. This project is all about integrating different AI models to handle PDFs in a single chat interface. It's a great way for anyone interested in AI and software development to get practical experience with these technologies.


I'm really open to pull requests. Whether you have ideas for new features, ways to make the code better, or just want to fix a bug, your contributions are welcome. This project is as much about learning from each other as it is about building something cool.

So, if you're interested in AI chat applications and want to dive into how they're built, join in. Your code and ideas can help make this project better for everyone who wants to learn more about building with AI.

## Features

- **Quantized Model Integration**: This app uses what are called "quantized models." These are special because they are designed to work well on regular consumer hardware, like the kind most of us have at home or in our offices. Normally, the original versions of these models are really big and need more powerful computers to run them. But quantized models are optimized to be smaller and more efficient, without losing much performance. This means you can use this app and its features without needing a super powerful computer. [Quantized Models from TheBloke](https://huggingface.co/TheBloke)



- **PDF Chatting with Chroma DB**: The app is tailored for both professional and academic uses, integrating Chroma DB as a vector database for efficient PDF interactions. This feature allows users to engage with their own PDF files locally on their device. Whether it's for reviewing business reports, academic papers, or any other PDF document, the app offers a seamless experience. It provides an effective way for users to interact with their PDFs, leveraging the power of AI to understand and respond to content within these documents. This makes it a valuable tool for personal use, where one can extract insights, summaries, and engage in a unique form of dialogue with the text in their PDF files. [Chroma website](https://docs.trychroma.com/)


## Getting Started

To get started with Local Multimodal AI Chat, clone the repository and follow these simple steps:

1. **Upgrade pip**: pip install --upgrade pip

2. **Install Requirements**: pip install -r requirements.txt
   
   **Note:** in requirements_with_versions.txt I saved the versions of the requirements while creating this project, and in pip_freeze.txt is a complete freeze of the packages in the environment I used. So if you encounter errors due to newer versions, you might want to consider using one of those requirements files, or at least the versions for the packages which make problems.
   
   **Windows Users:** The installation might differ a bit for you, if you encounter errors you can't solve, please open an Issue here on github.

3. **Setting Up Local Models**: Download the models you want to implement. [Here](https://huggingface.co/mys/ggml_llava-v1.5-7b/tree/main) is the llava model I used for image chat (ggml-model-q5_k.gguf and mmproj-model-f16.gguf). 
And the [quantized mistral model](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF) form TheBloke.

4. **Customize config file**: Check the config file and change accordingly to the models you downloaded.

5. **Enter command in terminal**: streamlit run app.py


## Possible Improvements
- Add Model Caching.
- Add Images and Audio to Chat History Saving and Loading.
- Use a Database to Save the Chat History.
- Integrate Ollama, OpenAI, Gemini, or Other Model Providers.
- Add Image Generator Model.
- Authentication Mechanism.
- Change Theme.
- Separate Frontend and Backend Code for Better Deployment.

