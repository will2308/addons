from odoo import models, fields, api, _



class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    cancel_days = fields.Integer('cancel_days', config_parameter='om_hospital.cancel_day')
