# -*- coding: utf-8 -*-
{
    'name': "Hospital Management",

    'summary': """Hospital Management System""",

    'description': """
        Hospital management system
    """,

    'author': "Cnedana 2000",
    'website': "https://www.cendana2000.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Hospital',
    'version': '16.0.1',
    'sequence': 10,


    # any module necessary for this one to work correctly
    'depends': [],

    # always loaded
    'data': [
        # 'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],

    'application':True,
    'auto_install': False,
    'license': 'LGPL-3',
}
