# Multi AI Context Switcher

## 📌 Overview

Multi AI Context Switcher is a web-based application that allows users to interact with multiple AI models through a single interface.

The application provides a unified chat interface where users can select an AI model, send prompts, maintain conversation history, and switch between different AI models without changing the application.

## ✨ Features

* 🤖 Multiple AI model selection
* 💬 Interactive chat interface
* 🔄 Switch between different AI models
* 🧠 Conversation history
* 🗑️ Clear chat functionality
* 🌙 Dark mode
* 🔐 API keys managed using environment variables
* ⚡ FastAPI backend
* 🌐 HTML, CSS and JavaScript frontend
* ☁️ Deployment-ready architecture

## 🛠️ Technologies Used

### Backend

* Python
* FastAPI
* Uvicorn

### Frontend

* HTML
* CSS
* JavaScript

### AI Integration

* OpenRouter API
* Multiple AI models

### Other

* REST API
* Environment Variables
* Git & GitHub

## 🏗️ Project Architecture

```text
User
  ↓
Frontend
(HTML / CSS / JavaScript)
  ↓
FastAPI Backend
  ↓
AskAI Function
  ↓
OpenRouter API
  ↓
Selected AI Model
  ↓
AI Response
  ↓
Frontend
```

## ⚙️ How It Works

1. The user opens the web application.
2. The user selects an AI model.
3. The user enters a prompt.
4. The frontend sends the request to the FastAPI backend.
5. FastAPI processes the request and sends it to the `AskAI` function.
6. The `AskAI` function communicates with the selected model through OpenRouter.
7. The AI response is returned to the backend.
8. The response is displayed in the frontend.
9. Conversation history can be maintained for continued interaction.

## 📁 Project Structure

```text
Multi-AI-Context-Switcher/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/rahulsingh45500-ux/multi_ai_chat_system.git
```

### 2. Navigate to the project

```bash
cd multi_ai_chat_system
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project root:

```text
OPENROUTER_API_KEY=your_api_key_here
```

If your application uses additional API keys, add them to the `.env` file as required.

**Never upload your `.env` file or expose API keys publicly.**

## ▶️ Run the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Then open the application in your browser:

```text
http://127.0.0.1:8000
```

## 🔄 Model Switching

The application allows the user to select different AI models from the interface.

The selected model and user prompt are sent to the backend, where the request is processed and forwarded to the appropriate AI model through OpenRouter.

This allows multiple models to be accessed through a single application instead of building separate applications for each model.

## 💡 Key Learning Outcomes

Through this project, I gained practical experience with:

* Building REST APIs using FastAPI
* Connecting a frontend with a Python backend
* Working with external AI APIs
* Managing API credentials using environment variables
* Handling user requests and responses
* Maintaining conversation history
* Structuring a full-stack application
* Using Git and GitHub for version control
* Deploying a web application

## 🔮 Future Improvements

* User authentication
* Persistent database-based chat history
* More AI model providers
* Streaming AI responses
* Voice input and output
* File upload and document-based conversations
* Model performance comparison
* Docker-based deployment

## 👨‍💻 Author

**Rahul Kumar Singh**

GitHub:
https://github.com/rahulsingh45500-ux
