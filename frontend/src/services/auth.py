import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def register_user(student_name, email, mobile, password, confirm_password, aadhar_no):
    try:
        if password != confirm_password:
            return {"error": "Passwords do not match."}

        user = frappe.get_doc({
            "doctype": "Student",
            "first_name": student_name,
            "student_email_id": email,
            "student_mobile_number": mobile,
            "custom_password": password,
            "custom_aadhar_no": aadhar_no,
            
        })

        user.insert(ignore_permissions=True, ignore_mandatory=True)
        frappe.db.commit()

        return {"message": "User registered successfully"}

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "User Registration Failed")
        return {"error": str(e)}
