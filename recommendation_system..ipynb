# enhanced_job_recommendation.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random

# Sample dataset with job titles, categories, and skills
data = {
    'title': [
        'Drone Director',
        'Computer Magician',
        'Ex-Data Explorer',
        'Dream Designer',
        'Virtual Reality Guide',
        'Robot Trainer',
        'Superhero Coach',
        'Waste Recycling Specialist',
        'Quantum Economist',
        'Smart Agriculture Advisor'
    ],
    'category': [
        'Tech Innovation',
        'IT / Computer',
        'Research & Analysis',
        'Creative Design',
        'Virtual Experience',
        'Robotics',
        'Training & Leadership',
        'Environment / Recycling',
        'Science & Math',
        'Agriculture & Smart Farming'
    ],
    'skills': [
        'drones, photography, cinematography',
        'coding, algorithms, hacking',
        'data analysis, statistics, research',
        'creativity, design, visualization',
        'VR, simulation, gaming',
        'robotics, AI, programming',
        'mentoring, leadership, fitness',
        'waste management, recycling, sustainability',
        'math, quantum theory, economics',
        'agriculture, IoT, automation'
    ]
}

df = pd.DataFrame(data)

# TF-IDF Vectorizer for skills
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(df['skills'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Favorites list
favorites = []

# Recommendation by title
def recommend_by_title(job_title, top_n=3):
    if job_title not in df['title'].values:
        return f"No job found with title '{job_title}'."
    idx = df[df['title'] == job_title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    recommended = df['title'].iloc[[i[0] for i in sim_scores]].tolist()
    return recommended

# Recommendation by skills
def recommend_by_skills(user_skills, top_n=3):
    user_vec = tfidf.transform([user_skills])
    sim_scores = cosine_similarity(user_vec, tfidf_matrix)[0]
    top_indices = sim_scores.argsort()[-top_n:][::-1]
    recommended = df['title'].iloc[top_indices].tolist()
    return recommended

# Recommendation by category
def recommend_by_category(category, top_n=3):
    filtered = df[df['category'].str.contains(category, case=False)]
    if filtered.empty:
        return f"No jobs found in category '{category}'."
    return filtered['title'].tolist()[:top_n]

# Surprise job
def surprise_job():
    return random.choice(df['title'].tolist())

# Add to favorites
def add_to_favorites(job_title):
    if job_title in df['title'].values and job_title not in favorites:
        favorites.append(job_title)
        return f"Added '{job_title}' to favorites!"
    return f"Job '{job_title}' is already in favorites or does not exist."

# Show favorites
def show_favorites():
    if not favorites:
        return "No favorites yet."
    return favorites

# Interactive menu
def menu():
    while True:
        print("\n=== Job Recommendation System ===")
        print("1. Recommend by Job Title")
        print("2. Recommend by Your Skills")
        print("3. Recommend by Category")
        print("4. Surprise Me!")
        print("5. Add Job to Favorites")
        print("6. Show Favorites")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            title = input("Enter job title: ")
            print("Recommended Jobs:", recommend_by_title(title))
        elif choice == '2':
            skills = input("Enter your skills (comma separated): ")
            print("Recommended Jobs:", recommend_by_skills(skills))
        elif choice == '3':
            category = input("Enter category: ")
            print("Recommended Jobs:", recommend_by_category(category))
        elif choice == '4':
            print("Surprise Job:", surprise_job())
        elif choice == '5':
            job = input("Enter job title to add to favorites: ")
            print(add_to_favorites(job))
        elif choice == '6':
            print("Your Favorites:", show_favorites())
        elif choice == '7':
            print("Exiting. Have a great day!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
