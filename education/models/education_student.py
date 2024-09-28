from odoo import fields, models

class EducationStudent(models.Model):
    _name = 'education.student'
    _description = 'Education Student'

    name = fields.Char(string='Student Name')
    student_code = fields.Char(string='Student Code')
    class_id = fields.Many2one('education.class', string='Class')