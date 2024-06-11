import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from neo4j_driver import run_query
import math

from ui_utils import render_header_svg

st.set_page_config(
    page_title="PETRONAS Employee and Training Chatbot",
    page_icon="images/logo-mark-fullcolor-RGB-transBG.svg",
    layout="wide",
)


render_header_svg("images/main-top-header.svg", 350)

render_header_svg("images/bottom-header.svg", 200)

"Welcome to PETRONAS Employee and Training Chatbot"
        