# -*- coding: utf-8 -*-

from odoo import models, fields 


class teacher(models.Model):
    _name = 'arkana.faris_teacher'  
    _description = 'teacher'
    _rec_name = 'nama_guru'
    

    image_guru = fields.Binary(string="Foto Guru")
    nama_guru = fields.Char('Nama Guru' , required=True )
    