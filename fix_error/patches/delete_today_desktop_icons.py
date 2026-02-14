import frappe
from frappe.utils import nowdate

def execute():
    today = nowdate()

    # Get all Desktop Icon records created today
    icons = frappe.get_all(
        "Desktop Icon",
        filters={"creation": ["like", f"{today}%"]},
        pluck="name"
    )

    if not icons:
        print("No Desktop Icon records found for today.")
        return

    for icon in icons:
        frappe.delete_doc("Desktop Icon", icon, force=True)

    frappe.db.commit()
    print(f"Deleted {len(icons)} Desktop Icon records created today.")
