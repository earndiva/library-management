# -*- coding: utf-8 -*-
# Copyright (c) 2021, earn and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class LibraryMembership(Document):
	def before_submit(self):
		exists = frappe.db.exitsts(
			"Library Membership",
			{
			"library_member" : self.library.member,
			"docstatus": 1,
			"to_date": (">", self.from_date),
			},	
		)
		if exists:
			frappe.throw("There is an active membership for this member")

		loan_period = frappe.db.get.single.value("Library Settings", "loan_period")
		self.to_date = frappe.utils.add_days(self.from_date, loan_period or 30)

