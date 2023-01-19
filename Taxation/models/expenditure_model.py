# -*- coding: utf-8 -*-
from odoo import fields,models,api
from odoo.exceptions import ValidationError
from datetime import date
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


    @api.constrains("date")
    def _check_year(self):
        for record in self:
            year=record.date
            today_year=date.today().year()

            time=today_year - year
            sec=time.total_seconds()
            int_time=sec//1000000
            if int_time < 0 or int_time >365 :
                raise ValidationError("Please enter the valid date")    
            
