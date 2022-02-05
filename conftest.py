from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.model.director import Director


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
