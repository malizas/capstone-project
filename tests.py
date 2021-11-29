from unittest import TestCase
from server import app
from model import connect_to_db, example_data, db
from flask import Flask, session

class FlaskTests(TestCase):
    """Flask tests Class"""
    def setUp(self):
        """Set Up -- stuff to do before every test"""
        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'key'

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1

        connect_to_db(app, "postgresql:///testdb")

        db.create_all()
        example_data()

    def homepage(self):
        """Test Homepage"""
        result = self.client.get('/')
        self.assertIn(b"Welcome to k-Templates!", result.data)

    def register(self):
        """Register Test"""
        result = self.client.post('/user',
                                data={"email":"testing@email.com", "password": "testing"},
                                follow_redirects=True)
        self.assertIn(b"Registration complete!, Account has been created", result.data)

    def login(self):
        """Login Test"""
        result = self.client.post('/login',
                                data={"email":"user1@test.com", "password": "test_password"},
                                follow_redirects=True)
        self.assertIn(b"Login Successful!", result.data)

    def template_creator(self):
        result = self.client.get('/template_creator')
        self.assertIn(b"Template with photocards", result.data)

    def tearDown(self):
        """Tear Down -- stuff to do after every test"""
        db.session.remove()
        db.drop_all()
        db.engine.dispose()


if __name__ == "__main__":
    import unittest
    unittest.main()