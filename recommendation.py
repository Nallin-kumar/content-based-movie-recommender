import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from rapidfuzz import process  # fuzzy matching

# === Load and train model ===
print("🔄 Loading dataset...")
movies = pd.read_csv(r"D:\Nallin\VS\Website\Hackathon\movies_metadata.csv", low_memory=False)
movies = movies[['title', 'overview']].dropna().drop_duplicates(subset='title').reset_index(drop=True)

print(f"✅ Total movies loaded: {len(movies)}")

print("🧠 Training TF-IDF model...")
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['overview'])

print("🔍 Computing similarity matrix...")
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Create title-to-index mapping
indices = pd.Series(movies.index, index=movies['title'])

# === Fuzzy Matching Recommendation Function ===
def get_recommendations_fuzzy(input_title):
    # Step 1: Fuzzy match to find the closest actual title
    all_titles = movies['title'].tolist()
    closest_match = process.extractOne(input_title, all_titles, score_cutoff=60)

    if not closest_match:
        return f"❌ No similar titles found for: '{input_title}'"

    matched_title = closest_match[0]
    idx = indices[matched_title]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    movie_indices = [i[0] for i in sim_scores]

    return matched_title, movies['title'].iloc[movie_indices].tolist()

# === CLI Loop ===
print("\n✅ Model is ready with fuzzy matching! Type a movie name:")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("🎬 Enter a movie title: ").strip()
    
    if user_input.lower() == 'exit':
        print("👋 Exiting recommendation system. See you!")
        break

    result = get_recommendations_fuzzy(user_input)

    if isinstance(result, str):
        print(result)
    else:
        matched_title, recommendations = result
        print(f"\n🔍 Closest match found: {matched_title}")
        print("🎯 Top 5 similar movies:")
        for i, rec in enumerate(recommendations, 1):
            print(f"{i}. {rec}")
        print()
