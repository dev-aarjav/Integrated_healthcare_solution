# -*- coding: utf-8 -*-
{
    'name': "Hospital Management System",

    'summary': "Integrated Healthcare Solution ,a web based platform to manage all the health care solution",

    'description': """
    An Integrated Healthcare Solution is a unified system that connects various healthcare services, departments, and technologies into a single platform to deliver coordinated, patient-centered care. It ensures that patient data, clinical workflows, billing, and administrative processes are all interconnected and accessible across the organization.

🔗 Key Components:
Electronic Health Records (EHR/EMR) – Centralized patient medical history and clinical data

Appointment & Scheduling System – Manages doctor availability and patient bookings

Lab & Diagnostic Integration – Real-time test orders, results, and imaging access

Pharmacy Management – Prescription handling and medicine inventory

Billing & Insurance – Automated invoicing, insurance claims, and payments

Telemedicine – Virtual consultations and remote patient monitoring

Patient Portal – Self-service access to reports, appointments, and communication

Reporting & Analytics – Clinical, financial, and operational insights for decision-making


    """,

    'author': "Aarjav",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','product',],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
        'views/patient_tag_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'application':True,
}

