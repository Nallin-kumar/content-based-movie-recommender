🎥 Movie Recommendation System (with Fuzzy Matching)
A simple content-based movie recommendation system built with Python.
This CLI-based tool uses TF-IDF vectorization and cosine similarity on movie overviews to suggest similar movies.
It also supports fuzzy matching to handle partial or misspelled movie titles!

📦 Features
✅ Recommends 5 movies similar to your input
✅ Uses fuzzy title matching for better flexibility
✅ Content-based (works using movie descriptions only)
✅ Clean and interactive command-line interface
✅ Beginner-friendly, lightweight and easy to extend                  

🛠️ Tech Stack
✅ Python 3
✅ Pandas
✅ Scikit-learn
✅ RapidFuzz
✅ TF-IDF Vectorizer
✅ Cosine Similarity

📥 Dataset
This project uses the movies_metadata.csv dataset from Kaggle.
Link : https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?select=movies_metadata.csv
⚠️ Note: Due to GitHub file size restrictions, the dataset isn’t included in this repository.
After downloading, place the file in your project directory or update the file path in the code accordingly.

🚀 How to Run
✅ pip install -r requirements.txt   
✅ python recommendation.py

🖥️ Demo
🎬 Enter a movie title: Interstellar

🔍 Closest match found: Interstellar
🎯 Top 5 similar movies:
1. Gravity
2. The Martian
3. Inception
4. Contact
5. 2001: A Space Odyssey

Type exit to quit.

📜 License
This project is open source — feel free to fork and improve it! 🚀



