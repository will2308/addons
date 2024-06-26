from odoo import models, fields, api
from odoo.exceptions import ValidationError
import datetime
from dateutil import relativedelta
from datetime import date

class CancelAppointmentWizard(models.Model):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'

    @api.model
    def default_get(self, fields):
        res = super(CancelAppointmentWizard, self).default_get(fields)
        res['date_cancel'] = datetime.date.today()
        # print("........ context : ", self.env.context.get('active_id'))
        if self.env.context.get('active_id'):
            res['appointment_id'] = self.env.context.get('active_id')
        return res

    appointment_id = fields.Many2one('hospital.appointment', string='Appointment', domain=['|',('state', '=', 'draf'),('priority', 'in', ('0','1', False))])
    reason = fields.Text(string='Reason', default="test reason")
    date_cancel = fields.Date(string='Cancellation Date')    

    def action_cancel(self):
        cancel_day = self.env['ir.config_parameter'].get_param('om_hospital.cancel_day')
        allowed_date = self.appointment_id.booking_date - relativedelta.relativedelta(days=int(cancel_day))
        if allowed_date < date.today():
            raise ValidationError("Sorry, Cancellation is not allowed of this booking")
        self.appointment_id.state = 'cancel'
       
        # print("......cancel day :", cancel_day, "....alloewd_date", allowed_date, "...relativedelta : ", relativedelta.relativedelta(days=int(cancel_day)))
        # print("********** config : ", self.env['ir.config_parameter'].get_param('om_hospital.cancel_day'))
