from odoo import fields, models

class EductionSchool(models.Model):

   _name = 'education.school'
   _description = 'School'

   name = fields.Char(string='Name', translate=True, required=True)
   code = fields.Char(string='Code')
   address = fields.Char(string='Address')
   # relationship fields
   class_ids = fields.One2many('education.class', 'school_id', string='Classes')
