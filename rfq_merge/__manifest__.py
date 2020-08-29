# -*- coding: utf-8 -*-
{
    'name': 'Merge Purchase Orders',
    'version': '13.0.1.0',
    'category': 'Proof of Concept',
    'summary': "Cancel existing RFQ's to make a merged new one.",
    'description': u"""
This module has been generated by Odoo Studio.
It contains the apps created with Studio and the customizations of existing apps.
""",
    'author': 'Odoo Technical Marketing',
    'depends': [
        'purchase',
        'stock',
        'sale_management',
        'web_studio',
    ],
    'data': [
        'data/ir_actions_server.xml',
    ],
    'application': False,
    'license': 'OPL-1',
    'support': 'Unsupported',
    'images': [
        'images/main_screenshot.png'
    ],
}
