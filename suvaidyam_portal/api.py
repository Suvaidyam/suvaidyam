import frappe

def sync_course_to_lms(doc, method):
    if not frappe.db.exists("LMS Course", {"course_title": doc.course_name}):
        frappe.get_doc({
            "doctype": "LMS Course",
            "course_title": doc.course_name,
            "title": doc.course_name,
            "route": f"/courses/{frappe.scrub(doc.course_name)}",
            "published": 1,

            # ✅ Mandatory Fields
            "short_introduction": "This is a short intro to the course.",
            "description": doc.get("description") or "Detailed course description goes here.",

            # ✅ Instructors (example entry with logged-in user)
            "instructors": [
                {
                    "instructor": frappe.session.user  # or replace with a valid Instructor ID
                }
            ]
        }).insert(ignore_permissions=True, ignore_mandatory=True)
