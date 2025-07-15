import streamlit as st
import pandas as pd
import seaborn as sns
from PIL import Image
import plotly.express as px
import matplotlib.pyplot as plt

def run():
    # Membuat Title
    st.title('Aplikasi Prediksi Rating Pemain FIFA 2022')

    # Membuat Sub Header
    st.subheader('Page mengenai Exploratory Data Analysis dari dataset FIFA 2022')

    # Menambahkan Gambar
    image = Image.open('soccer.jpg')
    st.image(image, caption='FIFA 2022')

    # Menambahkan Teks
    st.write('Page ini dibuat oleh **Ali Aufa**')

    # magic syntax

    st.write('# Suka main FIFA?')

    '''
    Pada page kali ini, penulis akan melakukan explorasi sederhana.
    Dataset yang digunakan adalah dataset FIFA 2022.
    Dataset ini berasal dari web sofifa.com.
    '''

    #
    st.write('# Dataset')
    # Show DataFrame
    data = pd.read_csv('https://raw.githubusercontent.com/FTDS-learning-materials/phase-1/master/w1/P1W1D1PM%20-%20Machine%20Learning%20Problem%20Framing.csv')
    st.dataframe(data)

    # Membuat Bar Plot
    st.write('#### Plot Attacking WorkRate')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x='AttackingWorkRate', data=data)
    st.pyplot(fig)

    # Membuat Histogram
    st.write('#### Historam of Rating')
    fig =plt.figure(figsize=(15,5))
    sns.histplot(data['Overall'],bins=30,kde=True)
    st.pyplot(fig)

    # Membuat Bar Plot
    st.write('#### Histogram Berdasarkan Input User')
    pilihan = st.selectbox('Pilih column :', ('Age','Weight','Height','ShootingTotal'))
    fig = plt.figure(figsize=(15,5))
    sns.histplot(data[pilihan], bins=30, kde=True)
    st.pyplot(fig)


    # Membuat Plotly plot
    st.write('#### Ploty Plot - ValueEUR dengan Overall')
    fig = px.scatter(data, x='ValueEUR', y='Overall', hover_data =['Name','Age'])
    st.plotly_chart(fig)



if __name__ =='__main__':
    run()