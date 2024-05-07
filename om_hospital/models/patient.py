from odoo import models, fields, api
from datetime import date



class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string='Name', tracking=True)
    ref = fields.Char(string='Reference', tracking=True, default="odoo")
    date_of_birth = fields.Date('date_of_birth')
    age = fields.Integer('Age', compute="_compute_age", tracking=True)
    gender = fields.Selection(string='Gender', selection=[('male', 'Male'), ('female', 'Female'),], tracking=True, default="female")
    active = fields.Boolean(string='Active', default=True)
    appointment_id = fields.Many2one('hospital.appointment', string='appointment')
    image = fields.Image('Image')
    tag_ids = fields.Many2many('patient.tag', string='Tags')

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1
    
    
    
