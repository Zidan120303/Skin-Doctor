import streamlit as st
import pandas as pd
from data import data_penyakit_kulit, data_gejala, data_aturan



def show_gejala_klasifikasi():
    st.title("Tabel Gejala dan Klasifikasi Penyakit")
    
    df_penyakit = pd.DataFrame(data_penyakit_kulit)
    df_penyakit.columns = ['ID', 'Kode Penyakit']
    st.subheader("Tabel Penyakit")
    st.dataframe(df_penyakit, hide_index= True, use_container_width= True)

    df_gejala = pd.DataFrame(data_gejala)
    df_gejala.columns = ['ID', 'Kode Gejala']
    st.subheader("Tabel Gejala")
    st.dataframe(df_gejala, hide_index= True, use_container_width= True)

    df_aturan = pd.DataFrame(data_aturan)
    df_aturan.columns = ['ID', 'Kode Gejala', 'Kode Penyakit', 'Nama Penyakit']
    st.subheader("Tabel Aturan")
    st.dataframe(df_aturan, hide_index= True, use_container_width= True)
