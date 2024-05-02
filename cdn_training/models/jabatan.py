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
    # pejabat_ids = fields.One2many('instruktur', 'jabatan_id', string='pejabat')
    
    
    # @api.constraints('jenis_jabatan')
    # def _check_jabatan(self):
    #     for rec in self:
    #         if rec.jenis_jabatan == 'staf':
    #             continue
    #         existing_rec = self.search([('jenis_jabatan','=','kepala')])
    #         if len(existing_rec) > 0:
    #             raise ValidationError('Jabatan sudah terisi')