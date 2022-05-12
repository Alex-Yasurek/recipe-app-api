from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTests(TestCase):

    def test_wait_for_db_ready(self):
        """Test waiting for db when db is available"""
        # overwrite built-in ConnectHandler function
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            # have overwritten func just return True
            gi.return_value = True
            call_command('wait_for_db')
            # assert func was called 1 time
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            # raise error first 5 times its called then True on 6th
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
