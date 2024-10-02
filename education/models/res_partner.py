from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_teacher = fields.Boolean(string='Is a Teacher')

    def _get_all_teachers(self):
        return self.search([('is_teacher', '=', True)])
