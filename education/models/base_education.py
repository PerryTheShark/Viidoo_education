from odoo import fields, models

class BaseEducation(models.AbstractModel):
    _name = 'education.student.abstract'
    _description = 'Base Education'

    active = fields.Boolean(string='Active')

    def do_active(self):
        for r in self:
            r.active = not r.active