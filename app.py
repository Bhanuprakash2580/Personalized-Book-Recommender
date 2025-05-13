# 📚 Personalized Book Recommender System

import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os

# Set page configuration
st.set_page_config(layout="wide")

# Utility to load pickle safely
def load_pickle(filename):
    path = os.path.join(os.path.dirname(books.pkl), books.pkl)
    with open(path, 'rb') as f:
        return pickle.load(f)

# Session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Authentication (placeholder)
def login(username, password):
    if username == "admin" and password == "password":
        st.session_state.logged_in = True
    else:
        st.error("Invalid username or password")

def logout():
    st.session_state.logged_in = False

# Login UI
if not st.session_state.logged_in:
    st.title("🔐 Login")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.form_submit_button("Login"):
            login(username, password)

# Main App
else:
    st.header("📚 Personalized Book Recommender System")
    st.markdown("##### This app uses collaborative filtering to recommend books based on reader preferences.")

    # Sidebar: logout
    if st.sidebar.button("Logout"):
        logout()

    # Load models/data
    try:
        books = load_pickle('books.pkl')
        popular = load_pickle('popular.pkl')
        pt = load_pickle('pt.pkl')
        similarity_scores = load_pickle('similarity_scores.pkl')
    except FileNotFoundError as e:
        st.error("❌ Required model/data file is missing. Please check your deployment setup.")
        st.stop()

    # 🔥 Top 50 Books
    st.sidebar.title("🔥Top 50 Books")
    if st.sidebar.button("SHOW"):
        cols = st.columns(5)
        for i, (_, row) in enumerate(popular.iterrows()):
            with cols[i % 5]:
                st.image(row['Image-URL-M'])
                st.text(row['Book-Title'])
                st.text(row['Book-Author'])

    # 📖 Book Recommendation Logic
    def recommend(book_name):
        index = np.where(pt.index == book_name)[0][0]
        similar_items = sorted(enumerate(similarity_scores[index]), key=lambda x: x[1], reverse=True)[1:6]
        recommendations = []
        for i in similar_items:
            temp = books[books['Book-Title'] == pt.index[i[0]]].drop_duplicates('Book-Title')
            recommendations.append([
                temp['Book-Title'].values[0],
                temp['Book-Author'].values[0],
                temp['Image-URL-M'].values[0]
            ])
        return recommendations

    # Sidebar: Book Recommender
    st.sidebar.title("🤖 Similar Book Suggestions")
    selected_book = st.sidebar.selectbox("Select a book", pt.index.values)
    if st.sidebar.button("Recommend Me"):
        recs = recommend(selected_book)
        cols = st.columns(5)
        for i, rec in enumerate(recs):
            with cols[i]:
                st.image(rec[2])
                st.text(rec[0])
                st.text(rec[1])

    # 📊 Raw Data Viewer
    st.sidebar.title("📊 Data Used")
    if st.sidebar.button("Show Raw Data"):
        try:
            books_df = pd.read_csv("Data/Books.csv")
            users_df = pd.read_csv("Data/Ratings.csv")
            ratings_df = pd.read_csv("Data/Users.csv")
        except FileNotFoundError:
            st.error("❌ CSV files not found. Ensure they're in a `data/` folder.")
            st.stop()

        st.subheader("Books Data")
        st.dataframe(books_df)
        st.subheader("User Ratings")
        st.dataframe(ratings_df)
        st.subheader("Users Info")
        st.dataframe(users_df)

    st.markdown("---")
    st.markdown("**Built with ❤️ using Streamlit | Reimagined for reliability**")
