{
    'name': 'Autorización de despacho en ventas',
    'version': '18.0',
    'depends': ['sale', 'stock'],
    'author': 'Mauro Bogado, Exemax',
    'category': 'Sales',
    'description': 'Agrega un check de autorización en ventas que se refleja en la orden de despacho',
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/sale_order_view.xml',
        'views/stock_picking_view.xml',
    ],
    'installable': True,
}
