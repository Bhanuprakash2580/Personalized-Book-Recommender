# Import the necessary libraries
import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os

# ✅ Set Streamlit page configuration (this MUST be the first Streamlit command)
st.set_page_config(layout="wide")

# ✅ Define the absolute file paths
base_path = r"E:\PBRS\Personalized-Book-Recommender"
books_file_path = os.path.join(base_path, "books.pkl")
popular_file_path = os.path.join(base_path, "popular.pkl")
pt_file_path = os.path.join(base_path, "pt.pkl")
similarity_scores_path = os.path.join(base_path, "similarity_scores.pkl")

# ✅ Function to load pickle files safely
def load_pickle_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            return pickle.load(f)
    else:
        st.error(f"❌ File not found: {file_path}")
        return None

# ✅ Load the required datasets
books = load_pickle_file(books_file_path)
popular = load_pickle_file(popular_file_path)
pt = load_pickle_file(pt_file_path)
similarity_scores = load_pickle_file(similarity_scores_path)

# ✅ Initialize session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ✅ Login function
def login(username, password):
    if username == "admin" and password == "password":
        st.session_state.logged_in = True
    else:
        st.error("❌ Invalid username or password")

# ✅ Logout function
def logout():
    st.session_state.logged_in = False

# ✅ Login form
if not st.session_state.logged_in:
    st.title("🔐 Login")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
        if submit:
            login(username, password)
else:
    # ✅ Main application content
    st.header("📚 Personalized Book Recommender System")

    st.markdown("""
    ##### This system uses collaborative filtering to suggest books.
    ##### We recommend the **Top 50 Books** for general users as well.
    """)

    # ✅ Add a logout button
    if st.sidebar.button("Logout"):
        logout()

    # ✅ Top 50 Books Section
    st.sidebar.title("🔥 Top 50 Books")
    if st.sidebar.button("SHOW"):
        cols_per_row = 5
        num_rows = 10
        for row in range(num_rows):
            cols = st.columns(cols_per_row)
            for col in range(cols_per_row):
                book_idx = row * cols_per_row + col
                if popular is not None and book_idx < len(popular):
                    with cols[col]:
                        st.image(popular.iloc[book_idx]['Image-URL-M'])
                        st.text(popular.iloc[book_idx]['Book-Title'])
                        st.text(popular.iloc[book_idx]['Book-Author'])

    # ✅ Function to Recommend Books
    def recommend(book_name):
        if pt is None or similarity_scores is None or books is None:
            return []

        index = np.where(pt.index == book_name)[0][0]
        similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]

        data = []
        for i in similar_items:
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item = [
                temp_df.drop_duplicates('Book-Title')['Book-Title'].values[0],
                temp_df.drop_duplicates('Book-Title')['Book-Author'].values[0],
                temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values[0]
            ]
            data.append(item)
        return data

    # ✅ Dropdown to select books
    if pt is not None:
        book_list = pt.index.values
        st.sidebar.title("📖 Similar Book Suggestions")
        selected_book = st.sidebar.selectbox("Select a book", book_list)

        if st.sidebar.button("Recommend Me"):
            book_recommend = recommend(selected_book)
            cols = st.columns(5)
            for col_idx in range(5):
                with cols[col_idx]:
                    if col_idx < len(book_recommend):
                        st.image(book_recommend[col_idx][2])
                        st.text(book_recommend[col_idx][0])
                        st.text(book_recommend[col_idx][1])

    # ✅ Load book data safely
    books_csv_path = os.path.join(base_path, "Data", "Books.csv")
    users_csv_path = os.path.join(base_path, "Data", "Users.csv")
    ratings_csv_path = os.path.join(base_path, "Data", "Ratings.csv")

    if os.path.exists(books_csv_path):
        books = pd.read_csv(books_csv_path)
    if os.path.exists(users_csv_path):
        users = pd.read_csv(users_csv_path)
    if os.path.exists(ratings_csv_path):
        ratings = pd.read_csv(ratings_csv_path)

    # ✅ Sidebar Data Preview
    st.sidebar.title("📊 Data Used")
    if st.sidebar.button("Show Data"):
        if books is not None:
            st.subheader('Books Data')
            st.dataframe(books)
        if ratings is not None:
            st.subheader('User Ratings Data')
            st.dataframe(ratings)
        if users is not None:
            st.subheader('User Information Data')
            st.dataframe(users)

    # ✅ Footer
    st.markdown("---")
    st.markdown("**Personalized Book Recommender System** | Built with ❤️ using Streamlit")
