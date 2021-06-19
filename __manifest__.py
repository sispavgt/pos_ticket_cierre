# -*- coding: utf-8 -*-


{
    'name': 'Pos ticket cierre',
    'version': '1.0',
    'category': 'Hidden',
    'sequence': 6,
    'summary': 'Cierre de sesion en ticket',
    'description': """

""",
    'depends': ['point_of_sale'],
    'data': [
        # 'views/res_users_view.xml',
        'data/paperformat_ticket.xml',
        'views/reporte_cierre.xml',
        'views/report.xml',
    ],
    'installable': True,
    'auto_install': False,
}
