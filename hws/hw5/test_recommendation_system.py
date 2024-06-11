import pytest

from recommendation_system import User, Movie, RecommendationSystem

recommender = RecommendationSystem()
recommender.load_data('tiny_ratings.csv')

def test_user_add_rating():
    user = User(user_id=1)
    user.add_rating(movie_id=101, rating=5)
    assert user.ratings[101] == 5

def test_movie_add_rating():
    movie = Movie(movie_id=101)
    movie.add_rating(user_id=1, rating=5)
    assert movie.ratings[1] == 5

def test_load_data():
    assert len(recommender.users) == 5
    assert len(recommender.movies) == 3
    assert recommender.users[1].ratings[11] == 5
    assert recommender.movies[11].ratings[1] == 5
    assert recommender.users[3].ratings[12] == 4
    assert recommender.movies[13].ratings[3] == 5

def test_calculate_user_similarity():
    result = recommender.calculate_user_similarity(1, 3)
    assert result == pytest.approx(0.573804, rel=1e-5)
    result = recommender.calculate_user_similarity(1, 2)
    assert result == pytest.approx(0.964763, rel=1e-5)
    result = recommender.calculate_user_similarity(1, 4)
    assert result == 1.0

def test_calculate_top_n_similar_users():
    sim = recommender.calculate_top_n_similar_users(1)
    expected_users = [4, 5, 2, 3]
    assert [sim[i][0] for i in range(len(sim))] == expected_users
    sim = recommender.calculate_top_n_similar_users(1, 2)
    assert [sim[i][0] for i in range(len(sim))] == expected_users[:2]
    sim = recommender.calculate_top_n_similar_users(2)
    expected_users = [4, 5, 1, 3]
    assert [sim[i][0] for i in range(len(sim))] == expected_users

def test_recommend_movies():
    rec = recommender.recommend_movies(4)
    expected = [(12, 3.5), (13, 2.6666666666666665)]
    for i in range(len(rec)):
        assert rec[i][0] == expected[i][0]
        assert rec[i][1] == pytest.approx(expected[i][1], rel=1e-5)
    rec = recommender.recommend_movies(5)
    for i in range(len(rec)):
        assert rec[i][0] == expected[i][0]
        assert rec[i][1] == pytest.approx(expected[i][1], rel=1e-5)
