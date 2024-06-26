from odoo import models, fields, api
from datetime import timedelta

class TrainingCourse(models.Model):
    _name = 'training.course'
    _description = 'tabel Training Course'

    name = fields.Char(string='Nama Kursus',required=True)
    keterangan = fields.Text(string='Keterangan')
    user_id = fields.Many2one(comodel_name='res.users',string='Penanggung Jawab')
    session_line = fields.One2many(comodel_name='training.session', inverse_name='course_id', string='Sesi Training')
    product_ids = fields.Many2many('product.product', string='Peralatan / Konsumsi', domain=[('product_training','=','konsumsi'),('product_training','=','training_kit')])

    _sql_constrains = [
        ('name_course_unique', 'UNIQUE(name)', 'Nama kursus sudah ada')
    ]

class TrainingSession(models.Model):
    _name = 'training.session'
    _description = 'Training Session'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string='Sesi Training',required=True,tracking=True)
    course_id = fields.Many2one(comodel_name="training.course", string='ID Kursus', required=True,tracking=True)
    start_date = fields.Date(string='Tanggal Mulai', required=True,tracking=True)
    duration = fields.Float(string='Durasi', required=True,tracking=True)
    seats = fields.Integer(string='Jumlah Peserta', required=True,default=1,tracking=True)
    instruktur_id = fields.Many2one(comodel_name='instruktur', string='Nama Instruktur')
    alamat = fields.Char(string='Alamat', related='instruktur_id.street')
    no_hp = fields.Char(related='instruktur_id.mobile')
    email = fields.Char(related='instruktur_id.email')
    jenis_kel = fields.Selection(related='instruktur_id.jenis_kel')
    peserta_ids = fields.Many2many('peserta', string='Peserta')
    jml_peserta = fields.Integer(compute='_compute_jml_peserta', string='Jumlah Peserta')
    state = fields.Selection(string='Status', selection=[('draf', 'Draf'), ('progress', 'Sedang Berlangsung'),('done', 'Selesai')], default="draf")
    # end_date = fields.Date(string='Tanggal Bearakhir', )
    end_date = fields.Date(string='Tanggal Bearakhir', compute='_compute_end_date')
    
    
    @api.depends('peserta_ids')
    def _compute_jml_peserta(self):
        for rec in self:
            rec.jml_peserta = len(rec.peserta_ids)

    @api.onchange('start_date','duration')
    def _compute_end_date(self):
        for rec in self:
            if rec.start_date and rec.duration:
                start_date = fields.Date.from_string(rec.start_date)
                end_date = start_date + timedelta(days=rec.duration)
                rec.end_date = fields.Date.to_string(end_date)
            else:
                rec.end_date = False

    def action_confirm(self):
        self.state = 'progress'
    
    def action_done(self):
        self.state = 'done'

    def action_draf(self):
        self.state = 'draf'

    
    

    
    
    
    
    
    


    
    
