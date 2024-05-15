from odoo import api, models, fields
from datetime import date
from odoo.exceptions import ValidationError
from dateutil import relativedelta

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string='Name', tracking=True)
    ref = fields.Char(string='Reference', tracking=True)
    date_of_birth = fields.Date('date_of_birth')
    age = fields.Integer('Age', compute="_compute_age", search="_search_age", tracking=True)
    # age = fields.Integer('Age', compute="_compute_age", inverse="_inverse_compute_age", tracking=True)
    gender = fields.Selection(string='Gender', selection=[('male', 'Male'), ('female', 'Female'),], tracking=True, default="female")
    active = fields.Boolean(string='Active', default=True)
    appointment_id = fields.Many2one('hospital.appointment', string='appointment')
    image = fields.Image('Image')
    tag_ids = fields.Many2many('patient.tag', string='Tags')
    appointment_count = fields.Integer(compute='_compute_appointment_count', string='appointment_count', store=True)
    appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string='appointment')
    parent = fields.Char(string='Parent')
    partner_name = fields.Char(string='Partner Name')
    marital_status = fields.Selection(string='Martial Status', selection=[('married', 'Married'), ('single', 'Sigle'),], tracking=True)
    
    @api.model
    def create(self, vals):
        print("........... data : ", vals)
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals)

    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        for rec in self:
            rec.appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', rec.id)])

    @api.constrains('date_of_birth')
    def _chek_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and date_of_birth > fields.Date.today():
                raise ValidationError('input not acceptable')

    @api.ondelete(at_uninstall=False)
    def _chek_appointment(self):
        for rec in self:
            if rec.appointment_ids:
                raise ValidationError('You cannot delete patient with appointment !')

    @api.model
    def create(self, vals):
        print("........... data : ", vals)
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals)

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1

    # @api.depends('age')
    # def _inverse_compute_age(self):
    #     today = date.today()
    #     for rec in self:
    #         rec.date_of_birth = today - relativedelta.relativedelta(years=rec.age)

    def _search_age(self, operator, value):
        date_of_birth = date.today() - relativedelta.relativedelta(years=value)
        start_year = date_of_birth.replace(day=1,month=1) 
        end_year = date_of_birth.replace(day=31,month=12)
        return [('date_of_birth','>=', start_year),('date_of_birth','<=', end_year)] 
    
    def name_get(self):
        patient_list = []
        # for record in self:
        #     name =  record.ref + ' - ' + record.name
        #     patient_list.append((record.id, name))
        # return patient_list
        return [(record.id, "%s - %s" % (record.ref, record.name)) for record in self]

    def action_test(self):
        print('........click click click click')
    
