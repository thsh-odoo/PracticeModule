# -*- coding: utf-8 -*-

from odoo import fields,models
class Tax_Slab_Model(models.Model):
    _name='tax.slab.model'
    _description='tax slabs'

# ------------------------------------------------------------------
# Field in our Model
# ------------------------------------------------------------------   
    name=fields.Char(required=True,readonly=True)
  