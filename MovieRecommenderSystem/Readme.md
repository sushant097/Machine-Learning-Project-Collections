## Movie Recommender System
We build end-to-end movie recommender system with tmbd 5000 movie dataset which recommend movies based on cosine similarity.

### Data: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

### Demo
![](movie_recommender_demo.gif)

### How to run?
1. First download data and place two csv file inside data directory.
2. Install packages on requirements.txt as: `pip install requirements.txt`
3. Download similarity matrix (Trained) from Drive: https://drive.google.com/file/d/1vDdHLd3rYBVNw6Xifk7-BnB5TGOrxxPI/view?usp=sharing
4. Run on cmd: `streamlit run app.py`
5. (Optional) To deploy on heroku, create new app and follow instruction.

#### Full Deployed App: [Heroku](https://mrs-imbd.herokuapp.com/)

