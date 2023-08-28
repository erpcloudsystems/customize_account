# Copyright (c) 2022, Tech Station and contributors
# For license information, please see license.txt

import frappe
from frappe import msgprint, throw, _
from frappe.model.document import Document

class InstallmentRequest(Document):
	def on_submit(self):
		if self.status not in ['Cancelled','Rejected','Accepted']:
			throw(_("Status Should be one of <b>(Cancelled / Rejected / Accepted)</b>"))

@frappe.whitelist()
def get_installment_period(installment_payment_method):
	installment_payment_method = frappe.db.sql("""select installment_period from `tabInstallment Offer Table` where 
	parent = %s;""",(installment_payment_method),as_dict = True)

	return installment_payment_method[0].installment_period if installment_payment_method else 0
