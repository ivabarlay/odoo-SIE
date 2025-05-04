# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'AgendaCasos',
    'version': '1.2',
    'category': 'Administración',
    'sequence': 15,
    'summary': 'Services',
    'description': "Agenda de casos para empleados",
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/agenda_casos_views.xml',
        'views/agenda_casos.xml'
    ],

    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'application': True
}
