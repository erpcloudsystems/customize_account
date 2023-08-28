import frappe
from erpnext.accounts.doctype.mode_of_payment.mode_of_payment import ModeofPayment

class CustomModeofPayment(ModeofPayment):
	def validate_repeating_companies(self):
		pass