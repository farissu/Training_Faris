# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class Present(models.Model):
    _name = 'arkana.faris_present'
    _description = 'present'
    _rec_name = 'tanggal_hari'

    tanggal_hari = fields.Date(string='Tanggal', default=datetime.today(), readonly=True)
    hari = fields.Char(string='Hari', compute='convert_hari', readonly=True)
    guru_id = fields.Many2one('arkana.faris_teacher', string='Guru')
    nama_ruangan_id = fields.Many2one('arkana.faris_room', string='Nama Ruangan')
    pelajaran = fields.Selection([
        ('mtk', 'Matematika'),
        ('indo', 'B. Indonesia'),
        ('ingris', 'B. Ingris'),
        ('ipa', 'IPA'),
        ('ips', 'IPS'),
        ('agama', 'Agama'),
        ('olahraga', 'Olahraga'),
        ('sains', 'Sains')
    ], string='Pelajaran')
    siswa_id = fields.Many2many(string="Siswa", comodel_name="arkana.faris_student")
    kehadiran = fields.Boolean('kehadiran', default=False)
    status = fields.Selection([
        ('rancangan', 'Rancangan'),
        ('selesai', 'Selesai')
        ],default="rancangan")
    @api.depends('tanggal_hari')
    def convert_hari(self):
        hari_list = {
            'Monday': 'Senin',
            'Tuesday': 'Selasa',
            'Wednesday': 'Rabu',
            'Thursday': 'Kamis',
            'Friday': 'Jumat',
            'Saturday': 'Sabtu',
            'Sunday': 'Minggu',
        }
        for record in self:
            if record.tanggal_hari:
                hari = record.tanggal_hari.strftime('%A')
                if hari in hari_list:
                    record.hari = hari_list[hari]

    def hadir(self):
        self.kehadiran = True
        # return self.env.ref('arkana.absen_template_download')._render_qweb_pdf(self)
    
    def rancangan_button(self):
        self.status = 'rancangan'

    def selesai_button(self):
        self.status = 'selesai'