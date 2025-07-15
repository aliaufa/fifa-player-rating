import streamlit as st

# Ambil libraries dari model inference
import pickle
import json
import pandas as pd
import numpy as np

st.set_page_config(
   page_title='FIFA 2022',
   layout='wide',
   initial_sidebar_state='expanded'
)


# Copy Syntax Model Loading di Inference (Load files)

with open('list_cat_cols.txt', 'r') as file_1:
  list_cat_cols = json.load(file_1)

with open('list_num_cols.txt', 'r') as file_2:
  list_num_cols = json.load(file_2)

with open('encoder.pkl', 'rb') as file_3:
  encoder = pickle.load(file_3)

with open('scaler.pkl', 'rb') as file_4:
  scaler = pickle.load(file_4)

with open('model_lin_reg.pkl', 'rb') as file_5:
  model_lin_reg = pickle.load(file_5)

def run():
    # Membuat Form
    with st.form(key='form_fifa_2022'):
        # user input nama, defaultnya kosong boleh dikosongin
        name = st.text_input('Name', value='')
        ## opsi 2 name = st.text_input('Name', value='--Masukkan Nama Anda--')

        # step naik 1 angka lebih tinggi atau lebih rendah, kalau 2 naik + 2
        # value itu yang ditampilkan di UI
        age = st.number_input('Age', min_value=16, max_value=60, value=25, step=1, help='Usia Pemain')

        weight = st.number_input('Weight', min_value=50, max_value=150, value=70)

        height = st.slider('Height', 50, 250, 170)

        price = st.number_input('Price',min_value=0, max_value=1000000000, value=0)
        st.markdown('---')

        attacking_work_rate = st.selectbox('Attacking Work Rate',('Low','Medium','High'), index=2)
        deffensive_work_rate = st.radio('Deffensive Work Rate',('Low','Medium','High'), index=1)
        st.markdown('---')

        pace = st.number_input('Pace', min_value=0, max_value=100, value=50)
        shooting = st.number_input('Shooting', min_value=0, max_value=100, value=50)
        passing = st.number_input('Passing', min_value=0, max_value=100, value=50)
        dribbling = st.number_input('Dribbling', min_value=0, max_value=100, value=50)
        defending = st.number_input('Defending', min_value=0, max_value=100, value=50)
        physicality = st.number_input('Physicality', min_value=0, max_value=100, value=50)
        
        # tombol predict
        submitted = st.form_submit_button('Predict')
    
    # Nama kolom samakan dengan data train
    data_inf = {
            'Name': name,
            'Age': age,
            'Height': height,
            'Weight': weight,
            'Price':price,
            'AttackingWorkRate':attacking_work_rate,
            'DefensiveWorkRate':deffensive_work_rate,
            'PaceTotal':pace,
            'ShootingTotal':shooting,
            'PassingTotal':passing,
            'DribblingTotal':dribbling,
            'DefendingTotal': defending,
            'PhysicalityTotal': physicality
            }
    # data_inf =pd.DataFrame([data_inf])
    # st.dataframe(data_inf)
    st.write("## Data User")

    with st.expander("Lihat DataFrame mentah", expanded=False):
        st.dataframe(data_inf, width= 400)
    
    data_inf =pd.DataFrame([data_inf])

    if submitted:
        # Split between categorical and numerical
        data_inf_num = data_inf[list_num_cols]
        data_inf_cat = data_inf[list_cat_cols]

        # Scaling and Encoding
        data_inf_scaled = scaler.transform(data_inf_num)
        data_inf_encoded = encoder.transform(data_inf_cat)
        data_inf_final = np.concatenate([data_inf_scaled, data_inf_encoded], axis = 1)

        # Predict using linreg
        y_pred_inf = model_lin_reg.predict(data_inf_final)

        st.write('# Rating : ',str(int(y_pred_inf)))


if __name__ == '__main__':
  run()
