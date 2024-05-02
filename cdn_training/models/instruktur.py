from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Instruktur(models.Model):
    _name = 'instruktur'
    _description = 'instruktur'
    _inherits = {'res.partner':'partner_id'}

    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner',required=True,ondelete='cascade')
    keahlian_ids = fields.Many2many(comodel_name='keahlian', string='keahlian')
    jabatan_id = fields.Many2one('jabatan', string='jabatan', domain="([('jenis_jabatan','=','staf')])")
    jenis_jabatan = fields.Selection([
        ('kepala', 'Kepala / Pimpinan Lembaga'),
        ('wakil', 'Wakil Kepala Lembaga'),
        ('staf', 'Staf'),
    ], string='Jenis Jabatan')

    @api.onchange('jenis_jabatan')
    def _onchange_(self):
        if self.jenis_jabatan == 'kepala':
            self.jabatan_id = self.env['jabatan'].search([('jenis_jabatan','=','kepala')])
        elif self.jenis_jabatan == 'wakil':
            self.jabatan_id = self.env['jabatan'].search([('jenis_jabatan','=','wakil')])

    def action_update_jabatan(self):
        verify_jabatan = self.env['jabatan'].search([('pejabat_id','=', 'null')])
        if verify_jabatan == 'null':
            self.jabatan_id.pejabat_id = self.id
        else:
            raise ValidationError('Jabatan sudah terisi')
        return True

class Keahlian(models.Model):
    _name = 'keahlian'
    _description = 'keahlian'

    name = fields.Char(string='Keahlian',required=True)
    

