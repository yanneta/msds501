import numpy as np
import pandas as pd
from collections import defaultdict

class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.ratings = {}  # {movie_id: rating}
    
    def add_rating(self, movie_id, rating):
        # YOUR CODE HERE


class Movie:
    def __init__(self, movie_id):
        self.movie_id = movie_id
        self.ratings = {}  # {user_id: rating}
    
    def add_rating(self, user_id, rating):
        # YOUR CODE HERE


class RecommendationSystem:
    def __init__(self):
        self.users = {} 
        self.movies = {}
    
    def load_data(self, file_path):
        """
        Load user-movie rating data from a CSV file into the recommendation system.

        This method reads a CSV file containing columns 'user_id', 'movie_id', and 'rating'.
        It then populates the 'users' and 'movies' dictionaries with User and Movie objects,
        respectively, and adds the corresponding ratings.

        Args:
             file_path (str): The path to the CSV file containing the ratings data.

        Example:
            >>> recommender = RecommendationSystem()
            >>> recommender.load_data('ratings.csv')
        """
        df = pd.read_csv(file_path)
        # YOUR CODE HERE
    
    def calculate_user_similarity(self, user1, user2):
        """
        Calculate the cosine similarity between two users based on their common movie ratings.

        This method computes the cosine similarity between two users by identifying movies
        that both users have rated and using their ratings to calculate the similarity score.

        Args:
           user1 (int): The ID of the first user.
           user2 (int): The ID of the second user.

        Returns:
           float: The cosine similarity score between the two users.
           A value of 0 indicates no similarity.
        """
        # YOUR CODE HERE
    
    def calculate_top_n_similar_users(self, user_id, n=10):
        """
        Calculate the top N most similar users to the specified user based on their movie ratings.

        This method iterates through all users in the recommendation system, calculates the
        similarity score between the specified user and each other user using the 
        `calculate_user_similarity` method, and returns the top N most similar users.

        Args:
            user_id (int): The ID of the user for whom to find similar users.
            n (int, optional): The number of top similar users to return. Default is 10.

        Returns:
            list of tuple: A list of tuples containing user IDs and their similarity scores,
                       sorted in descending order of similarity. Each tuple is of the form
                       (other_user_id, similarity_score).
        Notes:
        - Users with a similarity score of 0 are not included in the result.
        """
        # YOUR CODE HERE

    def recommend_movies(self, user_id, n=5):
        """
        Recommend the top N movies to a specified user based on the ratings of similar users.

        This method generates movie recommendations for a user by performing the following steps:
        1. Compute the top 10 similar users.
        2. Compute the average rating of all the movies watched by these similar users.
        3. Exclude movies that the specified user has already watched.
        4. Sort the remaining movies by their average rating in decreasing order.
        5. Return the top N movies from this sorted list.

        Args:
            user_id (int): The ID of the user for whom to generate movie recommendations.
            n (int, optional): The number of top movie recommendations to return. Default is 5.

        Returns:
            list of tuple: A list of tuples containing movie IDs and their average ratings, sorted
                       in descending order of average rating. Each tuple is of the form
                       (movie_id, average_rating).
        """
        # YOUR CODE HERE
