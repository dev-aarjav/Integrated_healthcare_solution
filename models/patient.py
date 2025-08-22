# -*- coding: utf-8 -*-
from datetime import date
from odoo import models, fields, api


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient"

    name = fields.Char(string="Name",tracking=True)
    date_of_birth=fields.Date(string='Date of Birth')
   
    
    age=fields.Integer(string="Age",compute='_compute_age',tracking=True)
    gender=fields.Selection([('male','Male'),('female','Female')],string="Gender",tracking=True)
    ref=fields.Char(string='Reference',default='Odoo Mates')
    
    active = fields.Boolean(
        string='Active',default=True
    )
    appointment_id = fields.Many2one(comodel_name='hospital.appointment', string="Appointments")
    
    tag_ids = fields.Many2many(
        string='Tags',
        comodel_name='patient.tag'
    )
    
    
    @api.depends('date_of_birth')
    def _compute_age(self):
        print("self.......",self)
        for rec in self:
            today=date.today()
            if rec.date_of_birth:
                rec.age=today.year-rec.date_of_birth.year
            else:
                rec.age=0
