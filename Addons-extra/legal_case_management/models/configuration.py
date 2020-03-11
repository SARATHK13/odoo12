from odoo import models, fields, api
from datetime import datetime

class FeeTypes(models.Model):
    _name = 'fee.types'

    fee_name = fields.Char(string="Fee Name")
    fee_amount = fields.Float(string="Fee Amount")


class UniversityType(models.Model):
    _name = 'university.type'
    _rec_name = 'university_name'

    university_name = fields.Char(string="University Name")
    year = fields.Date(string="Year of Graduation")


class ServiceTypes(models.Model):
    _name = 'lawyer.master'

    lawyer_name = fields.Many2one('hr.employee', string="Lawyer Name")
    lawyer_val = fields.Many2one('hr.contract')
    month_salary = fields.Char(compute="total_salary", string="Total Salary")
    state = fields.Selection([('request', 'Request'), ('paid', 'Approved')], default='request')

    # @api.multi
    # @api.depends('lawyer_val.name', 'lawyer_val.employee_id')
    # def total_salary(self):
    #     for record in self:
    #         if record.

    @api.multi
    def action_paid(self):
        payslip = self.env['hr.payslip'].create({
            'employee_id': self.lawyer_name.id,
            'date_from': datetime.now(),
            'date_to': datetime.now(),
        })
        self.state = 'paid'
        return payslip


class MatterTypes(models.Model):
    _name = 'matter.type'
    _rec_name = 'matter_name'

    matter_section = fields.Char(string="Section no")
    matter_name = fields.Char(string="Matter Name")
    matter_amount = fields.Char(string="Amount")



