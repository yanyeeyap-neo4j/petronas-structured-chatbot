from langchain.chains import GraphCypherQAChain
from langchain.graphs import Neo4jGraph
from langchain.prompts.prompt import PromptTemplate
from langchain.llms import VertexAI
from retry import retry
from timeit import default_timer as timer
import streamlit as st

host = st.secrets["NEO4J_HOST"]+":"+st.secrets["NEO4J_PORT"]
user = st.secrets["NEO4J_USER"]
password = st.secrets["NEO4J_PASSWORD"]
db = st.secrets["NEO4J_DB"]

codey_model_name = st.secrets["TUNED_CYPHER_MODEL"]
if codey_model_name == '':
    codey_model_name = 'code-bison'
    

CYPHER_GENERATION_TEMPLATE = """You are an expert Neo4j Cypher translator who understands the question in english and convert to Cypher strictly based on the Neo4j Schema provided and following the instructions below:
1. Generate Cypher query compatible ONLY for Neo4j Version 5
2. Do not use EXISTS, SIZE keywords in the cypher. Use alias when using the WITH keyword
3. Use only Nodes and relationships mentioned in the schema
4. Always enclose the Cypher output inside 3 backticks
5. Always do a case-insensitive and fuzzy search for any properties related search. Eg: to search for a Company name use `toLower(c.name) contains 'neo4j'`
6. Candidate node is synonymous to Person
7. Always use aliases to refer the node in the query
8. Cypher is NOT SQL. So, do not mix and match the syntaxes
Schema:
{schema}
Samples:
Question: Who are the employees who have taken Customer Service program but has not completed?
Answer: MATCH (e:Employee)-[t:TAKEN_TRAINING]->(p:Program) WHERE toLower(p.ProgramName) CONTAINS 'customer service' AND t.TrainingOutcome <> 'Completed' RETURN e.FirstName, e.LastName
Question: What are the programs available?
Answer: MATCH (p:Program) RETURN p.ProgramName
Question: How many people failed the Technical Skills program?
Answer: MATCH (e:Employee)-[t:TAKEN_TRAINING]->(p:Program) WHERE toLower(p.ProgramName) CONTAINS 'technical skills' AND toLower(t.TrainingOutcome) CONTAINS 'fail' RETURN count(e)
Question: How many employees are there?
Answer: MATCH (e:Employee) RETURN count(e)
Question: {question}
Answer:
"""
CYPHER_GENERATION_PROMPT = PromptTemplate(
    input_variables=["schema", "question"], template=CYPHER_GENERATION_TEMPLATE
)

@retry(tries=5, delay=5)
def get_results(messages):
    start = timer()
    try:
        graph = Neo4jGraph(
            url=host, 
            username=user, 
            password=password
        )
        chain = GraphCypherQAChain.from_llm(
            VertexAI(
                    model_name=codey_model_name,
                    max_output_tokens=2048,
                    temperature=0,
                    top_p=0.95,
                    top_k=0.40), 
                    graph=graph, verbose=True,
                    return_intermediate_steps=True,
                    cypher_prompt=CYPHER_GENERATION_PROMPT
        )
        if messages:
            question = messages.pop()
        else: 
            question = 'How many cases are there?'
        return chain(question)
    finally:
        print('Cypher Generation Time : {}'.format(timer() - start))
        