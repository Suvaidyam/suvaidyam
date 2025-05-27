import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def register_student(student_name, email, mobile, password, confirm_password, address):
    try:
        if password != confirm_password:
            return {"error": "Passwords do not match."}

        user = frappe.new_doc("Student")
        user.first_name = student_name
        user.student_email_id= email
        user.student_mobile_number= mobile
        user.custom_password= password
        user.custom_address= address

        user.insert(ignore_permissions=True, ignore_mandatory=True)
        frappe.db.commit()

        return {"message": "User registered successfully"}

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "User Registration Failed")
        return {"error": str(e)}
