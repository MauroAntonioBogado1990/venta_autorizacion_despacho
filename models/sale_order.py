# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    #autorizado = fields.Boolean(string='Autorizado', groups='venta_autorizacion_despacho.group_autorizador_ventas')
    autorizado = fields.Boolean(string='Autorizado')
    #Esto en caso de confirmacion
    # def _action_confirm(self):
    #     res = super()._action_confirm()
    #     for order in self:
    #         for picking in order.picking_ids:
    #             picking.autorizado = order.autorizado
    #     return res
    
    #Esto en caso cuando se escribe
    def write(self, vals):
        res = super().write(vals)
        if 'autorizado' in vals:
            for order in self:
                for picking in order.picking_ids:
                    picking.autorizado = vals['autorizado']
        return res