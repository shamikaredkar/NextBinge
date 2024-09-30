import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:11]
    for i in movies_list:
        print(new_df.iloc[i[0]].title)

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
st.title("NextBinge") 
option = st.selectbox('Select a movie',movies['title'].values)

if st.button('Recommend'):
    recommend(option)
    st.write(option)
    
