from features.admin_management import add_admin, remove_admin
from features.link_protection import protect_link
from features.file_system.expiration import set_file_expiry

def handle_admin(update, context):
    action = context.args[0] if context.args else None
    if action == "add":
        add_admin(update, context)
    elif action == "remove":
        remove_admin(update, context)

def protect_link(update, context):
    # Implementation moved to link_protection.py
    pass

def set_expiry(update, context):
    set_file_expiry(update, context)
