# -*- coding: utf-8 -*-
from odoo import fields,models
class personal_info(models.Model):

    _name="personal.info.model"
    _description="personal information and "

    name=fields.Char(required=True,default="unknown")
    age=fields.Selection(
        string='Age Group',
        selection=[('adult','Adult(18-59)'),('seniorcitizen','Senior Citizen( age>=60)')]
    )
    contact_details=fields.Integer()
    total_income=fields.Float(required=True)
    tax_slab_id=fields.Many2one("tax.slab.model")
    expense_ids=fields.One2many("expenditure.model","info_id")
    income_tax=fields.Float(readonly=True)
    rebate_ids=fields.One2many("simple.rebate.model","personal_info_id")
