# custom_module/models/candidate.py

from odoo import models, fields, api
import requests

class HospitakCandidate(models.Model):
    _name = 'hospital.candidate'
    _description = 'Candidate'

    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    year = fields.Integer(string='Year')

    @classmethod
    def sync_candidates_from_api(cls):
        url = 'http://localhost:8000/api/candidate'
        response = requests.get(url)
        if response.status_code == 200:
            candidates_data = response.json().get('data', [])
            for candidate_data in candidates_data:
                cls.create({
                    'name': candidate_data.get('name'),
                    'email': candidate_data.get('email'),
                    'phone': candidate_data.get('phone'),
                    'year': candidate_data.get('year'),
                    # Add other fields as needed
                })
