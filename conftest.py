from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    director_1 = Director(id=1, name='John Peterson')
    director_2 = Director(id=2, name='Peter Johnson')
    director_3 = Director(id=3, name='Steven Madison')

    director_dao.get_one = MagicMock(return_value=director_1)
    director_dao.get_all = MagicMock(return_value=[director_1, director_2, director_3])
    director_dao.create = MagicMock(return_value=Director(id=4, name='Jerry Butcher'))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    genre_1 = Genre(id=1, name='comedy')
    genre_2 = Genre(id=2, name='action')
    genre_3 = Genre(id=3, name='horror')

    genre_dao.get_one = MagicMock(return_value=genre_1)
    genre_dao.get_all = MagicMock(return_value=[genre_1, genre_2, genre_3])
    genre_dao.create = MagicMock(return_value=Genre(id=4, name='detective'))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie_1 = Movie(id=1, title='Йеллоустоун', description='описание 1', trailer='link', year=2000, rating=7.6,
                    genre_id=1, director_id=1)
    movie_2 = Movie(id=2, title='Омерзительная восьмерка', description='описание 2', trailer='link', year=2001,
                    rating=9.0, genre_id=2, director_id=2)
    movie_3 = Movie(id=3, title='Рокетмен', description='описание 3', trailer='link', year=2002, rating=8.1, genre_id=3,
                    director_id=3)

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])
    movie_dao.create = MagicMock(return_value=Movie(id=4, title='Дюна', description='описание 4', trailer='link',
                                                    year=2021, rating=8.9, genre_id=1, director_id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao
