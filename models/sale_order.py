from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    laser_entries = fields.Char(string='Número de entradas del láser')
    dimension_length = fields.Float(string='Longitud', help='Longitud (con desperdicios de pieza)')
    dimension_width = fields.Float(string='Anchura', help='Anchura (con desperdicios de pieza)')
    dimension_height = fields.Float(string='Altura', help='Altura (con desperdicios de pieza)')