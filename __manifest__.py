# Copyright (C) 2022-TODAY Serpent Consulting Services Pvt. Ltd. (<http://www.serpentcs.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Hospital Management",
    "version": "15.0.1.0.0",
    "category": "Hospital Management",
    "author": "CRMIC",
    "sequence": -100,
    "website": "",
    "depends": [
        'report_xlsx',
    ],
    "license": "LGPL-3",
    "summary": "Hospital Management to manage patient and doctor in and out  ",
    "demo": [""],
    "data": [
        'views/view_doctor.xml',
        'views/view_patient.xml',
        'views/menu.xml',
        'report/patient_card.xml',
        'report/patient_details.xml',
        'report/report.xml',

    ],
    "assets": {},
    "application": True,
}
