# -*- coding: utf-8 -*-
from odoo import models,fields,api
class Simple_Rebate_Model(models.Model):
    _name="simple.rebate.model"
    _description="Rebate and Refunds"

    rebate_section_name=fields.Char(readonly=True)
    amount=fields.Float(required=True)
    personal_info_id=fields.Many2one("personal.info.model")

    @api.constraints("amount")
    def check_amount(self):
        pass