from odoo import models, fields

class RealEstateProperty(models.Model):
    _name = "real.estate.property"
    _description = "Real estate property"

    name = fields.Char(required=True)
    description = fields.Text()
    price = fields.Float()
    active = fields.Boolean(default=True)
    state = fields.Selection([
        ('available','Available'),
        ('sold','Sold'),
        ('rented','Rented')
    ], default='available')
    partner_id = fields.Many2one('res.partner', string="Owner")
