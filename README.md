# Movie Recommendation System

This is a Movie Recommendation System built using machine learning algorithms. It uses user data and preferences to recommend movies that best match their interests.

## Features

- Recommends movies based on a variety of factors such as user ratings, genre preferences, etc.
- Utilizes machine learning algorithms for predictions.
- Can handle large datasets and provides personalized recommendations.

## Movie Posters

Here are some example movie posters used in the recommendation system:

### Iron Man
![Iron Man](images/ironman.png)

### Batman
![Batman](images/batman.png)

## Installation

### Prerequisites

Before running this project, you will need to have the following installed:

- Python 3.x
- pip (Python package installer)
- Jupyter Notebook
- Git
- [Git LFS](https://git-lfs.github.com/) (for handling large files like `.pkl`)

## Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Tejas1730/Movie-Recommandation-AI.git
   cd movie-recommend
2. **Install the required libraries**:

   Make sure all dependencies are installed:

   ```bash
   pip install pandas numpy scikit-learn
   pip install streamlit
3. **Run the python ipynb file**:

   ```bash
   jupyter nbconvert --to notebook --execute --inplace movierecommend.ipynb   

4. **Run the python app.py**:

   ```bash
   streamlit run app.py
