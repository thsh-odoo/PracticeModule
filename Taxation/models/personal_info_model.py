# -*- coding: utf-8 -*-
from odoo import fields,models,api
from odoo.exceptions import ValidationError
class personal_info(models.Model):

    _name="personal.info.model"
    _description="personal information and "
    _inherit = ['mail.thread', 'mail.activity.mixin']
# ------------------------------------------------------------------
# Fields in our Model
# ------------------------------------------------------------------   
    name=fields.Char(required=True,default="unknown")
    age=fields.Selection(
        string='Age Group',
        selection=[('adult','Adult(18-59)'),('seniorcitizen','Senior Citizen( age>=60)')
        ],
        required=True
    )
    contact_details=fields.Char(required=True)
    total_income=fields.Monetary(required=True)
    currency_id = fields.Many2one(comodel_name='res.currency')
    tax_slab_id=fields.Many2one("tax.slab.model",required=True)
    expense_ids=fields.One2many("expenditure.model","info_id")
    
    company_id = fields.Many2one('res.company', store=True, copy=False,
                                string="Company",
                                default=lambda self: self.env.user.company_id.id)

    currency_id = fields.Many2one('res.currency', string="Currency",
                                 related='company_id.currency_id',
                                 default=lambda
                                 self: self.env.user.company_id.currency_id.id)
    
    income_tax=fields.Monetary(readonly=True,compute="_income_tax")
    rebate_ids=fields.One2many("simple.rebate.model","personal_info_id")

# ------------------------------------------------------------------
# Compute Method to calculate our Income Tax
# ------------------------------------------------------------------
    @api.depends("expense_ids.cost","total_income","rebate_ids.amount")
    def _income_tax(self):
        for record in self:
            tax=0
            if record.tax_slab_id.name=='New':             # Income Tax Calculation According to New regim
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

            elif record.tax_slab_id.name=="Old":                 # Income Tax Calulation According to old Regim
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
                
            print("------------------------",tax)    
            if Taxable_amount >= 5000000 and Taxable_amount <= 10000000:            #Surcharge Calculation 
                tax=tax+(tax*0.10)    
                
            elif Taxable_amount >10000000 and Taxable_amount <= 20000000:
                tax=tax+(tax*0.15)

            elif Taxable_amount > 20000000 and Taxable_amount <= 50000000:
                tax=tax+(tax*0.25)

            elif Taxable_amount > 50000000 : #and Taxable_amount <= 50000000:
                tax=tax+(tax*0.37)
            
            record.income_tax=(tax+tax*0.04)             #Health And Educational Cess

# ------------------------------------------------------------------
# Python Constraint to validate our contact details field
# ------------------------------------------------------------------
    @api.constrains("contact_details")
    def _check_contact(self):
        for record in self:
            length=len(record.contact_details)
            
            if length > 10 or record.contact_details.isnumeric() == False:
                raise ValidationError("Invalid Contact Details")