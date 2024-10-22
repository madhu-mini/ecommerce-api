import unittest
import json
from app import create_app
from extensions import db

class ProductAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_product(self):
        # Test creating a product with valid data
        response = self.client.post('/products/', data=json.dumps({
            'title': 'Valid Product',
            'description': 'Valid description',
            'price': 100.0
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)

        # Test creating a product with missing title (validation error)
        response = self.client.post('/products/', data=json.dumps({
            'description': 'No title provided',
            'price': 50.0
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_update_product(self):
        # First create a product
        create_response = self.client.post('/products/', data=json.dumps({
            'title': 'Product to update',
            'description': 'Product description',
            'price': 30.0
        }), content_type='application/json')
        product_id = create_response.get_json()['id']

        # Test updating the product with valid data
        update_response = self.client.put(f'/products/{product_id}', data=json.dumps({
            'title': 'Updated Product',
            'description': 'Updated description',
            'price': 40.0
        }), content_type='application/json')
        self.assertEqual(update_response.status_code, 200)

        # Test updating with invalid data (missing title)
        invalid_update_response = self.client.put(f'/products/{product_id}', data=json.dumps({
            'description': 'No title provided'
        }), content_type='application/json')
        self.assertEqual(invalid_update_response.status_code, 400)

    def test_get_product(self):
        create_response = self.client.post('/products/', data=json.dumps({
            'title': 'Test Product',
            'description': 'Testing',
            'price': 10.0
        }), content_type='application/json')
        product_id = create_response.get_json()['id']

        # Test retrieving the product
        response = self.client.get(f'/products/{product_id}')
        self.assertEqual(response.status_code, 200)

        # Test retrieving a non-existent product
        response = self.client.get('/products/999')
        self.assertEqual(response.status_code, 404)

    def test_delete_product(self):
        create_response = self.client.post('/products/', data=json.dumps({
            'title': 'Product to delete',
            'description': 'Product description',
            'price': 50.0
        }), content_type='application/json')
        product_id = create_response.get_json()['id']

        # Test deleting the product
        delete_response = self.client.delete(f'/products/{product_id}')
        self.assertEqual(delete_response.status_code, 200)

        # Test deleting a non-existent product
        delete_response = self.client.delete('/products/999')
        self.assertEqual(delete_response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
