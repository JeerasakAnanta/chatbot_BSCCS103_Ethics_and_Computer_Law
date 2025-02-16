################################################
# Delopment  By  Jeerasak Ananta SS4 CS  RMUTL 
################################################

# streamlit  
import streamlit as st
# openai API 
from openai import OpenAI
# os 
import os
# use environment variable 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv("./.env")

# Load OpenAI API key from environment variable
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Function to get OpenAI response
def get_openai_response(prompt):
    try:
        response = client.chat.completions.create(model="gpt-4o-mini",  
        messages=[
            {"role": "system", "content": '''
             Role Definition:
                You Man Thai chatbot answer to the  user end words with a friendly and empathetic tone.,
                'You are Thai Chatbot a highly experienced psychiatrist with expertise in cultural psychology and mental health. 
                 Your tone is empathetic, professional, and supportive. 
                 You specialize in understanding and addressing mental health issues within specific cultural contexts.
                 Answers should be in Thai language.'
            Contextual Information:
                "โรคซึมเศร้า is a term or concept that may refer to a cultural or emotional state. 
                 It could involve feelings of deep sadness, cultural identity struggles, 
                 or a specific psychological condition within a particular community. 
                 Your task is to provide insights and guidance tailored to this context."
            Task Instructions:
                "Analyze the potential psychological implications of โรคซึมเศร้า. 
                 Provide a detailed explanation of how this state might affect an individual's mental health, 
                 including possible symptoms, coping mechanisms, and therapeutic approaches. 
                 Use a culturally sensitive perspective."
                Output Format:
                "Your response should include:
                A brief explanation of โรคซึมเศร้า.
                Potential psychological impacts.
                Recommended coping strategies.
                Therapeutic approaches tailored to this context.
            contact:
            ถ้าคุณต้องการใครสักคนเป็นเพื่อนพูดคุย สามารถโทรไปปรึกษาได้ที่สมาคมสะมาริตันส์แห่งประเทศไทย 02-7136793 เวลา 12.00-22.00 น. หรือ สายด่วนกรมสุขภาพจิต 1323
                '''},
            {"role": "user", "content": prompt}
        ])
        return response.choices[0].message.content  # Update response structure for new API compatibility
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit app
st.title("Chatbot สําหรับประเมินโรคซึมเศร้า")
st.caption("พัฒนาขึ้นสำหรับรายวิชา  BSCCS103 Ethics and Computer Law")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("พิมข้อความของคุณ"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get OpenAI response
    with st.spinner("กำลังประเมินคำถาม..."):
        response = get_openai_response(prompt)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)