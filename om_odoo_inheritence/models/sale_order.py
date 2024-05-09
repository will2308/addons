from odoo import models, fields, api



class SaleOrder(models.Model):
    # _name = 'sale.order'
    # _description = 'Sale Order'
    _inherit = 'sale.order'

    confirmed_user_id = fields.Many2one('res.users', string='Confirmed User')
