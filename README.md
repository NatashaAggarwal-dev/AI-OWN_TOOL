Remote Linux Assistant (via SSH + Gemini)
A Streamlit-based AI assistant that allows you to execute natural language commands on a remote Linux server over SSH using Google Gemini as the LLM backend.
This application bridges human-like instructions with automated shell execution, simplifying cloud and server management tasks.

➤ Features
Secure SSH connection to remote Linux machines

AI-powered natural language command interpretation using Gemini

Execution of remote shell commands via Paramiko

Streamlit UI for clean interaction

Supports Docker, system commands, and more


➤ Prerequisites
Before using the application, ensure the following:

Python 3.8 or higher

Remote Linux server with SSH access

Gemini API key from Google AI Studio

Required Python packages installed


➤ Installation
1. Clone the Repository
git clone https://github.com/yourusername/remote-linux-assistant.git
cd remote-linux-assistant

2. Install Dependencies
pip install -r requirements.txt

➤ Running the Application
Start the Streamlit application using the following command:
streamlit run app.py
→ The app will open in your default web browser at http://localhost:8501


➤ Application Workflow
→ Enter the remote server’s IP address, SSH port, username, and password
→ Enter your Gemini API key
→ Type a natural language instruction such as:

List all running Docker containers

Check available disk space

Restart Apache service

→ The Gemini model interprets the instruction
→ The command is executed remotely via SSH
→ The result is displayed in the UI

➤ Technologies Used
Streamlit – UI framework

LangChain – Agent orchestration

Google Generative AI (Gemini) – LLM backend

Paramiko – SSH client for Python

➤ Security Notes
Your credentials are used only during the session and are not stored

SSH connections are made directly from your local machine to the remote server

➤ Disclaimer
This project is intended for educational and internal DevOps use.
Please ensure appropriate access controls and security best practices are followed when using in production environments.

➤ License
This project is licensed under the MIT License. See the LICENSE file for details.

➤ Connect with Me
If you found this project helpful or want to collaborate, feel free to connect:

LinkedIn → https://www.linkedin.com/in/natasha-aggarwal
