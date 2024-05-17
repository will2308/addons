from odoo import models, fields, api



class HospitalOperationDua(models.Model):
    _name = 'hospital.operation.dua'
    _description = 'Hospital Operation Dua'
    _log_access = False

    name = fields.Char(string='Name')
    
