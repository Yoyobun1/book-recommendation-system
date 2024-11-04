import pickle
import streamlit as st
import numpy as np


st.header("Book Recommender System using Collaborative Filtering")

model = pickle.load(open('artifacts/model.pkl', 'rb'))
book_names = pickle.load(open('artifacts/book_names.pkl', 'rb'))
final_rating = pickle.load(open('artifacts/final_rating.pkl', 'rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))


def fetch_poster(suggestion):
    book_names = []
    ids_index = []
    poster_url = []
    
    # Flatten the suggestion array if it's 2D
    suggestion = suggestion.flatten()
    
    for book_id in suggestion:
        book_names.append(book_pivot.index[book_id])
    
    for name in book_names:
        # Check if name exists in 'final_rating['title']' to avoid index error
        matches = np.where(final_rating['title'] == name)[0]
        if matches.size > 0:
            ids_index.append(matches[0])
        else:
            print(f"Warning: Title '{name}' not found in final_rating DataFrame")
    
    for idx in ids_index:
        # Correct usage of iloc with brackets
        url = final_rating.iloc[idx]['image_url']
        poster_url.append(url)
    
    return poster_url


def recommend_books(book_name):
    book_list = []
    
    # Get the book_id of the selected book
    book_id = np.where(book_pivot.index == book_name)[0][0]
    
    # Get the distances and suggestions of 6 similar books
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)
    
    # Fetch the poster URLs for the recommended books
    poster_url = fetch_poster(suggestion)
    
    # Flatten the suggestion array and get book names
    suggestion = suggestion.flatten()
    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        book_list.append(books)
    
    return book_list, poster_url

    


selected_books = st.selectbox(
    "Type or Select a book", book_names
    )


if st.button("Show Recommendations"):
    recommendation_books, poster_url = recommend_books(selected_books)
    col1, col2, col3, col4, col5 = st.columns(5)   
    
    with col1:
        st.text(recommendation_books[1]) 
        st.image(poster_url[1],width=100)
    
    with col2:
        st.text(recommendation_books[2]) 
        st.image(poster_url[2],width=100)
        
    with col3:
        st.text(recommendation_books[3]) 
        st.image(poster_url[3],width=100)
        
    with col4:
        st.text(recommendation_books[4]) 
        st.image(poster_url[4],width=100)
        
    with col5:
        st.text(recommendation_books[5]) 
        st.image(poster_url[5],width=100)