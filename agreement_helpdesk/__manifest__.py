# Copyright (C) 2019 - TODAY, Open Source Integrators
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Helpdesk ticket to an agreement",
    "summary": "Link a helpdesk ticket to an agreement",
    "version": "12.0.1.0.0",
    "license": "LGPL-3",
    "author": "Open Source Integrators",
    "category": "Helpdesk",
    "website": "https://github.com/ursais/osi-addons",
    "depends": [
        "helpdesk",
        "agreement_legal",
    ],
    "data": [
        "views/helpdesk_ticket_view.xml",
        "views/agreement_view.xml",
    ],
    "installable": True,
}
