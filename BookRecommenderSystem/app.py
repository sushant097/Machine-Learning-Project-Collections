from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Loading saved data and models
popular_df = pickle.load(open('model/popular_df.pickle', 'rb'))
books = pickle.load(open('model/books.pickle', 'rb'))
similarity_scores = pickle.load(open('model/similarity_scores.pickle', 'rb'))
pt = pickle.load(open('model/pivot_table.pickle', 'rb'))


# Function that recommend 4 similar books
def recommend_similar_books(book_name):
    suggestions = []
    # index fetch
    pos = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[pos])), key=lambda x: x[1], reverse=True)[1:5]
    data = []
    for item in similar_items:
        row = []
        temp_df = books[books['Book-Title'] == pt.index[item[0]]]
        temp_df = temp_df.drop_duplicates('Book-Title')  # Dropping duplicates same book of diff ISBN
        row.append(temp_df['Book-Title'].values[0])
        row.append(temp_df['Book-Author'].values[0])
        row.append(temp_df['Image-URL-M'].values[0])

        data.append(row)
    return data


@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           ratings=list(popular_df['avg_rating'].values),
                           )


@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


@app.route('/recommendbooks', methods=['GET'])
def recommend_books():
    if request.method == 'GET':
        book_name = str(request.args.get('book-name'))
        print(book_name)
        books_recommended = recommend_similar_books(book_name)
        return render_template('recommend.html',
                               data = books_recommended)



if __name__ == "__main__":
    app.run(debug=True)
