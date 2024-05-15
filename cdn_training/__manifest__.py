# -*- coding: utf-8 -*-
{
    'name': "training_odoo16",

    'summary': """
        membuat modul training odoo16""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Cnedana 2000",
    'website': "https://www.cendana2000.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '16.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'product', 'purchase','l10n_id_efaktur'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'data/sequence_data.xml',
        'views/menu_training.xml',
        'views/training_course.xml',
        'views/instruktur.xml',
        'views/training_session.xml',
        'views/propinsi.xml',
        'views/kota.xml',
        'views/kecamatan.xml',
        'views/desa.xml',
        'views/peserta.xml',
        'wizards/training_wizard.xml',
        'views/jabatan.xml',
        'wizards/jabatan_wizard.xml',
        'views/product_inherit.xml',
        'views/purchase_order_inherit.xml',
        'views/jenis_kelamin_inherit.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True,
    'license': 'LGPL-3',
}
