import streamlit as st
import subprocess

def get_installed_models():
    """Fetch installed ollama models"""
    result = subprocess.run(
        ["ollama", "list"],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        st.error("Error fetching models from Ollama")
        return []

    lines = result.stdout.strip().split("\n")
    models = []
    for line in lines[1:]:  # Skip header
        parts = line.split()
        if parts:
            models.append(parts[0])
    return models

def query_model(model, prompt):
    """Run query on the selected ollama model"""
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt,
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        return f"Error: {result.stderr}"
    return result.stdout.strip()

# Streamlit UI
st.title("🦙 Ollama Model Playground")
st.write("Run queries on your locally installed Ollama models.")

# Get available models
models = get_installed_models()

if models:
    selected_model = st.selectbox("Select a model", models)
    user_query = st.text_area("Enter your query")

    if st.button("Run Query"):
        with st.spinner("Running model..."):
            response = query_model(selected_model, user_query)
        st.subheader("Response")
        st.write(response)
else:
    st.warning("No models found. Please install Ollama models first.")
