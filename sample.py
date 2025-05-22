import streamlit as st
st.title("📚 Personalized Book Recommender")
book_name = st.text_input("Enter a book you like:")
if st.button("Recommend"):
    recommended_books = get_recommendations(book_name)
    for book in recommended_books:
        st.write(book)
