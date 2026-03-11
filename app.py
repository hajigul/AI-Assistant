import streamlit as st
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

# ====================== AI SETUP (same as your original code) ======================
model = OllamaLLM(model="llama3.2")

template = """
You are an expert in answering questions about a pizza restaurant.

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# ====================== STREAMLIT FRONT END ======================
st.set_page_config(page_title="Pizza AI", page_icon="🍕", layout="centered")

st.title("🍕 Pizza Restaurant AI Assistant")
st.markdown("**Ask anything** about our pizzas, service, crust, vegan options, prices — powered by real customer reviews!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if user_input := st.chat_input("Type your question here... (e.g. What do people say about the crust?)"):
    
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🍕"):
            # Get relevant reviews
            reviews_docs = retriever.invoke(user_input)
            # Make reviews nice and readable
            reviews_text = "\n\n".join([doc.page_content for doc in reviews_docs])
            
            # Run the chain
            response = chain.invoke({"reviews": reviews_text, "question": user_input})
            
            st.markdown(response)
    
    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar
with st.sidebar:
    st.header("🍕 About this AI")
    st.write("This assistant answers using **100+ real customer reviews** from our restaurant.")
    st.write("Built with LangChain + Ollama + Streamlit")
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    st.caption("Made with ❤️ for Haji's Pizza Project")