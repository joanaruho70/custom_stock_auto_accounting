from odoo import models, api

class StockMove(models.Model):
    _inherit = 'stock.move'

    @api.model
    def _create_account_move_line(self, move, qty, description):
        config = self.env['ir.config_parameter'].sudo().get_param('custom_stock_auto_accounting.auto_accounting')
        if config:
            move_obj = self.env['account.move']
            journal_id = self.env['account.journal'].search([('type', '=', 'general')], limit=1)

            # Define the debit and credit accounts for the stock move
            debit_account = move.product_id.categ_id.property_stock_account_input_categ_id
            credit_account = move.product_id.categ_id.property_stock_account_output_categ_id

            if not debit_account or not credit_account:
                return

            # Create the accounting entries for the stock move
            move_lines = [(0, 0, {
                'name': description,
                'account_id': debit_account.id,
                'debit': move.product_uom_qty * move.price_unit,
                'credit': 0.0,
            }), (0, 0, {
                'name': description,
                'account_id': credit_account.id,
                'debit': 0.0,
                'credit': move.product_uom_qty * move.price_unit,
            })]

            # Create the accounting move
            move_obj.create({
                'journal_id': journal_id.id,
                'line_ids': move_lines,
                'ref': move.reference,
            })

    @api.model
    def create(self, vals):
        res = super(StockMove, self).create(vals)
        config = self.env['ir.config_parameter'].sudo().get_param('custom_stock_auto_accounting.auto_accounting')
        if config and res.location_id.usage == 'internal' and res.location_dest_id.usage == 'internal':
            self._create_account_move_line(res, res.product_uom_qty, res.name)
        return res
