import streamlit as st
from data import data_gejala
from hasil_diagnosa import show_hasil_diagnosa
import time

def show_form_diagnosa():
    with st.form("diagnosa_form"):
        
        st.subheader("Data Diri")
        st.info('Isi data diri anda dengan lengkap!')
        nama = st.text_input("Nama Pasien")
        tgl_lahir = st.date_input("Tanggal Lahir")
        alamat = st.text_input("Alamat Rumah")
        nomor_telepon = st.text_input("Nomor Telepon")
        
        st.subheader("Pilih Gejala")

        gejala_responses = {}
        for gejala in data_gejala:
            response = st.radio(f"Apakah Anda mengalami gejala: {gejala[1]}?", ["Ya", "Tidak"], key=gejala[0], horizontal=True, index=1)
            gejala_responses[gejala[0]] = response
        
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            st.session_state['nama'] = nama
            st.session_state['tgl_lahir'] = tgl_lahir
            st.session_state['alamat'] = alamat
            st.session_state['nomor_telepon'] = nomor_telepon
            st.session_state['gejala_responses'] = gejala_responses
            st.spinner('Data Sedang Diproses')
            with st.spinner('Data Sedang Diproses'):
                time.sleep(2)
                
            st.success("Data berhasil disimpan. Silakan lihat hasil diagnosa.")
            st.session_state['page'] = 'Hasil Diagnosa'