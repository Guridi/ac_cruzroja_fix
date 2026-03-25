# -*- coding: utf-8 -*-
{
    'name': 'Cruz Roja Dominicana - Personalización de Reportes',
    'version': '17.0.1.0.0',
    'summary': 'Personalización de reportes de facturas, compras y ventas para Cruz Roja',
    'description': """
        Personalización de Reportes Cruz Roja Dominicana
        =================================================
        
        Este módulo personaliza los reportes de Odoo para Cruz Roja Dominicana:
        
        * Elimina espacios en blanco entre header y información de cliente/proveedor
        * Agrega fecha de orden y referencia del partner en el encabezado
        * Muestra ITBIS y retenciones debajo del total
        
        Aplica a: Facturas, Órdenes de Compra y Órdenes de Venta
    """,
    'author': 'Antonio Guridi',
    'category': 'Accounting/Accounting',
    'license': 'LGPL-3',
    'depends': [
        'account',
        'sale',
        'purchase',
    ],
    'data': [
        'report/invoice_report.xml',
        'report/purchase_report.xml',
        'report/sale_report.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
