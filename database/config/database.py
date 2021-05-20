from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "label": _("Database Console"),
            "icon": "octicon octicon-briefcase",
            "items": [
                {
                    "type": "page",
                    "name": "database_console",
                    "label": _("Database Console"),
                    "onboard": 1
                },
            ]
        }
    ]