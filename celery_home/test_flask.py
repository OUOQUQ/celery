from celery_test import add, star, task_update
from unittest.mock import Mock, patch


def test_add():
    mock_add = Mock()
    with patch('celery_test.add', mock_add):
        mock_add.return_value = 11
        result = add(1, 10)
        assert result == 11


def test_star():
    mock_star = Mock()
    with patch('celery_test.star', mock_star):
        mock_star.return_value = 'ok'
        result = star(5)
        assert result == 'ok'


def test_task_update():
    mock_task_update = Mock()
    with patch('celery_test.task_update', mock_task_update):
        mock_task_update.return_value = 'PENDING'
        result = task_update('d3fb586d-a517-47af-b3c8-40f87')
        assert result == 'PENDING'
    

