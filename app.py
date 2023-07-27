# app.py

import streamlit as st
import snowflake.connector
import pandas as pd

st.title("Zena's Amazing Athleisure Catalog")

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()

my_cur.execute("select color_or_style from zenas_athleisure_db.products.catalog_for_website")
catalog = my_cur.fetchall()

df = pd.DataFrame(catalog)
colors = df[0].values.tolist()

dropbox = st.selectbox('Pick a sweatsuit color or style:', list(colors))


