from odoo import models, fields, api



class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(string='Name')
    age = fields.Integer('Age')
    gender = fields.Selection(string='Gender', selection=[('male', 'Male'), ('female', 'Female'),])
    
    
