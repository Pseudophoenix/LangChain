import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage

# config for the InMemory Configuration of Workflow
CONFIG={"configurable":{"thread_id":"thread-1"}}
# message history that will persist till we refresh the page and won't refresh on press of ENTER key
if 'message_history' not in st.session_state:
    st.session_state['message_history']=[]

# PRINT all the past conversation form session_state['message_history']
# # loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])
# Take the input fromt the user
user_input=st.chat_input('Type here')
# if the user input exists
if user_input:
    # append the user input to the session_state
    st.session_state['message_history'].append({'role':'user','content':user_input})
    with st.chat_message('user'):
        st.text(user_input)
    # pass the user message to the chatbot
    response=chatbot.invoke({'messages':[HumanMessage(content=user_input)]},config=CONFIG)
    # store the last message as response from the AI into the session_state
    ai_message=response['messages'][-1].content
    st.session_state['message_history'].append({'role':'assistant',"content":ai_message})
    with st.chat_message('assistant'):
        st.text(ai_message)



# import streamlit as st

# if 'message_history' not in st.session_state:
#     # message_history=[]
#     st.session_state['message_history']=[]

# for message in st.session_state['message_history']:
#     with st.chat_message(message['role']):
#         st.text(message['message'])
    

# user_input=st.chat_input("Type here")
# if user_input:
#     st.session_state['message_history'].append({'role':'user','message':user_input})
#     with st.chat_message('user'):
#         st.text(user_input)
#     st.session_state['message_history'].append({'role':'assistant','message':user_input})
#     with st.chat_message('assistant'):
#         st.text("Hey")