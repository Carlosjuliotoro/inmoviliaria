# -*- coding: utf-8 -*-
{
    'name': "inmoviliaria",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Este es un modulo que permite la implementacion
        de una inmoviliaria con todos sus servicios
    """,

    'author': "Juan Gabriel Carvajal Hernanadez",
    'website': "jgcarvajalh@uqvirtual.edu.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product', 'website_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/inherited_product_template_view.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
}