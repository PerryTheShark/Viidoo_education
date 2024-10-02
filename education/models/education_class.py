from odoo import fields, models

class EducationClass(models.Model):
    # _inherit = ["education.student.abstract"]
    _name = 'education.class'
    _description = 'Education Class'

    name = fields.Char(string='Class Name')
    code = fields.Char(string='Class Code')

    # computed fields
    total_students = fields.Integer(compute='_compute_total_students', string='Total Students')

    # relationship fields
    school_id = fields.Many2one('education.school', string='School')
    student_ids = fields.One2many('education.student', 'class_id', string='Students')
    teacher_ids = fields.Many2many('res.partner', string='Teachers')

    def _compute_total_students(self):
        for record in self:
            record.total_students = len(record.student_ids)

    def get_all_students(self):
        # Khởi tạo đối tượng education.student (đây là một recordset rỗng của model education.student)
        student = self.env['education.student']
        all_students = student.search([])
        print("All Students: ", all_students)

    def create_classes(self):
        # Giá trị để tạo bản ghi student 01
        student_01 = {
            'name': 'Student 01',
        }
        # Giá trị để tạo bản ghi student 02
        student_02 = {
            'name': 'Student 02'
        }
        # Giá trị để tạo bản ghi lớp học
        class_value = {
            'name': 'Class 01',
            # Đồng thời tạo mới 2 học sinh
            'student_ids': [
                (0, 0, student_01),
                (0, 0, student_02)
            ]
        }
        record = self.env['education.class'].create(class_value)

    def change_class_name(self):
        self.ensure_one()
        self.name = 'Class 12A1'

    def classes_has_student(self, all_classes):
        return all_classes.filtered(lambda c: len(c.student_ids) >= 1)

    def show_classes_has_student(self):
        classes = self.env['education.class'].search([])
        print("classes that have students", self.classes_has_student(classes))

    def add_student(self):
        self.ensure_one()
        self.write({
            'student_ids': [(0, 0, {
                'name': 'Student'
            })]
        })