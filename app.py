"""Streamlit frontend for the query router."""

import streamlit as st
from router import QueryRouter

# Page config
st.set_page_config(page_title="Query Router", page_icon="🔀")

# Initialize router (cached to avoid reloading)
@st.cache_resource
def get_router():
    return QueryRouter()

# Header
st.title("Query Router")
st.caption("Routes your questions to the right agent using LLM")

# Initialize router
try:
    router = get_router()
except Exception as e:
    st.error(f"Failed to connect to Ollama. Make sure it's running: `ollama serve`")
    st.stop()

# Input
query = st.text_input("Enter your query:", placeholder="e.g., Show my open pull requests")

# Process query
if st.button("Route Query", type="primary") or query:
    if query.strip():
        with st.spinner("Routing..."):
            response = router.route(query)
        
        # Show result
        st.divider()
        st.subheader("Response")
        st.write(response)
    else:
        st.warning("Please enter a query")

# Sidebar info
with st.sidebar:
    st.header("Available Agents")
    st.markdown("** GitHubAgent**")
    st.caption("Pull requests, commits, repos, branches")
    
    st.markdown("** LinearAgent**")
    st.caption("Issues, tasks, sprints, assignments")
    
    st.divider()
    st.header("Example Queries")
    st.code("Show my open pull requests")
    st.code("What issues are assigned to me?")
    st.code("What's the weather today?")