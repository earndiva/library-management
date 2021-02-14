# -*- coding: utf-8 -*-
# Copyright (c) 2021, earn and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator

class LibraryMember(WebsiteGenerator):
	def before_save(self):
		self.full_name = f'{self.first_name} {self.last_name or ""}'

	def after_insert(self):
		frappe.msgprint(
			msg='Succestfully create a Library Member',
			title='Nice',
		)
