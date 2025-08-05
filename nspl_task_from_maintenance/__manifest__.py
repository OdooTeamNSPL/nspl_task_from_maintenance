{
    "name": " Create Task from Maintenance Request",
    "version": "18.0",
    'summary': """This module streamlines operations by automatically converting maintenance requests into project tasks. It eliminates manual work, enhances team collaboration, and ensures efficient tracking within project workflows.""",
    'description': """
This module streamlines operations by automatically converting maintenance requests into project tasks.

✔ Create tasks automatically when a new maintenance request is logged.
✔ Sync key maintenance request details (e.g., description, date) to the generated task.
✔ Define rules for task creation and specify how requests are converted into tasks.
✔ Efficiently manage and track maintenance tasks from within the Project module.
Perfect for HR managers and teams who want to manage employee data more efficiently.

    """,
    'category': 'Project',
    'sequence': 2,
    'author': 'Namah Softech Private Limited',
    'website': 'http://namahsoftech.com/',
    'license': 'OPL-1',
    'price': 29.99,
    'currency': 'USD',
    'support': 'support@namahsoftech.com',
    'contributors': ["Rutik Patil"],
    'depends': ['base', 'maintenance', 'project', 'mail'],

    "data": [
        "security/ir.model.access.csv",
        "views/maintenance_create_task.xml",
        "views/create_task_wizard_form.xml",
    ],
    'images': ['static/description/img/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,

}
