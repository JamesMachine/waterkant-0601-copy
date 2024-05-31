import streamlit as st
from st_audiorec import st_audiorec
from openai import OpenAI
import prompt_db
import time


api_key=st.secrets.api_key
client = OpenAI(api_key=api_key)

def stream_data(msg):
    for word in msg.split(" "):
        yield word + " "
        time.sleep(0.02)

page_background = """
    <style>
        [data-testid="stAppViewContainer"] {
            background: #ececec
            }
    </style>
"""
st.markdown(page_background, unsafe_allow_html=True)

title = """
    <h1 style='text-align: center; color: grey;'>
    Chat it Out!
    </h1>
"""
st.markdown(title, unsafe_allow_html=True)

if "conversation_history" not in st.session_state:
    st.session_state["conversation_history"] = [
        {"role": "system", "content": prompt_db.system_content}
    ]

# Initialize session state if it doesn't exist
if 'button_clicked' not in st.session_state:
    st.session_state['button_clicked'] = None

################ Side Button ################

# Create buttons in the sidebar
if st.sidebar.button(r"$\textsf{\normalsize 👧 Anna Müller}$"):
    st.session_state['button_clicked'] = 'Anna'
    st.experimental_rerun()

if st.sidebar.button(r"$\textsf{\normalsize 👸 Sara Ott}$"):
    st.session_state['button_clicked'] = 'Sara'
    st.experimental_rerun()
	
if st.sidebar.button(r"$\textsf{\normalsize 🧚‍♀️ Try Me!}$"):
    st.session_state['button_clicked'] = 'User'
    st.experimental_rerun()

# Use the button click value in the rest of the code
if st.session_state['button_clicked'] == 'Anna':
    st.session_state.conversation_history.append({"role": "user", "content": prompt_db.user_background("anna")})
    st.session_state.conversation_history, assistant_message = prompt_db.chat_response(st.session_state.conversation_history)
    
elif st.session_state['button_clicked'] == 'Sara':
    st.session_state.conversation_history.append({"role": "user", "content": prompt_db.user_background("sara")})
    st.session_state.conversation_history, assistant_message = prompt_db.chat_response(st.session_state.conversation_history)
    
elif st.session_state['button_clicked'] == 'User':
    st.session_state.conversation_history.append({"role": "user", "content": prompt_db.user_background("user")})
    st.session_state.conversation_history, assistant_message = prompt_db.chat_response(st.session_state.conversation_history)


################ Type Input ################

if type_input := st.chat_input("What is up?"):
    st.session_state.conversation_history.append({"role": "user", "content": type_input})
    st.session_state.conversation_history, assistant_message = prompt_db.chat_response(st.session_state.conversation_history)

for i, message in enumerate(st.session_state.conversation_history):

    if message["role"] != "system":

        if (len(st.session_state.conversation_history) <=3):
            with st.chat_message(message["role"]):
                st.write_stream(stream_data(message["content"]))

        elif i >= len(st.session_state.conversation_history)-2:
            with st.chat_message(message["role"]):
                st.write_stream(stream_data(message["content"]))
                
        else:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

















# col1, col2, col3 = st.columns([1, 3, 1])
# with col2:
#     wav_audio_data = st_audiorec()

# if wav_audio_data is not None:
#     
#     with open("recorded_audio.wav", "wb") as f:
#             f.write(wav_audio_data)
# 
#     audio_file = open("recorded_audio.wav", "rb")
#     
#     transcription = client.audio.transcriptions.create(
#         model="whisper-1", 
#         file=audio_file
#     )
#     
#     voice_input = transcription.text
#     st.session_state.conversation_history.append({"role": "user", "content": voice_input})
#     st.session_state.conversation_history, assistant_message = prompt_db.chat_response(st.session_state.conversation_history)

































