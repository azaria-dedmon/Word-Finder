from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

class FlaskTests(TestCase):
    def before_test(self):
        app.config['TESTING'] = True

    def test_create_board(self):
       with app.test_client() as client:
            res = client.get('/')
            self.assertIn('board', session)
            self.assertEqual(res.status_code, 200)
            self.assertIn(b'<p>Highest Score:', res.data)
            self.assertIn(b'<p>User has played', res.data)

    def test_check_answer(self):
        """Test if word is valid"""
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['board'] = [['B', 'A', 'C', 'K', 'E'],
                                 ['A', 'B', 'C', 'D', 'E'],
                                 ['A', 'B', 'C', 'D', 'E'],
                                 ['A', 'B', 'C', 'D', 'E'],
                                 ['A', 'B', 'C', 'D', 'E']]

        res = client.get('/check-answer?word=back')
        self.assertEqual(res.json['result'], 'ok')

        self.assertEqual(res.status_code, 200)

    def test_not_on_board(self):
        with app.test_client() as client:
            res = client.get('/')
            res = client.get('/check-answer?word=mummy')
            self.assertEqual(res.json['result'], 'not-on-board')

    def test_not_word(self):
        with app.test_client() as client:
            res = client.get('/')
            res = client.get('/check-answer?word=fojfjefj')
            self.assertEqual(res.json['result'], 'not-word')
            self.assertEqual(res.status_code, 200)


