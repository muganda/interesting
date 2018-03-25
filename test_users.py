from unittest import TestCase, main
from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_sqlalchemy import SQLAlchemy
import json

from app import app

class UserTestCase(TestCase):
    def setUp(self):
        self.client = app.test_client
        #with app.app_context():
        #    db.drop_all()
        #    db.create_all()  

    def test_registration(self):
        data = {"first_name":"David","password":"123456","last_name":"Ssali"}
        res = self.client().post('/api/v1/users/register',data=json.dumps(data),content_type='application/json')
        self.assertEqual(res.status_code,200)

    def test_index(self):
	    res = self.client().get('/api/v1/index')
	    self.assertEqual(res.status_code,200)

if __name__ == "__main__":
    main()
