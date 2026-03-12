
{
    'name': 'Custom Product Labels',
    'version': '19.0.0.1.0',
    'category': 'Extra Tools',
    'author': 'Ravindu Vibhooshitha',
    'license': 'OPL-1',
    'summary': 'Print custom product labels with barcode | Barcode Product Label',
    'depends': [
        'product',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/product_data.xml',
        'data/print_label_type_data.xml',
        'data/ir_filters_data.xml',
        'report/product_label_reports.xml',
        'report/product_label_templates.xml',
        'wizard/print_product_label_views.xml',
        'views/res_config_settings_views.xml',
        'views/res_users_views.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
