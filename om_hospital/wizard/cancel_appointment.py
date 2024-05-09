from odoo import models, fields, api



class CancelAppointmentWizard(models.Model):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'

    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
    reason = fields.Text(string='')
    

    def action_cancel(self):
        return
