*All projects in this class are individual projects, not group projects.  You may not look at or discuss code with others until after you have submitted your own individual effort.*


## Movie Recommendation System

This project implements a basic movie recommendation system using object-oriented programming and data manipulation with Pandas and NumPy. The recommendation system reads user-movie rating data, calculates similarities between users, and generates movie recommendations based on these similarities.

### Deliverables
- Complete all functions in `recommendation_system.py`
- Make sure you pass all the tests.

### Description

#### User similarity

To calculate user similarity, you first identify the movies watched by both users. Then, you create two vectors of ratings based solely on the common movies. Finally, you compute the cosine similarity between these two vectors.

#### Top similar users
To determine the top N most similar users for a given user_id, you iterate through all users in the system, calculating the similarity score between the specified user and each other user using the calculate_user_similarity method. Then, you return the top N users with the highest similarity scores.

### Personalized movie recommendations.
To generate movie recommendation for a given user_id, follow the following steps:
1. Compute the top 10 similar users.
2. Compute the average rating of all the movies watched by these similar users.
3. Exclude movies that the specified user has already watched.
4. Sort the remaining movies by their average rating in decreasing order.
5. Return the top N movies from this sorted list.

Be sure to consult the docstrings for each function and incorporate the provided test cases for verification.

### Testing on larger data
Download this file: https://files.grouplens.org/datasets/movielens/ml-latest-small.zip, move it to ~/data, and unzip it. Use the test.ipynb file to test your code on a larger dataset.

