
import unittest
from app import create_app, db
from app.models import Message

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['TESTING'] = True
        with self.app.app_context():
            db.create_all()

    def test_create_message(self):
        response = self.client.post('/create', json={
            'account_id': '1',
            'sender_number': '12345',
            'receiver_number': '67890'
        })
        self.assertEqual(response.status_code, 201)

    def test_get_messages(self):
        response = self.client.get('/get/messages/1')
        self.assertEqual(response.status_code, 200)

    def test_search_messages(self):
        self.client.post('/create', json={
            'account_id': '1',
            'sender_number': '12345',
            'receiver_number': '67890'
        })
        response = self.client.get('/search?sender_number=12345')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()


