# -*- coding: utf-8 -*-
# © <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Account Invoice Button Refund",
    "summary": "Account Invoice Button Refund invisible in state = paid",
    "version": "9.0.1.0.0",
    "category": "Personalized",
    "website": "https://odoo-community.org/",
    "author": "<Samuel Barron>, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "base", "account",
    ],
    "data": [
        "views/account_invoice.xml"
    ],
    "demo": [
    ],
    "qweb": [
    ]
}
