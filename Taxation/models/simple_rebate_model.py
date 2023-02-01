# -*- coding: utf-8 -*-
from odoo import models,fields,api
from odoo.exceptions import ValidationError as ve        #changing the name of the function for this file only 
class Simple_Rebate_Model(models.Model):
    _name="simple.rebate.model"
    _description="Rebate and Refunds"

# ------------------------------------------------------------------
# Fields in our Model
# ------------------------------------------------------------------
    rebate_section_name=fields.Selection(
        string="Rebate Sections",
        selection=[('80c','Section 80C'),('80gg','Section 80GG'),('80e','Section 80E'),('80ee','Section 80EE'),('80d','Section 80D'),('80dd','Section 80DD'),('80g','Section 80G'),('80ggc','Section 80GGC'),('80ddb','Section 80DDB'),('80u','Section 80U')]
    )
    disablity_level=fields.Selection(
        string="Disablity Level",
        selection=[('40%',"40% to 80%"),('80%','> 80%')]
    )
    amount=fields.Float(required=True)
    document=fields.Binary()
    personal_info_id=fields.Many2one("personal.info.model")

# ------------------------------------------------------------------
# Constraint on amount field for our rebate sections
# ------------------------------------------------------------------
    @api.constrains("amount")
    def check_amount(self):
        for record in self:
            if record.amount <= 0 :
                raise ve("Rebate amount cannot be negative or zero")
                
            if record.rebate_section_name=="80c" and record.amount>150000:
                raise ve("Maximum rebate in this section is 150000")     

            elif record.rebate_section_name=="80gg" and record.amount>60000:
                raise ve("Maximum rebate in this section is 60000")

            elif record.rebate_section_name=="80ee" and record.amount>250000:
                raise ve("Maximum rebate in this section is 250000")
            
            elif record.rebate_section_name=="80d" and record.amount>100000:
                raise ve("Maximum rebate in this section is 100000")
            
            elif record.rebate_section_name=="80dd" and record.disablity_level=='40%' and record.amount>75000:
                raise ve("Maximum rebate in this section is 75000 because your disablity level is 40 to 80%")
        
            elif record.rebate_section_name=="80dd" and record.disablity_level=='80%' and record.amount>125000:
                raise ve("Maximum rebate in this section is 125000 because your disablity is > 80%")

            elif record.rebate_section_name=="80ddb" and record.amount>100000 and record.personal_info_id.age=='seniorcitizen':
                raise ve("Maximum rebate in this section is 100000")
            
            elif record.rebate_section_name=="80ddb" and record.amount>40000 and record.personal_info_id.age=='adult':
                raise ve("Maximum rebate in this section is 100000")

            elif record.rebate_section_name=="80u" and record.amount>125000:
                raise ve("Maximum rebate in this section is 125000")
            
# ------------------------------------------------------------------
# Create method is use to check that no rebate section is repeated  
# ------------------------------------------------------------------   
    @api.model
    def create(self, values):
        rebate_id = self.env['personal.info.model'].browse(values['personal_info_id'])  
        rebate_id.state='crebate_details'
        # print('------------------------------------')
        section_list=rebate_id.mapped('rebate_ids.rebate_section_name')             
        if  values['rebate_section_name'] in section_list:
             raise ve("Rebate Section is Already Selected")                   # ve is our ValidationError
        return super().create(values)         
      