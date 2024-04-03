import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json

# Load necessary files and models
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

# Define page configuration
def run():
    st.title('APART HELPER')

    # Create user input form
    with st.form(key='person'):
        st.write('## Input Apart Data')
        neighborhood = st.selectbox('Neighborhood', options=['Palm Jumeirah', 'Jumeirah Lake Towers', 'Culture Village',
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

        price = st.number_input('Price', min_value=0, max_value=35000000, value='min', step=1)
        size_in_sqft = st.number_input('Size in Square Feet', min_value=0, max_value=9576, value='min', step=100)
        price_per_sqft = st.number_input('Price per Square Feet', min_value=0, max_value=4806, value='min', step=100)
        no_of_bedrooms = st.number_input('Total Bedrooms', min_value=0, max_value=5, value='min', step=1)
        no_of_bathrooms = st.number_input('Total Bathrooms', min_value=0, max_value=6, value='min', step=1)
        maid_room = st.selectbox('Maid Room', options=['True', 'False'])
        concierge = st.selectbox('Concierge', options=['True', 'False'])
        pets_allowed = st.selectbox('Pets Allowes', options=['True', 'False'])
        private_garden = st.selectbox('Private Garden', options=['True', 'False'])
        private_gym = st.selectbox('Private Gym', options=['True', 'False'])
        private_jacuzzi = st.selectbox('Private Jacuzzi', options=['True', 'False'])
        private_pool = st.selectbox('Private Pool', options=['True', 'False'])
        shared_pool = st.selectbox('Shared Pool', options=['True', 'False'])

        submit = st.form_submit_button("Predict")
        
        # Create new data
        data_inf = {
          'neighborhood': neighborhood,
          'price': price,
          'size_in_sqft': size_in_sqft,
          'price_per_sqft': price_per_sqft,
          'no_of_bedrooms': no_of_bedrooms,
          'no_of_bathrooms': no_of_bathrooms,
          'maid_room': maid_room,
          'concierge': concierge,
          'pets_allowed' : pets_allowed,
          'private_garden' : private_garden,
          'private_gym' : private_gym,
          'private_jacuzzi' : private_jacuzzi,
          'private_pool' : private_pool,
          'shared_pool' : shared_pool
        }

    # Predict
    if submit:
        # Prepare numeric and categorical data
        inf_num = pd.DataFrame([data_inf])[num_cols]
        inf_cat = pd.DataFrame([data_inf])[cat_cols]
        
        # Scale and perform dimension reduction
        inf_scaled = scaler.transform(inf_num)
        inf_scaled_pca = pca.transform(inf_scaled)

        inf_final = np.concatenate([inf_scaled_pca, inf_cat], axis=1)
        inf_final = pd.DataFrame(inf_final, columns=['PCA1', 'PCA2', 'PCA3'] + cat_cols)
        inf_final = inf_final.infer_objects()

        result = kp.predict(inf_final, categorical=index_cols)
        st.divider()
        
        # Prediction explanation
        if result is not None:
            if result == 0:
                keterangan_prediksi = "Cluster Apartemen Mewah\n\n" \
                                    "- Mencakup apartemen paling mahal dalam kumpulan data.\n" \
                                    "- Mungkin memiliki ukuran terbesar dalam satuan luas.\n" \
                                    "- Mungkin memiliki harga per satuan luas tertinggi.\n" \
                                    "- Memiliki jumlah kamar tidur dan kamar mandi yang lebih tinggi dibandingkan dengan cluster lainnya."
            elif result == 1:
                keterangan_prediksi = "Cluster Apartemen Menengah\n\n" \
                                    "- Memiliki harga lebih rendah daripada Cluster 0 (Cluster Apartemen Mewah) tetapi lebih tinggi dari Cluster 2 (Cluster Apartemen Ekonomis).\n" \
                                    "- Mungkin memiliki ukuran sedang dalam satuan luas dibandingkan dengan cluster lainnya.\n" \
                                    "- Harga per satuan luas berada di antara dua cluster lainnya.\n" \
                                    "- Memiliki jumlah kamar tidur dan kamar mandi yang sedang."
            else:
                keterangan_prediksi = "Cluster Apartemen Ekonomis\n\n" \
                                    "- Mencakup apartemen paling terjangkau dalam kumpulan data.\n" \
                                    "- Mungkin memiliki ukuran terkecil dalam satuan luas.\n" \
                                    "- Mungkin memiliki harga per satuan luas terendah.\n" \
                                    "- Memiliki jumlah kamar tidur dan kamar mandi yang lebih rendah dibandingkan dengan cluster lainnya."

            # Display result
            st.write('# Result')
            st.write(f'Prediksi : {int(result)} - {keterangan_prediksi}')
            
            # Show data table based on the result
            st.subheader('Data Table Based on Prediction Result')
            data_cluster = pd.read_csv("data_setelah_clustering.csv")
            data_cluster = data_cluster.drop(columns=['Unnamed: 0']) 
            if result == 0:
                 st.write(data_cluster.loc[(data_cluster['cluster']==0)].sample(n=5))
            elif result == 1:
                st.write(data_cluster.loc[(data_cluster['cluster']==1)].sample(n=5))
            else:
                st.write(data_cluster.loc[(data_cluster['cluster']==2)].sample(n=5))
        else:
            st.write('Error: Prediction result is None')

if __name__ == '__main__':
    run()