# -*- coding: utf-8 -*-
from odoo import fields,models,api
import numpy as np
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
    income_tax=fields.Float(readonly=True,compute="_income_tax")
    rebate_ids=fields.One2many("simple.rebate.model","personal_info_id")


    @api.depends("expense_ids.cost","total_income","rebate_ids.amount")
    def _income_tax(self):
        for record in self:
            tax=0
            if record.tax_slab_id.name=='New':   
                if record.total_income >= 0 and record.total_income <= 250000:
                    record.income_tax=0

                else:
                    deduction=sum(record.rebate_ids.mapped("amount"),sum(record.expense_ids.mapped('cost')))
                    Taxable_amount=record.total_income-deduction
                    
                    if Taxable_amount >250000 and Taxable_amount<=500000:
                        tax=(Taxable_amount-250000)*0.05

                    elif Taxable_amount >500000 and Taxable_amount <=750000:
                        tax=12500+((Taxable_amount-500000)*0.1)

                    elif Taxable_amount >750000 and Taxable_amount <=1000000:
                        tax=37500+((Taxable_amount-750000)*0.15)

                    elif Taxable_amount > 1000000 and Taxable_amount <=1250000:
                        tax=75000+((Taxable_amount-1000000)*0.2)

                    elif Taxable_amount >1250000 and Taxable_amount <=1500000:
                        tax=125000+((Taxable_amount-1250000)*0.25)

                    elif Taxable_amount>1500000:
                        tax=187500+((Taxable_amount-1500000)*0.3)

            elif record.tax_slab_id.name=="Old":
                if record.age=='adult':
                    if record.total_income >= 0  and record.total_income <=250000 :
                        record.income_tax=0
                    else:
                        deduction=sum(record.rebate_ids.mapped("amount"))+sum(record.expense_ids.mapped('cost'))
                        Taxable_amount=record.total_income-deduction
                        if Taxable_amount > 250000 and Taxable_amount <= 500000:
                            tax=(Taxable_amount-250000)*0.05

                        elif Taxable_amount >500000 and Taxable_amount <=1000000:
                            tax=12500+((Taxable_amount-500000)*0.2)
                        
                        elif Taxable_amount>1000000:
                            tax=112500+((Taxable_amount-1000000)*0.3)
                
                elif record.age=='seniorcitizen':
                    if record.total_income >= 0  and record.total_income <=300000 :
                        record.income_tax=0
                    else:
                        deduction=sum(record.rebate_ids.mapped("amount"))+sum(record.expense_ids.mapped('cost'))
                        Taxable_amount=record.total_income-deduction

                        if Taxable_amount > 300000 and Taxable_amount <= 500000:
                            tax=(Taxable_amount-250000)*0.05

                        elif Taxable_amount >500000 and Taxable_amount <=1000000:
                            tax=10500+((Taxable_amount-500000)*0.2)
                        
                        elif Taxable_amount>1000000:
                            tax=110000+((Taxable_amount-1000000)*0.3)

        record.income_tax=(tax+tax*0.04)

    # @api.constrains("rebate_ids")
    # def _unique_tax_rebate(self):
    #     for record in self:
    #         print(record.rebate_ids.amount)
    #         print(record.rebate_ids.mapped('rebate_section_name'))