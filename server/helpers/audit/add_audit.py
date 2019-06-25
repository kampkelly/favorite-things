from api.audit.models import Audit as AuditModel


class AddAudit:

    @staticmethod
    def add_audit(message, user):
        audit = AuditModel(log=message, user_id=user['id'])
        audit.save()
