# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Final Year Project',
    'version': '1.0',
    'category': 'eCommerce',
    'sequence': -101,
    'depends': [],
    'data': [
        'wizard/proposal.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/ideas.xml',
        'views/section.xml',
        'views/proposal.xml',
        'views/res_users.xml',
        'views/menus.xml',
    ],

    'installable': True,
    'application': True,
}
