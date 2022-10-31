# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, api, _


class Students(models.Model):
    _inherit = 'res.users'

    # student_user
    student_id = fields.Char(string="Student ID")
    student_track = fields.Selection([
        ('info_tec', 'Information Technology and Computing'),
        ('computerScience', 'Computer Science'),
        ('computing_business', 'Computing with Business'),
        ('network_security', 'Network and Security'),
        ('web_development', 'Web Development'),

    ],
        string='Student Track', required=True, )
    section_id = fields.Many2one('section.section')

    # doctor user
    doctor_id = fields.Char(string="Doctor ID")
    sections_ids = fields.One2many('section.section', 'doctor_id')

    # user type
    user_type_project = fields.Selection([
        ('doctor', 'Doctor'),
        ('student', 'Student')
    ], string="Info Type",  default='doctor', required=True)


class Section(models.Model):
    _name = 'section.section'

    name = fields.Char(string="Section")
    student_ids = fields.One2many('res.users', 'section_id', string="Enrolled students:",
                                  domain=lambda self: [
                                      ('groups_id', 'in', self.env.ref('final_year.group_consort_student').id)])
    doctor_id = fields.Many2one('res.users', string="Doctor:", domain=lambda self: [
        ('groups_id', 'in', self.env.ref('final_year.module_consort_doctor').id)])
