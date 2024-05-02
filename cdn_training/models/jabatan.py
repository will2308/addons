from odoo import models,fields,api
# from odoo.exceptions import ValidationError

class jabatan(models.Model):
    _name = 'jabatan'
    _description = 'jabatan'

    name = fields.Char(string='Nama Jabatan',required=True)
    keterangan = fields.Text(string='Keterangan')
    jenis_jabatan = fields.Selection([
        ('kepala', 'Kepala / Pimpinan Lembaga'),
        ('wakil', 'Wakil Kepala Lembaga'),
        ('staf', 'Staf'),
    ], string='Jenis Jabatan')
    pejabat_id = fields.Many2one('instruktur', string='nama pejabat')
   