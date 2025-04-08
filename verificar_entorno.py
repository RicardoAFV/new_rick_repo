import sys
import pandas as pd
import plotly.express as px
import streamlit as st

print("✅ Entorno activo:", sys.executable)
print("✅ pandas version:", pd.__version__)
print("✅ plotly express disponible:", hasattr(px, "bar"))
print("✅ streamlit instalado:", hasattr(st, "title"))
