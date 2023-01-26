#import libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import json
import matplotlib.patches as mpatches
from matplotlib import cm
from matplotlib.font_manager import FontProperties
import seaborn as sns

# adding title in streamlit
st.sidebar.markdown(f"<span style='color: black;font-size: 36px;font-weight: bold;'>Food Aayush</span>", unsafe_allow_html=True)

st.sidebar.info("Welcome to Food Aayush Data Analytics. Here you can analyse the nutritional value of food and draw some schematics")
