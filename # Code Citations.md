# Code Citations

## License: unknown
https://github.com/Shankar297/Book-Recommendation-System/tree/99c2ef48713e44096e0a74f722eabbb05db78e50/streamlit_app.py

```
('popular.pkl', 'rb'))
    books = pickle.load(open('books.pkl', 'rb'))
    pt = pickle.load(open('pt.pkl', 'rb'))
    similarity_scores = pickle.load
```


## License: unknown
https://github.com/mathew-2/Book-recommender-system/tree/710030d98da1de23b315cde23c004528fee742b1/app.py

```
popular.pkl', 'rb'))
    books = pickle.load(open('books.pkl', 'rb'))
    pt = pickle.load(open('pt.pkl', 'rb'))
    similarity_scores = pickle.load(open
```


## License: unknown
https://github.com/ameympatil/Book-Recommendation-System/tree/a599a6568ee0c474b520836c316b736a88cb2696/demo.py

```
recommend(book_name):
        index = np.where(pt.index == book_name)[0][0]
        similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1
```


## License: unknown
https://github.com/jhakrraman/Book_Recommendation_System/tree/575fa0735a55e143292c383591c304dc9e4d8706/Application.py

```
:
            item = []
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values)
```


## License: unknown
https://github.com/Gupta0Kaustubh/Book-Recommender-System/tree/006528e1121363f74f9b5e224eb29dfe07725e61/app.py

```
]
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend
```

