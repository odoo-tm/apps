# -*- coding: utf-8 -*-
{
    'name': 'Manufacturing Timesheets',
    'version': '13.0.0.9',
    'category': 'Proof of Concept',
    'summary': 'Studio App: Timesheets Tab on Manufacturing Orders. Post Costs via Journal Entry',
    'description': u"""
This module has been generated by Odoo Studio.
It contains the apps created with Studio and the customizations of existing apps.
""",
    'author': 'Odoo Technical Marketing',
    'depends': [
        'account_accountant',
        'mrp',
        'hr_timesheet',
        'web_studio',
    ],
    'data': [
        'data/account_analytic_account.xml',
        'data/ir_model_fields.xml',
        'data/ir_ui_view.xml',
        'data/ir_actions_server.xml',
        'data/base_automation.xml',
    ],
    'application': False,
    'license': 'OPL-1',
    'support': 'Unsupported',
    'images': [
        'images/main_screenshot.png'
    ],
}
