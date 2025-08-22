**Integrated Healthcare Module (Odoo)**
Overview
The Integrated Healthcare module is built on the Odoo framework to streamline hospital and clinic operations.
It provides a comprehensive system to manage patients, doctors, appointments, and medical records with intuitive form views, tree views, and search views.

This module enables healthcare centers to efficiently manage appointments, maintain patient history, and ensure smooth workflows.

Key Features
👤 Patient Management
Create and manage patient records with demographic and medical details.
Track patient history through form and tree views.

📋 Views
Form View – for detailed patient and doctor records.
Tree View – for quick listing of patients, doctors, and appointments.
Search View – for filtering records by date, doctor, patient, or status.

Version-odoo18

Core Models:
patient – Patient details
doctor – Doctor details
appointment – Appointment records
Views Implemented: Form, Tree, Search
Access Rights: Configurable for healthcare staff (doctors, receptionists, administrators).

Installation
Clone this repository into your Odoo addons folder:
git clone <repo-url> integrated_healthcare
Restart your Odoo server:
./odoo-bin -u integrated_healthcare -d <your-database>

Future Enhancements
Prescription and medication management.
Billing and invoicing integration.
Lab test reports.

