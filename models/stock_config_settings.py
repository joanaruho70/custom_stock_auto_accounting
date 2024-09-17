from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    auto_accounting = fields.Boolean(
        string='Enable Automatic Accounting for Stock',
        config_parameter='custom_stock_auto_accounting.auto_accounting',
    )
