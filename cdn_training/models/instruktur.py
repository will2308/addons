from odoo import models, fields, api

class Instruktur(models.Model):
    _name = 'instruktur'
    _description = 'instruktur'
    _inherits = {'res.partner':'partner_id'}

    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner',required=True,ondelete='cascade')
    keahlian_ids = fields.Many2many(comodel_name='keahlian', string='keahlian')

class Keahlian(models.Model):
    _name = 'keahlian'
    _description = 'keahlian'

    name = fields.Char(string='Keahlian',required=True)
    

