# -*- coding: utf-8 -*-
from odoo import models,fields,api
from odoo.exceptions import ValidationError as ve        #changing the name of the function for this file only 
class Simple_Rebate_Model(models.Model):
    _name="simple.rebate.model"
    _description="Rebate and Refunds"

    rebate_section_name=fields.Selection(
        string="Rebate Sections",
        selection=[('80c','Section 80C'),('80gg','Section 80GG'),('80e','Section 80E'),('80ee','Section 80EE'),('80d','Section 80D'),('80dd','Section 80DD'),('80g','Section 80G'),('80ggc','Section 80GGC'),('80ddb','Section 80DDB'),('80u','Section 80U')]
    )
    amount=fields.Float(required=True)
    personal_info_id=fields.Many2one("personal.info.model")

    @api.constrains("amount")
    def check_amount(self):
        for record in self:
            if record.rebate_section_name=="80c" and record.amount>150000:
                raise ve("Maximum rebate in this section is 150000")     

            elif record.rebate_section_name=="80gg" and record.amount>60000:
                raise ve("Maximum rebate in this section is 60000")

            elif record.rebate_section_name=="80ee" and record.amount>250000:
                raise ve("Maximum rebate in this section is 250000")
            
            elif record.rebate_section_name=="80d" and record.amount>100000:
                raise ve("Maximum rebate in this section is 100000")
            
            elif record.rebate_section_name=="80dd" and record.amount>125000:
                raise ve("Maximum rebate in this section is 125000")
            
            elif record.rebate_section_name=="80ddb" and record.amount>100000:
                raise ve("Maximum rebate in this section is 100000")
            
            elif record.rebate_section_name=="80u" and record.amount>125000:
                raise ve("Maximum rebate in this section is 125000")
            
    
    # @api.model
    # def create(self, vals):
    #     # property_id = self.env['personal.info.model'].browse(vals['personal_info_id']
    #         print('*************88')
    #         domain=[rebate_section_name,'=',vals['rebate_section_name']]
    #         result= self.env['simple.rebate.model'].search([domain])
    #         print(result)
    # #         # if result  == ['rebate_section_name']:
    #             #     return result
    #             # else:
    #             #  return False                      
    # #         return super().create(vals)      
    # #     # print(vals['rebate_section_name'])s
    #     # property_id = self.env['personal.info.model'].browse(values['personal_info_id'])
    #    # printt('------------------------------------')
    #     # print(property_id.read())

    #     # print("--------------------------------")
    #     # print([property_id.rebate_ids.rebate_section_name.read()])
    #     # if values['rebate_section_name'] == property_id.rebate_ids.rebate_section_name: 
    #     #     raise UserError("Nai chale bhai aavu")
        
        
    #     # print(values['property_id'])
        
        # property_id.state = 'offer_received'
    

    @api.model
    def create(self, values):
        property_id = self.env['personal.info.model'].browse(values['personal_info_id'])  
        print('------------------------------------')
        section_list=property_id.mapped('rebate_ids.rebate_section_name')             
        if  values['rebate_section_name'] in section_list:
             raise ve("Rebate Section is Already Selected")
        return super().create(values)         
      