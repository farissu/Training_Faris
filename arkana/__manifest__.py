# -*- coding: utf-8 -*-
{
    'name': "traning",

    'summary': """
        Module Training Faris""",

    'description': """
        Manajemen Training Faris
    """,

    'author': "Rizki Faris",
    'website': "",

    'category': 'Education',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/present.views.xml',
        'views/menuitems.views.xml',
        'views/teacher.views.xml',
        'views/room.views.xml',
        'views/student.views.xml',
        'views/download_paper.xml'
    ],

    'installable': True,
    'application': True,
    'auto_install': False

}