from odoo import models, fields, api, _
from odoo.exceptions import UserError


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    task_id = fields.Many2one('project.task', string='Related Task')
    task_count = fields.Integer(string='Task Count', compute='_compute_task_count')

    def _compute_task_count(self):
        for rec in self:
            rec.task_count = self.env['project.task'].search_count([('maintenance_id', '=', rec.id)])

    def action_open_quick_edit_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Create Task'),
            'view_mode': 'form',
            'res_model': 'maintenance.request.wizard',
            'target': 'new',
            'context': {'active_id': self.id},
        }

    def action_view_task(self):
        self.ensure_one()
        tasks = self.env['project.task'].search([('maintenance_id', '=', self.id)])
        if not tasks:
            raise UserError(_("No tasks linked to this maintenance request."))
        if len(tasks) == 1:
            return {
                'type': 'ir.actions.act_window',
                'name': _('Task'),
                'res_model': 'project.task',
                'res_id': tasks.id,
                'view_mode': 'form',
                'target': 'current',
            }
        else:
            return {
                'type': 'ir.actions.act_window',
                'name': _('Tasks'),
                'res_model': 'project.task',
                'domain': [('maintenance_id', '=', self.id)],
                'view_mode': 'list,form',
                'target': 'current',
            }


class ProjectTask(models.Model):
    _inherit = 'project.task'

    maintenance_id = fields.Many2one('maintenance.request', string='Maintenance Request')
