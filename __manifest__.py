# -*- coding: utf-8 -*-
################################################################################
#
#    Kolpolok Ltd. (https://www.kolpolok.com)
#    Author: Kaushik Ahmed Apu, Zarin Tasnim, Aqil Mahmud(<https://www.kolpolok.com>)
#
################################################################################

{
    'name': 'Stock Automatic Accounting',
    'version': '1.0',
    'summary': 'Enable automatic accounting entries for stock movements in Odoo Community',
    'depends': ['stock', 'account'],
    'data': [
      'views/stock_config_settings_view.xml',  # Add your custom XML file here
    ],
    'installable': True,
    'auto_install': False,
}

