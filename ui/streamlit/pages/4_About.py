import streamlit as st
from PIL import Image

st.set_page_config(page_icon="🧠", layout="wide")
st.markdown("""
This is a Proof of Concept application which shows how Google Vertex AI can be used with Neo4j to build and consume Knowledge Graphs using Structured Data.
The Structured Data used are Employee's information and list of all the details of the training programs that the employees have taken.

### Why using Vertex AI and LangChain with Codey Bison for querying AuraDB is beneficial:
By integrating Vertex AI and LangChain with Codey Bison, you can enhance your chatbot to effectively query the AuraDB graph database. This system, which uses structured data from CSV files, leverages sophisticated language models and Neo4j's graph database capabilities to deliver insightful interactions. Here’s how this setup benefits your application:

Fine-grained Access Control: With Vertex AI, you can precisely manage who has access to specific data, ensuring robust security and compliance.
Enhanced Reliability: The factual data stored in Neo4j ensures that your chatbot provides accurate and trustworthy responses.
Improved Explainability: The structured format of Neo4j, combined with the natural language understanding of Vertex AI, allows for clear and understandable chatbot responses.
Domain Specificity: The chatbot can be customized to understand and utilize domain-specific terminology, providing more relevant and contextual answers.
Insightful Graph Algorithms: Neo4j's graph algorithms can be leveraged to uncover patterns and insights within your data, enhancing the depth of chatbot interactions.
Optimized Query Generation: Using LangChain’s GraphCypherQAChain, the system translates natural language queries into efficient Cypher queries, tailored for Neo4j, ensuring precise and relevant data retrieval.
This integration empowers your chatbot to handle complex queries efficiently, providing meaningful and actionable insights derived from structured data in AuraDB.

""", unsafe_allow_html=True)

langchain = Image.open('./images/langchain-neo4j.png')
schema = Image.open('./images/bloom-visualisation.png')

st.markdown("""
---

This the schema in which the Employees and Training Programs data are stored in Neo4j
""")
st.image(schema)
st.markdown("""
---

This is how the Chatbot flow goes:
""")
st.image(langchain)
