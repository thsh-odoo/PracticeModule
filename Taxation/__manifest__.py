# -*- coding: utf-8 -*-
{
    'name' : 'Taxation',
    'category' : 'Sales',
    'summary' : 'Tax calculation',
    'description' : 'This app will help you to calculate your income tax',
    'version' : '1.0',
    'author' : 'THSH',
    'data' : [ 
        'security/ir.model.access.csv',
        'views/Personal_info_view.xml',
        'views/tax_slab_view.xml',
        'views/expenditure_view.xml',
        'views/simple_rebate_view.xml',
        'views/Taxation_menu.xml'
        ],
    'demo' : [ 
        'demo/tax_slab_demo.xml'
        ],
    'depends' : [   
      ],
    'installable' : True,
    'application' : True,
    'auto_install' : False
}