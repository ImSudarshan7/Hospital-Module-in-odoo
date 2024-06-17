from odoo import models, fields


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Management'

    name = fields.Char(string='Name', required=True)
    specialization = fields.Char(string='Specialization')
    phone = fields.Char(string='Phone Number', required=True)
    email = fields.Char(string='Email')
    address = fields.Char(string='Address', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', required=True)
    is_active = fields.Boolean(string='Active', default=True)

