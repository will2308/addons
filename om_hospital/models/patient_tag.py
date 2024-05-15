from odoo import models, fields, api, _

class PatientTag(models.Model):
    _name = 'patient.tag'
    _description = 'Patient Tag'
    from odoo.exceptions import ValidationError

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Acvtive', default=True, copy=False)
    color = fields.Integer('Color')
    color_2 = fields.Char(string='Color 2')
    sequence = fields.Integer('Sequence')

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get('name'):
            default['name'] = _("%s (copy)", self.name)
        return super(PatientTag, self).copy(default)

    _sql_constraints = [
        ('unique_tag_name', 'unique(name, active)', 'name must be unique'),
        ('chek_sequence', 'chek(sequence > 0)', 'Sequence must be non zero, positif number')
    ]

    
