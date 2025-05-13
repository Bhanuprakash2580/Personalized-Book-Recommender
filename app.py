# import the libraries
import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os

with open(os.path.join(os.path.dirname("E:\PBRS\Personalized-Book-Recommender\books.pkl"), 'books.pkl'), 'rb') as f:
    books = pickle.load(f)


# Set page configuration
st.set_page_config(layout="wide")

# Initialize session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Login function
def login(username, password):
    # Replace this with your actual authentication logic
    if username == "admin" and password == "password":
        st.session_state.logged_in = True
    else:
        st.error("Invalid username or password")

# Logout function
def logout():
    st.session_state.logged_in = False

# Login form
if not st.session_state.logged_in:
    st.title("🔐 Login")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
        if submit:
            login(username, password)
else:
    # Main application content
    st.header("📚 Personalized Book Recommender System")

    st.markdown('''
                ##### The site using collaborative filtering suggests books from our catalog. 
                ##### We recommend top 50 books for everyone as well. 
                ''')

    # Add a logout button
    if st.sidebar.button("Logout"):
        logout()

    # Import our models
    popular = pickle.load(open('popular.pkl', 'rb'))
    books = pickle.load(open('books.pkl', 'rb'))


    pt = pickle.load(open('pt.pkl', 'rb'))
    similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

    # Top 50 Books
    st.sidebar.title("🔥Top 50 Books")

    if st.sidebar.button("SHOW"):
        cols_per_row = 5
        num_rows = 10
        for row in range(num_rows):
            cols = st.columns(cols_per_row)
            for col in range(cols_per_row):
                book_idx = row * cols_per_row + col
                if book_idx < len(popular):
                    with cols[col]:
                        st.image(popular.iloc[book_idx]['Image-URL-M'])  # Displays the image
                        st.text(popular.iloc[book_idx]['Book-Title'])  # Displays the Book Title
                        st.text(popular.iloc[book_idx]['Book-Author'])  # Display the Author name

    # Function to recommend Books
    def recommend(book_name):
        index = np.where(pt.index == book_name)[0][0]
        similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]
        # Create a list to populate with book information
        data = []
        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
            data.append(item)
        return data

    # Dropdown to select books
    book_list = pt.index.values
    st.sidebar.title("Similar Book Suggestions")
    selected_book = st.sidebar.selectbox("Select a book from the dropdown", book_list)

    if st.sidebar.button("Recommend Me"):
        book_recommend = recommend(selected_book)
        cols = st.columns(5)
        for col_idx in range(5):
            with cols[col_idx]:
                if col_idx < len(book_recommend):
                    st.image(book_recommend[col_idx][2])
                    st.text(book_recommend[col_idx][0])
                    st.text(book_recommend[col_idx][1])

    # Import data
    books = pd.read_csv("E:\PBRS\Personalized-Book-Recommender\Data\Books.csv")  # books data
    users = pd.read_csv("E:\\PBRS\\Personalized-Book-Recommender\\Data\\Users.csv") # Users location and age data
    ratings = pd.read_csv("E:\PBRS\Personalized-Book-Recommender\Data\Ratings.csv")  # Users rating data

    st.sidebar.title("📊 Data Used")

    if st.sidebar.button("Show"):
        st.subheader('This is the books data we used in our model')
        st.dataframe(books)
        st.subheader('This is the User ratings data we used in our model')
        st.dataframe(ratings)
        st.subheader('This is the user data we used in our model')
        st.dataframe(users)

    # Footer
    st.markdown("---")
    st.markdown("**Personalized Book Recommender System** | Built with ❤️ using Streamlit") 












