import unittest
from app import create_app, db
from flask import json

CLUSTER_API_URL = '/clusters/'


class ClusterTestCase(unittest.TestCase):
    """This class represents the cluster api test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.cluster = {
            'name': 'Cluster1',
            'data': ''
        }

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.session.close()
            db.drop_all()
            db.create_all()

    def test_cluster_creation(self):
        """Test API can create a cluster (POST request)"""
        res = self.client().post(
            CLUSTER_API_URL,
            data=json.dumps(self.cluster),
            content_type='application/json')
        self.assertEqual(res.status_code, 201)

    def test_cluster_get_all(self):
        """Test API can get all clusters (GET request)."""
        res = self.client().post(
            CLUSTER_API_URL,
            data=json.dumps(self.cluster),
            content_type='application/json')
        self.assertEqual(res.status_code, 201)
        res = self.client().get(
            CLUSTER_API_URL
        )
        self.assertEqual(res.status_code, 200)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
