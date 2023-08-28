// Copyright (c) 2022, Tech Station and contributors
// For license information, please see license.txt

frappe.ui.form.on('Installment Request', {
	refresh: function(frm) {
		frm.set_query("installment_payment_method", function() {
			return {
				"filters": {
					"enabled": 1,
					"installment": 1
				}
			};
		});
	
	},
	applicant_type: function(frm) {
		frm.set_value('applicant',"");
		frm.set_value('applicant_name',"");
	},
	applicant: function(frm) {
		if(frm.doc.applicant_type == "Customer"){
			frappe.db.get_value("Customer", frm.doc.applicant, 'customer_name', (r) => {
				frm.set_value('applicant_name',r.customer_name);
			});
		}
		else{
			frappe.db.get_value("Lead", frm.doc.applicant, 'lead_name', (r) => {
				frm.set_value('applicant_name',r.lead_name);
			});
		}
	},
	installment_payment_method: function(frm) {
		if(frm.doc.installment_payment_method){
			frappe.model.with_doc("Mode of Payment", frm.doc.installment_payment_method, function() {
				var mop = frappe.model.get_doc("Mode of Payment", frm.doc.installment_payment_method);
					frm.clear_table("installment_offer");
					frm.refresh_field("installment_offer");
					$.each(mop.installment_offer, function(index, row){
						var d = frm.add_child("installment_offer");
						d.installment_period = row.installment_period;
						d.interest_ratio = row.interest_ratio;
						d.advance_payment = row.advance_payment;
						d.advance_payment_type = row.advance_payment_type;
						d.offer_expiry_date = row.offer_expiry_date;
					});	
					frm.refresh_field("installment_offer");
			});

			frappe.call({
				"method": "customize_account.customize_account.doctype.installment_request.installment_request.get_installment_period",
				args: {
					installment_payment_method: frm.doc.installment_payment_method
				},
				callback:function(r){
					frm.set_value('installment_plan',r.message);
				}
			});
		}
	}
});

frappe.ui.form.on("Installment Request Item", {
	"qty": function(frm, cdt, cdn) {
		var d = locals[cdt][cdn];
		frappe.model.set_value(d.doctype, d.name, "amount", (d.qty * d.rate));
	},
	"rate": function(frm, cdt, cdn) {
		var d = locals[cdt][cdn];
		frappe.model.set_value(d.doctype, d.name, "amount", (d.qty * d.rate));
	}
});