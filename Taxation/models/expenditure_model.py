# -*- coding: utf-8 -*-
from odoo import fields,models,api
from odoo.exceptions import ValidationError
from datetime import date
class Expenditure_Model(models.Model):
    _name="expenditure.model"
    _description="All your Expenses"

# ------------------------------------------------------------------
# Fields in our Model
# ------------------------------------------------------------------
    expense_name=fields.Char(required=True)
    date=fields.Date(required=True)
    cost=fields.Float(required=True)
    info_id=fields.Many2one("personal.info.model",required=True)
    _sql_constrains=[
        ('check_cost','CHECK(cost>0)','Cost cannot be negative')
    ]

# ------------------------------------------------------------------
# Python Constrains to check our data
# ------------------------------------------------------------------
    @api.constrains("date")
    def _check_year(self):
        for record in self:
            if record.date > date.today():
                raise ValidationError("Date is not Acceptable")
            
