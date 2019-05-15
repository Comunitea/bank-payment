# -*- coding: utf-8 -*-
# © 2019 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import models, api


class PurchaseLineInvoice(models.TransientModel):

    _inherit = 'purchase.order.line_invoice'
    _description = 'Purchase Order Line Make Invoice'

    @api.model
    def _make_invoice_by_partner(self, partner, orders, lines_ids):
        res = super(PurchaseLineInvoice, self)._make_invoice_by_partner(
            partner, orders, lines_ids)
        invoice = self.env['account.invoice'].browse(res)
        invoice.payment_mode_id = partner.supplier_payment_mode.id
        return res
