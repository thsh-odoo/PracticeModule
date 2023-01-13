# -*- coding: utf-8 -*-
from odoo import fields,models,api
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
            if record.total_income > 0 and record.total_income < 250000:
                record.income_tax=0
            else:
                deduction=sum(record.rebate_ids.mapped("amount"))+sum(record.expense_ids.mapped('cost'))
                Taxable_amount=record.total_income-deduction
                while(Taxable_amount>250000):

                    if Taxable_amount < 500000:
                        Tax=(0.05*Taxable_amount)
                        pass
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    elif Taxable_amount < 750000:
                        Tax+=(0.1*Taxable_amount)
                        Taxable_amount-=750000

                    elif Taxable_amount < 1000000:
                        T