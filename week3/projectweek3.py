from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

user_skills = []
print("Please enter your skills to find suitable job opportunities.")
preferred_choices = input("Enter your skills separated by commas: ").split(",")
for skill in preferred_choices:
    clean_skill = skill.lower().strip()
    if clean_skill not in user_skills and clean_skill != "":
        user_skills.append(clean_skill)
print("Your skills have been added to your profile.")

print(user_skills)


# 1. Our Temporary Dataset
job_dataset = {
    "Data Scientist": "python sql machine learning data analysis",
    "DevOps Engineer": "aws docker kubernetes automation git",
    "Backend Developer": "java python sql apis git",
    "Frontend Developer": "javascript html css react git",
    "Cybersecurity Analyst": "networks linux security sql"
}

# converting to single line string for vectorization
user_skills_string = " ".join(user_skills)

# preparing the data
job_titles = list(job_dataset.keys())
job_skills = list(job_dataset.values())

# converting into numeric scores
vectorizer = TfidfVectorizer()

# transforming text into vectors
job_vectors = vectorizer.fit_transform(job_skills)
user_vector = vectorizer.transform([user_skills_string])
# calculating cosine similarity
similarity_scores = cosine_similarity(user_vector, job_vectors)

# finding top result
scores = similarity_scores.flatten()
job_scores = list(zip(job_titles, scores))
# sorting by score
job_scores.sort(key=lambda x: x[1], reverse=True)

print("top 3 matches")
for i in range(3):
    print(f"{job_scores[i][0]}: {job_scores[i][1]:.2f}")
