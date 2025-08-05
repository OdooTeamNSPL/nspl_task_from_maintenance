from odoo import models, fields, api


class MaintenanceRequestWizard(models.TransientModel):
    _name = 'maintenance.request.wizard'
    _description = 'Maintenance Request Wizard'

    name = fields.Char(string='Task Name')
    project_id = fields.Many2one('project.project', string='Project')
    user_ids = fields.Many2many('res.users', string='Assigned Users')
    description = fields.Text(string='Description')
    planned_hours = fields.Float(string='Planned Hours')
    deadline = fields.Date(string='Deadline')
    tag_ids = fields.Many2many('project.tags', string='Tags')

    @api.model
    def default_get(self, fields_list):
        defaults = super().default_get(fields_list)
        active_id = self.env.context.get('active_id')
        if active_id:
            maintenance = self.env['maintenance.request'].browse(active_id)
            defaults['name'] = maintenance.name
        return defaults

    def action_create_task(self):
        self.ensure_one()
        active_id = self.env.context.get('active_id')

        task_vals = {
            'name': self.name,
            'project_id': self.project_id.id,
            'user_ids': [(6, 0, self.user_ids.ids)],
            'description': self.description,
            'allocated_hours': self.planned_hours,
            'date_deadline': self.deadline,
            'tag_ids': [(6, 0, self.tag_ids.ids)],
            'maintenance_id': active_id,
        }
        task = self.env['project.task'].create(task_vals)

        if active_id:
            maintenance = self.env['maintenance.request'].browse(active_id)
            maintenance.task_id = task.id

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'project.task',
            'res_id': task.id,
            'view_mode': 'form',
            'target': 'current',
        }
