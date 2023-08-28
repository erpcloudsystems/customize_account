// Copyright (c) 2020, Tech Station and contributors
// For license information, please see license.txt

frappe.ui.form.on('Mode of Payment', {
	refresh(frm) {
		frm.set_query("cost_center", "accounts", function(doc, cdt, cdn) {
			let d = locals[cdt][cdn];
			return {
				filters: [
					['Cost Center', 'is_group', '=', 0],
                    ['Cost Center', 'company', '=', d.company]
				]
			};
		});
        frm.set_query("default_account", "accounts", function(doc, cdt, cdn) {
			let d = locals[cdt][cdn];
			return {
				filters: [
					['Account', 'account_type', 'in', 'Cash,Bank'],
			        ['Account', 'is_group', '=', 0],
                    ['Account', 'company', '=', d.company]
				]
			};
		});
	},
    is_public(frm) {
		frm.clear_table("accessibility");
        frm.refresh_field("accessibility");
	},
	validate(frm) {
		if(frm.doc.create_payment_entry_on_so == 1 && frm.doc.create_payment_entry_on_delivery == 1){
			frappe.throw(__("<b>Create Payment Entry While Approving Sales Order</b> and <b>Create Payment Entry While Approving Delivery</b> can not be set <b>1</b> together."))
		}
	}
});
