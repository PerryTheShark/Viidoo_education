from odoo import fields, models, api


class EducationSchoolYear(models.Model):
    _name = 'education.school.year'
    _description = 'Description'

    name = fields.Char('Name', required=True)
    # report_id = fields.One2many('education.admission.report', 'school_year_id', string='Report')