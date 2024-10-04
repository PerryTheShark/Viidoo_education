from odoo import fields, models

class EducationStudentDropoutWizard(models.TransientModel):
    _name = 'education.student.dropout.wizard'
    _description = 'Education Student Dropout Wizard'

    def _default_student(self):
        active_model = self.env.context.get('active_model')
        active_id = self.env.context.get('active_id')
        return self.env[active_model].browse(active_id)

    student_id = fields.Many2one('education.student', string='Student',  default=_default_student)
    dropout_reason = fields.Text(string='Dropout Reason')

    def action_confirm(self):
        self.student_id.dropout_reason = self.dropout_reason
        self.student_id.state = 'off'

        result = self.env.ref('education.education_class_action').read()[0]
        res = self.env.ref('education.education_class_view_form', False)
        result['view'] = [(res and res.id or False, 'form')]
        result['res_id'] = self.student_id.class_id.id
        return result
