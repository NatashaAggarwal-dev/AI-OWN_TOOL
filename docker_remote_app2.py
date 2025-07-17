import streamlit as st
import paramiko
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType, tool
from langchain.tools import Tool
import os

# ✅ Set page config and title
st.set_page_config(page_title="Remote Linux + Docker AI Controller")
st.title("🤖 Remote Linux Assistant (via SSH + Gemini)")

# ✅ Form to get user inputs
with st.form("credentials_form"):
    remote_host = st.text_input("🔌 Remote IP Address (e.g., 192.168.10.100)")
    remote_port = st.number_input("📡 Port", value=22)
    username = st.text_input("👤 SSH Username")
    password = st.text_input("🔐 SSH Password", type="password")
    gemini_api_key = st.text_input("🧠 Gemini API Key", type="password")
    user_prompt = st.text_area("💬 Ask something (e.g., show running containers, check memory, etc.)")
    submitted = st.form_submit_button("🚀 Run")

# ✅ Set Gemini API Key
if gemini_api_key:
    os.environ["GOOGLE_API_KEY"] = "AIzaSyDHes_cKcPPrdNtEDuKyOHCEiCyCCL_ZLs"

# ✅ Function to run SSH command
def run_ssh_command(command: str) -> str:
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(remote_host, port=int(remote_port), username=username, password=password)
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode().strip()
        error = stderr.read().decode().strip()
        client.close()
        return output if output else error
    except Exception as e:
        return f"SSH Error: {e}"

# ✅ Tool for agent to use
@tool
def linux_command_executor(command: str) -> str:
    """Run any shell command on the remote server via SSH."""
    return run_ssh_command(command)

# ✅ Initialize Gemini LLM and agent
if gemini_api_key:
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    tools = [Tool(name="LinuxShell", func=linux_command_executor, description="Executes Linux shell commands on a remote server via SSH.")]
    agent = initialize_agent(tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=False)

# ✅ Run user prompt if submitted
if submitted:
    if not all([remote_host, username, password, gemini_api_key, user_prompt]):
        st.warning("Please fill in all fields.")
    else:
        with st.spinner("Thinking..."):
            try:
                result = agent.run(user_prompt)
                st.success("✅ Command output:")
                st.code(result)
            except Exception as e:
                if "429" in str(e):
                    st.error("❌ Gemini API quota exceeded. Please wait for reset or enable billing: https://ai.google.dev/gemini-api/docs/rate-limits")
                else:
                    st.error(f"❌ Error: {e}")
