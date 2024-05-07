from odoo import models, fields, api



class PatientTag(models.Model):
    _name = 'patient.tag'
    _description = 'Patient Tag'

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Acvtive', default=True)
    color = fields.Integer('Color')
    color_2 = fields.Char(string='Color 2')
    
    
    
