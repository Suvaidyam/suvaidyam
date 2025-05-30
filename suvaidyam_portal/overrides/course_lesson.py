import json
import frappe
from lms.lms.doctype.course_lesson.course_lesson import CourseLesson as LMSCourseLesson

class CourseLesson(LMSCourseLesson):
    def on_update(self):
        self.validate_quiz_id()

    def validate_quiz_id(self):
        if self.content and self.content.strip().startswith("{"):
            try:
                self.save_lesson_details_in_quiz(self.content)
            except json.JSONDecodeError:
                frappe.log_error(f"Invalid JSON content in Course Lesson: {self.content}", "JSON Decode Error")

    def save_lesson_details_in_quiz(self, content):
        content = json.loads(content)
        # your logic here if needed...
