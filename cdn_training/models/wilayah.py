from odoo import models, fields, api



class RefProfinsi(models.Model):
    _name = 'ref.profinsi'
    _description = 'Ref Profinsi'

    name = fields.Char(string='Nama Profinsi', required=True)
    kode = fields.Char(string='Kode Profinsi')
    singkat = fields.Char('Singakatan')
    keterangan = fields.Text('Keterangan')
    kota_ids = fields.One2many('ref.kota', 'profinsi_id', string='Daftar Kota')


class RefKota(models.Model):
    _name = 'ref.kota'
    _description = 'Ref Kota'

    name = fields.Char(string='Nama Kota', required=True)
    profinsi_id = fields.Many2one('ref.profinsi', string='Nama Profinsi')
    kode = fields.Char(string='Kode Kota')
    singkat = fields.Char('Singakatan')
    keterangan = fields.Text('Keterangan')
    kecamatan_ids = fields.One2many('ref.kecamatan', 'kota_id', string='Daftar Kecamatan')



class RefKecamatan(models.Model):
    _name = 'ref.kecamatan'
    _description = 'Ref Kecamatan'

    name = fields.Char(string='Nama Kecamatan', required=True)
    kota_id = fields.Many2one('ref.kota', string='Nama Kota / Kabupaten')
    kode = fields.Char(string='Kode Kecamatan')
    keterangan = fields.Text('Keterangan')
    desa_ids = fields.One2many('ref.desa', 'kecamatan_id', string='Daftar Desa')


class RefDesa(models.Model):
    _name = 'ref.desa'
    _description = 'Ref Desa'

    name = fields.Char(string='Nama Desa', required=True)
    kecamatan_id = fields.Many2one('ref.kecamatan', string='Nama Kecamatan')
    kode = fields.Char(string='Kode Desa')
    keterangan = fields.Text('Keterangan')
    

    

    
