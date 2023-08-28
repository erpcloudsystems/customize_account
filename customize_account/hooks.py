from . import __version__ as app_version

app_name = "customize_account"
app_title = "Customize Account"
app_publisher = "Tech Station"
app_description = "Customisation In Account"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "developers@techstation.com.eg"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/customize_account/css/customize_account.css"
# app_include_js = "/assets/customize_account/js/customize_account.js"

# include js, css files in header of web template
# web_include_css = "/assets/customize_account/css/customize_account.css"
# web_include_js = "/assets/customize_account/js/customize_account.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "customize_account/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views

doctype_js = {
	"Mode of Payment" : "public/js/mode_of_payment.js"
}

# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "customize_account.install.before_install"
# after_install = "customize_account.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "customize_account.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Mode of Payment": {
		"validate": "customize_account.hook.mode_of_payment.validate",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"customize_account.tasks.all"
# 	],
# 	"daily": [
# 		"customize_account.tasks.daily"
# 	],
# 	"hourly": [
# 		"customize_account.tasks.hourly"
# 	],
# 	"weekly": [
# 		"customize_account.tasks.weekly"
# 	]
# 	"monthly": [
# 		"customize_account.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "customize_account.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "customize_account.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "customize_account.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"customize_account.auth.validate"
# ]


fixtures = [
	{
		"doctype": "Custom Field",
		"filters": [
		[
			"name",
			"in",
		[
			"Mode of Payment-create_payment_entry_on_so",
			"Mode of Payment-create_payment_entry_on_delivery",
			"Mode of Payment-enable_for_split_payment",
			"Mode of Payment-payment_recipient",
			"Mode of Payment-column_break_7",
			"Mode of Payment-is_default",
			"Mode of Payment-section_break_9",
			"Mode of Payment-is_public",
			"Mode of Payment-accessibility",
			"Mode of Payment Account-cost_center",
			"Mode of Payment Account-account_name",
			"Mode of Payment Account-fees",
			"Mode of Payment-installment",
			"Mode of Payment-section_break_10",
			"Mode of Payment-installment_type",
			"Mode of Payment-installment_offer",
		]
		]
	]
	},
]

after_migrate = "customize_account.utils.migrate.after_migrate"

override_doctype_class = {
    'Mode of Payment': 'customize_account.override.mode_of_payment.CustomModeofPayment'
}