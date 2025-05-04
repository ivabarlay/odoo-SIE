# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Estate',
    'version': '1.2',
    'category': 'Category',
    'sequence': 15,
    'summary': 'Test',
    'description': "Tests",
    'website': 'https://www.odoo.com/page/crm',
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml'
    ],

    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'application': True
}
