# -*- coding: utf-8 -*-
from odoo import models, fields

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    autorizado = fields.Boolean(string='Autorizado por ventas')