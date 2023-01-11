# -*- coding: utf-8 -*-

from odoo import fields,models
class Tax_Slab_Model(models.Model):
    _name='tax.slab.model'
    _description='tax slabs'
    
    tax_slab_critaria=fields.Char()
  

