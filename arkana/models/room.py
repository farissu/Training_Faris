# -*- coding: utf-8 -*-

from odoo import models, fields 


class room(models.Model):
    _name = 'arkana.faris_room'  
    _description = 'room'
    _rec_name = 'nama_ruangan'
    

    image_ruangan = fields.Binary('Image Ruangan')
    nama_ruangan = fields.Char('Nama Ruangan' , required=True )