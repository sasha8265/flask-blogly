from unittest import TestCase

from app import app
from models import db, User

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///users_test'
app.config['SQLALCHEMY_ECHO'] = False

app.config['TESTING'] = True

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

DEFAULT_IMG_URL = "https://upload.wikimedia.org/wikipedia/commons/8/89/Portrait_Placeholder.png"

class UserViewsTestCase(TestCase):

    def setUp(self):
        """Add Sample User"""

        User.query.delete()

        test_user = User(first_name="Jane", last_name="Doe", image_url=DEFAULT_IMG_URL)
        db.session.add(test_user)
        db.session.commit()

        self.user_id = test_user.id
        self.user = test_user

    def tearDown(self):
        db.session.rollback()

    def test_list_users(self):
        with app.test_client() as client:
            resp = client.get("/users")
            html = resp.get_data(as_text=True)

            self.assertIn('Jane Doe', html)


    def test_show_user(self):
        with app.test_client() as client:
            resp = client.get(f"/users/{self.user_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Jane Doe', html)


    def test_add_user(self):
        with app.test_client() as client:
            data = {"first_name": "John", "last_name": "Smith", "image_url": DEFAULT_IMG_URL}
            resp = client.post("/users/add-user", data=data, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('John Smith</a></li>', html)


    def test_delete_user(self):
        with app.test_client() as client:
            resp = client.post(f"/users/{self.user_id}/delete-user", follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertNotIn(f'<li><a href="/users/{self.user_id}', html)

        


