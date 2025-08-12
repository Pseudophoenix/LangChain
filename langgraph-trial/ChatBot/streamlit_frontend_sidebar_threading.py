import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage
import uuid

# **************************************** utility functions *************************

# generate the thread_id
def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id
# reset means generate a new thread_id and make it as the current thread_id also add it to chat_threads sesion_state, make its message history as blank
def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history'] = []
# add the given thread_id to chat_threads session_state
def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

# from the states of chat bot fetch the messages of that particular thread id and return those
def load_conversation(thread_id):
    if "messages" in chatbot.get_state(config={"configurable":{'thread_id':thread_id}}).values:
        return chatbot.get_state(config={'configurable': {'thread_id': thread_id}}).values['messages']
    return []

# *********** Session Setup ***************
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = []
# add the current thread_id to the chat_threads session_state
add_thread(st.session_state['thread_id'])


# ********************* Sidebar UI *******************

st.sidebar.title('LangGraph Chatbot')
# on button click reset the chat that is create a fresh thread_id and make its initial configuration
if st.sidebar.button('New Chat'):
    reset_chat()

st.sidebar.header('My Conversations')
# displau all the chats in the sidebar use the chat_threads and fetch all of the thread_ids in reverse order[::-1]
for thread_id in st.session_state['chat_threads'][::-1]:
    # create a separate clickable button for each thread_id
    if st.sidebar.button(str(thread_id)):
        # make that particular thread_id as the current thread_id and load on screen
        st.session_state['thread_id'] = thread_id
        messages = load_conversation(thread_id)
        # messaages now has those messages
        temp_messages = []
        # from the messages assign role to the chat message depending on whether it is an instanceof HumanMessage or Not
        for msg in messages:
            if isinstance(msg, HumanMessage):
                role='user'
            else:
                role='assistant'
            # temp messages will store the role and content 
            temp_messages.append({'role': role, 'content': msg.content})
        # change the entire message history session_state replacing it with temp_messages
        st.session_state['message_history'] = temp_messages


# ********************** Main UI ****************

# loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input = st.chat_input('Type here')

if user_input:

    # first add the message to message_history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}}

    # first add the message to message_history
    with st.chat_message('assistant'):

        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config= CONFIG,
                stream_mode= 'messages'
            )
        )

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})