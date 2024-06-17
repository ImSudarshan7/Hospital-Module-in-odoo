from odoo import models, fields


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Management'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', required=True)
    phone = fields.Char(string='Phone', required=True)
    address = fields.Char(string='Address', required=True)
    gender = fields.Selection([('male', 'Male'),('female', 'Female')], string='Gender', required=True)
    image = fields.Image(string='Image')
    # description = fields.Text(string='Description')
    is_active = fields.Boolean(string='Active', default=True)
