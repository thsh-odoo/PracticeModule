# -*- coding: utf-8 -*-
from odoo import fields,models
class Expenditure_Model(models.Model):
    _name="expenditure.model"
    _description="All your Expenses"

    expense_name=fields.Char(required=True)
    date=fields.Date(required=True)
    cost=fields.Float(required=True)
    info_id=fields.Many2one("personal.info.model",required=True)
    _sql_constrains=[
        ('check_cost','CHECK(cost>0)','Cost cannot be negative')
    ]

