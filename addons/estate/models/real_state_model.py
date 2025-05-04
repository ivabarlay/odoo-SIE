from odoo import fields, models

class RealState(models.Model):
    _name = "estate_property"

    name = fields.Char('Empleado', required=True)
    casos = fields.Integer('Número de casos', required=True)
