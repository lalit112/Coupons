# project/test_basic.py

import os
import unittest

from database.models import db
from run import app

TEST_DB = 'test.db'


class BasicTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                                                os.path.join(app.config['BASEDIR'], TEST_DB)
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
        self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

    ###############
    #### tests ####
    ###############

    def test_get_coupon(self):
        with app.test_client() as client:
            # send data as POST form to endpoint
            sent = {'userid': 9999}
            result = client.post(
                '/fetch/',
                data=sent
            )
            self.assert_(result.status_code == 200)

    def test_generate(self):
        with app.test_client() as client:
            # send data as POST form to endpoint
            sent = {'count': 100}
            result = client.post(
                '/generate/generate_coupon',
                data=sent
            )
            # check result from server with expected data
            self.assertEqual(
                result.status_code, 201
            )


if __name__ == "__main__":
    unittest.main()
