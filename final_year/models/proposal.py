from odoo import api, fields, models, _


class Proposal(models.Model):
    _name = 'proposal.proposal'
    _description = "proposal of idea"

    user_id = fields.Many2one('res.users', required=False, default=lambda self: self.env.user)

    name = fields.Many2one('ideas.ideas', string="Idea Title", required=True, readonly=True)
    problem = fields.Text(string="Problem")
    solution = fields.Text(string="Solution")

    type = fields.Selection([
        ('Systems', 'Systems Development '),
        ('mobile_apps', 'Mobile Apps Development'),
        ('hardware', 'Hardware '),
        ('business', 'Business-Related Projects '),
    ], string='Type')
    user_id = fields.Many2one('res.users', required=False, default=lambda self: self.env.user)

    student_name = fields.Char(string="Name", related='user_id.name')
    student_id = fields.Char(string="Student ID", related='user_id.student_id')
    student_track = fields.Selection([
        ('info_tec', 'Information Technology and Computing'),
        ('computerScience', 'Computer Science'),
        ('computing_business', 'Computing with Business'),
        ('network_security', 'Network and Security'),
        ('web_development', 'Web Development'),

    ], related='user_id.student_track')

    checkbox1 = fields.Boolean('Select')
    checkbox2 = fields.Boolean('Select')
    checkbox3 = fields.Boolean('Select')
    note1 = fields.Text("Notes:")
    note2 = fields.Text("Notes:")
    note3 = fields.Text("Notes:")

    state = fields.Selection(selection=[
        ('initial', 'Initial'),
        ('waiting', 'Submitted / Waiting'),
        ('send', 'Send Modification to student'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ], string='Status',
        default='initial', tracking=True, index=True)

    def submit(self):
        self.state = 'waiting'

    def accept(self):
        self.state = 'accepted'

    def send(self):
        self.state = 'send'

    def reject(self):
        self.state = 'rejected'

