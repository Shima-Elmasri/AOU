from odoo import api, fields, models, _


class IdeasIdeas(models.Model):
    _name = 'ideas.ideas'
    _description = "Student idea"

    proposal_id = fields.Many2one(comodel_name='proposal.proposal', string='Proposal')

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description", required=True)
    initial_type = fields.Selection([
        ('Systems', 'Systems Development '),
        ('mobile_apps', 'Mobile Apps Development'),
        ('hardware', 'Hardware '),
        ('business', 'Business-Related Projects '),
    ], string='Initial Type')

    active = fields.Boolean('Active', default=True)

    state = fields.Selection(selection=[
        ('initial', 'Initial'),
        ('waiting', 'Waiting'),
        ('accepted', 'Accepted'),
        ('proposal', 'Proposal submitted'),
        ('rejected', 'Rejected'),
    ], string='Status',
        default='initial', tracking=True, index=True)

    count_proposal = fields.Integer(compute='_count_proposal', string="Make Proposal")



    def submit(self):
        self.state = 'waiting'

    def accept(self):
        self.state = 'accepted'

    def reject(self):
        self.state = 'rejected'

    @api.model
    def _count_proposal(self):
        for rec in self:
            rec.count_proposal = self.env['proposal.proposal'].search_count([('name', '=', rec.id)])

    def action_view_proposal(self):

        self.ensure_one()

        return {
            'name': 'proposal',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'self',
            'res_model': 'proposal.proposal',
            'res_id': self.id,
            'context': {'proposal_proposal_form_wiz': 'edit', 'force_detailed_view': 'true'}
            }

