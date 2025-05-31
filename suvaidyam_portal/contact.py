import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def submit_question(fullName, email, message):
    try:
        user = frappe.new_doc("Incoming queries")
        user.fullname = fullName
        user.email= email
        user.message= message

        user.insert(ignore_permissions=True, ignore_mandatory=True)
        frappe.db.commit()

        return {"message": "Question entered successfully"}

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Question entry Failed")
        return {"error": str(e)}
