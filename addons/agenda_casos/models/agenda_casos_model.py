from odoo import fields, models

class AgendaCasos(models.Model):
    _name = "agenda_casos"

    name = fields.Char('Empleado', required=True)
    casos = fields.Integer('Número de casos', required=True)
