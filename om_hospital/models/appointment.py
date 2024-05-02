import odoo from models, fields, api



class Appointment(models.Model):
    _name = 'appointment'
    _description = 'Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    patient_id = fields.Many2one('hospital.patient', string='Patient')    