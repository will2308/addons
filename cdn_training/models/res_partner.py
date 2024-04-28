from odoo import models, fields, api



class ResPartner(models.Model):
    _inherit = 'res.partner'


    jenis_kel = fields.Selection(string='Jenis Kelamin', selection=[('l', 'Laki Laki'), ('p', 'Perempuan'),])
    profinsi_id = fields.Many2one('ref.profinsi', string='Profinsi')
    kota_id = fields.Many2one('ref.kota', string='Kota')
    kecamatan_id = fields.Many2one('ref.kecamatan', string='Kecamatan')
    desa_id = fields.Many2one('ref.desa', string='Desa')
    peserta_id = fields.Many2one('peserta', string='Peserta')
