# -*- coding: utf-8 -*-

from odoo import models, fields 


class Student(models.Model):
    _name = 'arkana.faris_student'  
    _description = 'student'
    _rec_name = 'nama_siswa'
    

    image_siswa = fields.Binary(string="Foto siswa")
    nama_siswa = fields.Char('Nama siswa' , required=True )
    jenis_kelamin = fields.Selection([
        ('L', 'Laki - Laki'),
        ('P', 'Perempuan'),
    ], string='Jenis Kelamin')