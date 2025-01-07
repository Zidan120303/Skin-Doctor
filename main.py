import streamlit as st        
from streamlit_option_menu import option_menu      
from gejala_klasifikasi import show_gejala_klasifikasi        
from form_diagnosa import show_form_diagnosa        
from hasil_diagnosa import show_hasil_diagnosa        
  
  
def main():        
      
    if 'page' not in st.session_state:        
        st.session_state.page = "Klasifikasi Gejala"        
      
    with st.sidebar:        
        selected = option_menu("Menu",         
            ["Klasifikasi Gejala", "Form Diagnosa", "Hasil Diagnosa"],        
            icons=["clipboard", "clipboard-data", "check2"], 
            menu_icon="cast", 
            default_index=0       
        )        
       
    if selected == "Klasifikasi Gejala":        
        st.session_state.page = "gejala_klasifikasi"       
        show_gejala_klasifikasi()        
    elif selected == "Hasil Diagnosa":        
        st.session_state.page = "hasil_diagnosa"  # Set halaman ke hasil diagnosa        
        show_hasil_diagnosa()        
    elif selected == "Form Diagnosa":        
        st.session_state.page = "form_diagnosa"  # Set halaman ke form diagnosa        
        show_form_diagnosa()        
  
if __name__ == "__main__":        
    main()        
