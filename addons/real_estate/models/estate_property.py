from odoo import models, fields
from datetime import date, timedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    
    date_availability = fields.Date(
        string="Available From",
        default=lambda self: date.today() + timedelta(days=90),  # Default in 3 months
        copy=False  # Do not copy when duplicating
    )
    
    expected_price = fields.Float(string="Expected Price")
    
    selling_price = fields.Float(
        string="Selling Price",
        readonly=True,  # Read-only
        copy=False      # Do not copy when duplicating
    )
    
    bedrooms = fields.Integer(
        string="Bedrooms",
        default=2  # Default number of bedrooms
    )
    
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area (sqm)")
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], string="Garden Orientation")
    
    state = fields.Selection([
    ('new', 'New'),
    ('offer_received', 'Offer Received'),
    ('offer_accepted', 'Offer Accepted'),
    ('sold', 'Sold'),
    ('cancelled', 'Cancelled')
], string='Status',
   required=True,
   default='new',
   copy=False
)
