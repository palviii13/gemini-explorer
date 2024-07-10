import os
from google.oauth2 import service_account
import vertexai
import uuid
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession

# Path to the downloaded JSON key file
key_path = '/Users/palvishroff/Downloads/gemini-explorer-428820-32d250deb8cf.json'

# Set the environment variable for authentication
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path

# Initialize Vertex AI with the project name
project = "gemini-explorer-428820"
vertexai.init(project=project)

# Configure the generation settings for the model
config = generative_models.GenerationConfig(
    temperature=0.4
)

# Create a GenerativeModel instance with the specified configuration
model = GenerativeModel(
    "gemini-pro",
    generation_config=config
)

# Start a chat session with the model
chat = model.start_chat()

def llm_function(chat: ChatSession, query):
    # Send the user's query to the chat session
    response = chat.send_message(query)
    output = response.candidates[0].content.parts[0].text
    with st.chat_message("model"):
        st.markdown(output)
    
    # Update the session state with the user's query and the model's response
    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )
    st.session_state.messages.append(
        {
            "role": "model",
            "content": output
        }
    )

st.title("Gemini Explorer")

# Check if the 'messages' key is in the session state and initialize it if not present
if "messages" not in st.session_state:
    st.session_state.messages = []

# Add the logic for the initial message
if len(st.session_state.messages) == 0:
    initial_prompt = "Introduce yourself as ReX, an assistant powered by Google Gemini. You use emojis to be interactive make it as per genz"
    llm_function(chat, initial_prompt)

# Display chat history
for index, message in enumerate(st.session_state.messages):
    if index % 2 == 0:  # Skip every other message to prevent duplicates
        content = Content(
            role=message["role"],
            parts=[Part.from_text(message["content"])]
        )
        if index != 0:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        chat.history.append(content)

# Streamlit interface for interacting with the Gemini chat
user_input = st.text_input("You:", value="Type your query...")

# Text input for user query
query_input_key = str(uuid.uuid4())
query = st.text_input("Enter your query here", value="", key=query_input_key)

if st.button("Send"):
    llm_function(chat, query)  # Use the llm_function to process the user's input

# Display the response
if st.session_state.messages:
    st.text_area("Gemini:", value=st.session_state.messages[-1]["content"], height=200)
