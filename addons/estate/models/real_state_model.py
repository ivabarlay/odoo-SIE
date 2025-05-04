from odoo import fields, models

class RealState(models.Model):
    _name = "estate_property"

    name = fields.Char('Plan Name', required=True)
