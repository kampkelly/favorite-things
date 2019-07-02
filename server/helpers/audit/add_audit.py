from api.models import Audit as AuditModel
from dataclasses import dataclass, field


@dataclass(order=True)
class AddAudit:
    message: str
    user: dict = field(repr=False, compare=False)
    """
    A class to add audit logs to the audit table
    """
    def add_audit(self):
        """
        A method to save the user logs

        Args:
            message (str): The message to save as the log
            user (object): The user to attach the log to
        """
        audit = AuditModel(log=self.message, user_id=self.user['id'])
        audit.save()
