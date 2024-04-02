import streamlit as st
import pandas as pd
import pickle
import json

# Melakukan load model dan file-file lain yang dibutuhkan
with open('model_scaler.pkl', 'rb') as file_1:
  scaler = pickle.load(file_1)
with open('model_pca.pkl', 'rb') as file_2:
  pca = pickle.load(file_2)
with open('model_kp.pkl', 'rb') as file_3:
  kp = pickle.load(file_3)
with open('index_cols.txt', 'r') as file_4:
  index_cols = json.load(file_4)
with open('num_cols.txt', 'r') as file_5:
  num_cols = json.load(file_5)
with open('cat_cols.txt', 'r') as file_6:
  cat_cols = json.load(file_6)

  def run():
    st.title('Apart Helper')
    # Membuat form user input
    with st.form(key='Apart'):
        st.write('### Input')
        neighborhood = st.selectbox('Neighborhood',options=['Palm Jumeirah', 'Jumeirah Lake Towers', 'Culture Village',
                                                        'Downtown Dubai', 'Dubai Marina', 'Business Bay', 'Old Town',
                                                        'Al Kifaf', 'Meydan', 'Arjan', 'Jumeirah Beach Residence',
                                                        'Dubai Creek Harbour (The Lagoons)', 'Greens', 'City Walk',
                                                        'Al Furjan', 'DAMAC Hills', 'Jumeirah Golf Estates', 'Jumeirah',
                                                        'Dubai Hills Estate', 'Umm Suqeim', 'Motor City', 'DIFC',
                                                        'Jumeirah Village Circle', 'Barsha Heights (Tecom)', 'Al Barari',
                                                        'Dubai Production City (IMPZ)', 'The Hills', 'The Views',
                                                        'Dubai Sports City', 'Dubai Silicon Oasis',
                                                        'Jumeirah Village Triangle', 'Mohammed Bin Rashid City',
                                                        'Dubai Harbour', 'Bluewaters', 'International City',
                                                        'Falcon City of Wonders', 'Mina Rashid', 'Town Square',
                                                        'Green Community', 'Al Barsha', 'Al Sufouh', 'Dubai Festival City',
                                                        'Jebel Ali', 'Dubai Land', 'World Trade Center', 'Mudon',
                                                        'Discovery Gardens', 'Remraam', 'Mirdif',
                                                        'Dubai South (Dubai World Central)', 'Dubai Healthcare City',
                                                        'wasl gate', 'Dubai Residence Complex', 'Al Quoz'])
        price = st.number_input('Price', min_value=0, max_value=35000000, value='min', step=100000)
        size_in_sqft = st.number_input('Size in Squarefoot', min_value=0, max_value=9576, value='min', step=100)
        price_per_sqft = st.number_input('Price per Squarefoot', min_value=0, max_value=4805.87, value='min', step=100)


        age = st.number_input('Umur', min_value=0, max_value=100, value='min')
        marital = st.selectbox('Status Pernikahan',options=["married","divorced","single"])
        education = st.selectbox('Pendidikan',options=["unknown","secondary","primary","tertiary"])
        default = st.selectbox('Apakah pernah melewatkan pembayaran kredit?',options=["yes","no"])
        if default=='yes':
            default=1
        else:
           default=0
        balance = st.number_input('Saldo', min_value=0, max_value=10000, value='min', step=100)
        housing = st.selectbox('Apakah mempunyai pinjaman perumahan?',options=["yes","no"])
        if housing=='yes':
            housing=1
        else:
           housing=0
        loan = st.selectbox('Apakah mempunyai pinjaman?',options=["yes","no"])
        if loan=='yes':
            loan=1
        else:
           loan=0
        contact = st.selectbox('Jenis kontak dengan bank',options=["unknown","telephone","cellular"])
        day = st.number_input('Tanggal terakhir kali dihubungi', min_value=1, max_value=31, value='min')
        month = st.selectbox('Bulan terakhir kali dihubungi',options=["jan","feb","mar","apr","may","jun",
                                                                      "jul","aug","sep","oct","nov","dec"])
        campaign = st.number_input('Jumlah kontak dengan bank pada kampanye ini', min_value=1, max_value=100, value='min')
        pdays = st.number_input('Jumlah hari yang telah lewat setelah klien dihubungi sebelumnya pada kampanye sebelumnya (isi -1 jika belum pernah dihubungi sebelumnya)',
                                 min_value=-1, max_value=100, value='min')
        previous = st.number_input('Jumlah kontak dengan bank sebelum kampanye ini', min_value=0, max_value=100, value='min')
        poutcome = st.selectbox('Hasil dari kampanye sebelumnya',options=["unknown","other","failure","success"])
        submit = st.form_submit_button('Predict')


    # Membuat data inference
    data_inf = {
        'age': age,
        'job' : job,
        'marital' : marital,
        'education' : education,
        'default' : default,
        'balance': balance,
        'housing': housing,
        'loan': loan,
        'contact': contact,
        'day': day,
        'month': month,
        'campaign': campaign,
        'pdays': pdays,
        'previous': previous,
        'poutcome': poutcome,
    }

    # Menjadikan data inference sebagai dataframe dan menampilkannya
    st.write('## Informasi Klien')
    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf, hide_index=True)

    data_inf_final = data_inf[list_cols]

    # Melakukan prediksi terhadap data inference
    if submit:
        prediksi = model_rf.predict(data_inf_final)
        st.write('# Hasil')
        if prediksi == 0:
            st.write('Klien diprediksi tidak akan menerima penawaran deposito')
        else:
           st.write('Klien diprediksi akan menerima penawaran deposito')

if __name__== '__main__':
    run()