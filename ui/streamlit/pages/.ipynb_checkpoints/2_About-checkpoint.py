import streamlit as st
from PIL import Image

# Load the images
langchain = Image.open('./images/langchain-neo4j.png')
schema = Image.open('./images/bloom-visualisation_1.png')
petronas = Image.open('./images/Petronas_Logo.png')

# Streamlit page configuration
st.set_page_config(page_icon="🧠", layout="wide")

# Display the uploaded image at the top and center
st.markdown("""
    <div style='text-align: center;'>
        <img src='data:image/png;base64,{}' width="100">
    </div>
""".format(st.image(petronas, use_column_width=True)), unsafe_allow_html=True)


# Main content
st.markdown("""
This is a Proof of Concept application which shows how Google Vertex AI can be used with Neo4j to build and consume Knowledge Graphs using Structured Data.
The Structured Data used are Employee's information and list of all the details of the training programs that the employees have taken.

### Why using Vertex AI and LangChain with Codey Bison for querying AuraDB is beneficial:
By integrating Vertex AI and LangChain with Codey Bison, you can enhance your chatbot to effectively query the AuraDB graph database. This system, which uses structured data from CSV files, leverages sophisticated language models and Neo4j's graph database capabilities to deliver insightful interactions. Here’s how this setup benefits your application:

<b>Fine-grained Access Control:</b> With Vertex AI, you can precisely manage who has access to specific data, ensuring robust security and compliance.<br><br>
<b>Enhanced Reliability:</b> The factual data stored in Neo4j ensures that your chatbot provides accurate and trustworthy responses.<br><br>
<b>Improved Explainability:</b> The structured format of Neo4j, combined with the natural language understanding of Vertex AI, allows for clear and understandable chatbot responses.<br><br>
<b>Domain Specificity:</b> The chatbot can be customized to understand and utilize domain-specific terminology, providing more relevant and contextual answers.<br><br>
<b>Insightful Graph Algorithms:</b> Neo4j's graph algorithms can be leveraged to uncover patterns and insights within your data, enhancing the depth of chatbot interactions.<br><br>
<b>Optimized Query Generation:</b> Using LangChain’s GraphCypherQAChain, the system translates natural language queries into efficient Cypher queries, tailored for Neo4j, ensuring precise and relevant data retrieval.<br><br>
This integration empowers your chatbot to handle complex queries efficiently, providing meaningful and actionable insights derived from structured data in AuraDB.

""", unsafe_allow_html=True)

# Additional content with images
st.markdown("""
---

This is the data model in which the Employees and Training Programs data are stored in Neo4j
""")
st.image(schema)
st.markdown("""
---

This is how the Chatbot flow goes:
""")
st.image(langchain)


