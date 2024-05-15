from odoo import models, fields, api
from odoo.exceptions import ValidationError
import datetime

class CancelAppointmentWizard(models.Model):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'

    @api.model
    def default_get(self, fields):
        res = super(CancelAppointmentWizard, self).default_get(fields)
        # res['reason'] = "hello word"
        res['date_cancel'] = datetime.date.today()
        # print("........ context : ", self.env.context.get('active_id'))
        if self.env.context.get('active_id'):
            res['appointment_id'] = self.env.context.get('active_id')
        return res

    appointment_id = fields.Many2one('hospital.appointment', string='Appointment', domain=['|',('state', '=', 'draf'),('priority', 'in', ('0','1', False))])
    reason = fields.Text(string='Reason', default="test reason")
    date_cancel = fields.Date(string='Cancellation Date')    

    def action_cancel(self):
        if self.appointment_id.booking_date == fields.Date.today():
            raise ValidationError("Sorry, Cancellation is not allowed on the sameday of booking")
        self.appointment_id.state = 'cancel'
        return
