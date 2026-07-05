# 🎬 Movie Recommendation System (Streamlit + AWS S3 + Render)

A machine learning–based movie recommendation web app built using Python, Streamlit, and cosine similarity, deployed on Render, with large dataset files stored securely on AWS S3.
Workflow:
- Data Ingestion: Load raw movie datasets from structured sources
- Data Cleaning & Preprocessing: Handle missing values and inconsistencies, standardize and normalize relevant fields
- Feature Engineering: Extract meaningful attributes from metadata (genres, cast, overview, keywords)
- Text Feature Construction: Combine multiple textual fields into a unified feature representation
- Vectorization: Convert text data into numerical form using NLP techniques (Bag of words / Count Vectorization)
- Similarity Computation: Compute pairwise similarity using cosine similarity to measure movie relevance
- Recommendation Engine: Rank and return the top-5 most similar movies based on similarity scores



🚀 Live Demo
👉 https://movie-recommender-system-nyke.onrender.com



📌 Features
- Content-based movie recommendations
- Search movies and get similar suggestions
- Fast and interactive Streamlit UI
- Scalable model storage using AWS S3
- Fully deployed on Render (cloud hosting)

🧠 How It Works
- The system recommends movies based on similarity scores:
- Movies are converted into feature vectors
- Cosine similarity is computed
- Top matching movies are recommended

🏗️ Tech Stack
- Python 
- Streamlit
- Pandas & NumPy 
- Scikit-learn 
- AWS S3 (for model storage)
- Render (deployment platform)


📂 Project Structure
  Movie-Recommender/
│
├── app.py                  # Main Streamlit app
├── requirements.txt        # Dependencies
├── .gitignore              # Ignored files
└── README.md               # Project documentation

☁️ AWS S3 Setup
- Large model files are stored in S3:
movies.pkl
similarity.pkl

⚙️ Installation (Local Setup)
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
pip install -r requirements.txt

▶️ Run Locally
streamlit run app.py

📊 Dataset
Movie metadata dataset used for training
Cosine similarity matrix for recommendations

⚠️ Important Notes
Large .pkl files are NOT stored in GitHub due to size limits
AWS S3 is used for scalable model storage
Streamlit app loads models dynamically at runtime

👨‍💻 Author
Niyanta
📍 Toronto, Canada
💼 ML Engineer
