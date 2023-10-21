import streamlit as st
import pickle
import numpy as np

# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Forecasting Harga Tanah")
# Desa
Desa = st.selectbox('DESA',df["Desa/Kelurahan"].unique())
Kecamatan = st.selectbox('KECAMATAN',df["Kecamatan"].unique())
Kabupaten = st.selectbox('KABUPATEN',df["Kabupaten/Kota"].unique())
Provinsi = st.selectbox('PROVINSI',df['Provinsi'].unique())

if st.button('Predict Price'):
    
    query = np.array([Desa,Kecamatan,Kabupaten,Provinsi])

    query = query.reshape(1,4)
    st.title("Harga(m²) :" + '{:,}'.format(int(pipe.predict(query)[0])).replace(",","."))