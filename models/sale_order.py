# -*- coding: utf-8 -*-
from odoo import models, fields, api, _, exceptions


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    autorizado = fields.Boolean(string='Autorizado')
    can_authorize = fields.Boolean(
        string='Can Authorize',
        compute='_compute_can_authorize',
        store=False,
    )

    def _compute_can_authorize(self):
        can = self.env.user.has_group('venta_autorizacion_despacho.group_autorizador_ventas')
        for rec in self:
            rec.can_authorize = can

    @api.model
    def create(self, vals):
        # Prevent unauthorized users from setting 'autorizado' on create
        if 'autorizado' in vals and not self.env.user.has_group('venta_autorizacion_despacho.group_autorizador_ventas'):
            raise exceptions.AccessError(_("Su grupo no puede modificar el campo 'Autorizado'."))
        return super(SaleOrder, self).create(vals)

    def write(self, vals):
        # Prevent unauthorized users from changing 'autorizado'
        if 'autorizado' in vals and not self.env.user.has_group('venta_autorizacion_despacho.group_autorizador_ventas'):
            raise exceptions.AccessError(_("Su grupo no puede modificar el campo 'Autorizado'."))
        res = super(SaleOrder, self).write(vals)
        if 'autorizado' in vals:
            for order in self:
                for picking in order.picking_ids:
                    picking.autorizado = vals['autorizado']
        return res