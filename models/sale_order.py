# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    autorizado = fields.Boolean(string='Autorizado', groups='venta_autorizacion_despacho.group_autorizador_ventas')

    def _action_confirm(self):
        res = super()._action_confirm()
        for order in self:
            for picking in order.picking_ids:
                picking.autorizado = order.autorizado
        return res