# Personalized-Book-Recommender
ML Project

A book recommendation system built using Popularity-Based Recommender, Collaborative Filtering, and Cosine Similarity. This project provides personalized book recommendations to users based on their preferences. It is implemented using Flask as the web framework.

Data Description
We've three dataset -
• Book data – (ISBN, Book-Title, Book-Author, Year-Of-Publication, Publisher, Image-URL-S, Image-URL-M, Image-URL-L)
• Users data - (User-ID, Location, Age)
• Ratings data - (User-ID, ISBN, Book-Rating)

# Project Overview
This project aims to develop a book recommendation system based on historical data to provide personalized book suggestions. The goal is to enhance users' reading experiences by recommending books that align with their preferences and interests.

# Dataset
The dataset used for this project is obtained from Kaggle. It contains book-related data, including titles, authors, genres, and user interactions, which will be analyzed to generate recommendations.
Use this link
https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset

## Technologies Used
- **Python**: Primary programming language
- **Jupyter Notebook**: For data analysis and model development
- **pandas**: For data manipulation and processing
- **cosine similarity**: To measure the similarity between books
- **pickle**: To save the trained recommendation model
- **Streamlit**: To create an interactive web application for users to input book details and receive recommendations

## Features
- Analyzes historical book data to generate recommendations
- Uses cosine similarity to find similar books
- Saves the trained recommendation model for efficient predictions
- Provides an interactive interface using Streamlit

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Bhanuprakash2580/Personalized-Book-Recommender.git
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```   

## Usage
1. Run the Jupyter Notebook to analyze the dataset and train the model.
2. Save the trained model using the `pickle` library.
3. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```
4. Enter book details in the web application to receive recommendations.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License.

## Acknowledgments
- Kaggle for providing the dataset
- The open-source community for supporting libraries like pandas, Streamlit, and scikit-learn
