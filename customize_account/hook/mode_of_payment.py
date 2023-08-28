# -*- coding: utf-8 -*-
# Copyright (c) 2020, Tech Station and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _, throw
from frappe.model.document import Document

def validate(self,method):
	if self.is_public == 0 and len(self.accessibility) == 0:
		frappe.throw(_("Please add minimum 1 user in <b>Accessibility</b> table as you have kept this payment method as private"))