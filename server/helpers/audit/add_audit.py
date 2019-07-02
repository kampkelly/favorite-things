from api.audit.models import Audit as AuditModel


class AddAudit:
    """
    A class to add audit logs to the audit table
    """
    @staticmethod
    def add_audit(message, user):
        """
        A method to save the user logs

        Args:
            message (str): The message to save as the log
            user (object): The user to attach the log to
        """
        audit = AuditModel(log=message, user_id=user['id'])
        audit.save()
