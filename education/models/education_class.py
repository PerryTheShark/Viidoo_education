from odoo import fields, models

class EducationClass(models.Model):
    _name = 'education.class'
    _description = 'Education Class'

    name = fields.Char(string='Class Name')
    code = fields.Char(string='Class Code')
    student_ids = fields.One2many('education.student', 'class_id', string='Students')
    total_students = fields.Integer(compute='_compute_total_students', string='Total Students')

    def _compute_total_students(self):
        for record in self:
            record.total_students = len(record.student_ids)