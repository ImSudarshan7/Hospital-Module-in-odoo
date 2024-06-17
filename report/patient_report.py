from odoo import models

class PatientXlsxReport(models.AbstractModel):
    _name = 'report.hospital.report_patient_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, patients):
        sheet = workbook.add_worksheet('Patients')
        bold = workbook.add_format({'bold': True})

        sheet.write(0, 0, 'Name', bold)
        sheet.write(0, 1, 'Age', bold)
        sheet.write(0, 2, 'Gender', bold)
        sheet.write(0, 3, 'Phone', bold)
        sheet.write(0, 4, 'Address', bold)

        row = 1
        for patient in patients:
            sheet.write(row, 0, patient.name)
            sheet.write(row, 1, patient.age)
            sheet.write(row, 2, patient.gender)
            sheet.write(row, 3, patient.phone)
            sheet.write(row, 4, patient.address)
            row += 1
