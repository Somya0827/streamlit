import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo

# Page title
st.title("AI Search Assistant")

# Initialize the agent
agent = Agent(
    model=Groq(
        id="llama-3.3-70b-versatile", 
        api_key="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"
    ),
    tools=[DuckDuckGo()],
    markdown=True
)

# Create text input
user_query = st.text_input("Enter your question:")

# Create search button
if st.button("Search"):
    if user_query:
        with st.spinner("Searching..."):
            try:
                response = agent.run(user_query)
                st.write(response.content)
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a question!")