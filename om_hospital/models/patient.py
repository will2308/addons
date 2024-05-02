from odoo import models, fields, api



class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string='Name', tracking=True)
    ref = fields.Char(string='Reference', tracking=True)
    age = fields.Integer('Age', tracking=True)
    gender = fields.Selection(string='Gender', selection=[('male', 'Male'), ('female', 'Female'),], tracking=True)
    active = fields.Boolean(string='Active', default=True)
    
    
    
