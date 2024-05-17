from odoo import models, fields, api, _



class HospitalOperation(models.Model):
    _name = 'hospital.operation'
    _description = 'Hospital Operation'
    _log_access = False

    doctor_id = fields.Many2one('res.users', string='doctor')
    operation_name = fields.Char(string='Name')

    @api.model
    def name_create(self, name):
        return self.create({'operation_name': name}).name_get()[0]
        
    def name_get(self):
        return [(record.id, "%s" % (record.operation_name)) for record in self]
    