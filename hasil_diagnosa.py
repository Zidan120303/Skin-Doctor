import streamlit as st        
import pandas as pd        
from datetime import datetime    
from dateutil.relativedelta import relativedelta    
  
from data import data_aturan, solusi_penyakit, data_gejala  
  
def show_hasil_diagnosa():        
    st.subheader("Hasil Diagnosa")
       
    if 'gejala_responses' in st.session_state:
        st.write(f"**Nama:** {st.session_state['nama']}")    
        age_years, age_months, age_days = calculate_age(st.session_state['tgl_lahir'])    
        st.write(f"**Usia:** {age_years} Tahun, {age_months} Bulan, {age_days} Hari")  
        st.write(f"**Alamat:** {st.session_state['alamat']}")    
        st.write(f"**Nomor Telepon:** {st.session_state['nomor_telepon']}")
                
        gejala_responses = st.session_state['gejala_responses']        
                   
        gejala_kode = [kode for kode, response in gejala_responses.items() if response == "Ya"]      
  
        df_gejala = pd.DataFrame(data_gejala, columns=['kode gejala', 'keterangan'])      
        gejala_ditemukan = df_gejala[df_gejala['kode gejala'].isin(gejala_kode)]      
      
        if not gejala_ditemukan.empty:       
            st.dataframe(gejala_ditemukan, hide_index=True, use_container_width=True)  
            penyakit = None        
            for rule in data_aturan:        
                if set(rule[1].split(',')) == set(gejala_kode):        
                    penyakit = rule[3]        
                    break       
            if penyakit:          
                st.info(f"Dari hasil pemeriksaan pada gejala yang anda alami, anda terdiagnosa terkena penyakit {penyakit}")  
                # Menampilkan informasi tentang penyakit        
                st.markdown(        
                    f"""        
                    <div style="border: 2px solid #2196F3; padding: 10px; border-radius: 5px; margin-bottom: 20px; text-align: justify;">        
                        <strong>Informasi tentang Penyakit:</strong><br>        
                        <img src="{solusi_penyakit[penyakit]['url']}" style="width: 400px; height: auto;" alt="Gambar Penyakit {penyakit}"><br>        
                        {solusi_penyakit[penyakit]['info'][0]}<br>        
                    </div>        
                    """,         
                    unsafe_allow_html=True        
                )        
                    
                st.markdown(        
                    f"""        
                    <div style="border: 2px solid #4CAF50; padding: 10px; border-radius: 5px;">        
                        <strong>Solusi:</strong><br>        
                        {solusi_penyakit[penyakit]['solusi'][0]}        
                    </div>        
                    """,         
                    unsafe_allow_html=True        
                )        
            else:       
                st.write("Tidak ada penyakit yang sesuai dengan gejala yang anda alami.")        
                st.warning("Tidak ada penyakit yang sesuai dengan gejala yang dipilih. Disarankan konsultasikan dengan dokter spesialis kulit!")     
        else:   
            st.warning("Tidak ada gejala yang ditemukan. Sepertinya anda tidak menemukan penyakit yang sesuai dengan gejala yang anda alami.")             
    else:
        st.image('./assets/form.png',width=200)
        st.warning("Silakan isi form diagnosa terlebih dahulu.")        
  
def calculate_age(birthdate):    
    today = datetime.now() 
    delta = relativedelta(today, birthdate)  
    return delta.years, delta.months, delta.days 
