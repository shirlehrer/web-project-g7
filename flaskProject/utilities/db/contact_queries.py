from flaskProject.utilities.db.db_manager import dbManager
from datetime import datetime


class ContactManager:

    @staticmethod
    def addContactReq(first_name, last_name, email, massage):
        query_result = dbManager.commit(
            "insert into contact_massages(first_name, last_name, email, massage) VALUES ('%s', '%s', '%s', '%s')" %
            (first_name, last_name, email, massage))
        return query_result

    @staticmethod
    def addAppointment(full_name, phone, email, description, date):
        query2 = dbManager.fetch("SELECT * FROM appointments")
        app_id = len(query2) + 1
        query_result = dbManager.commit(
            "insert into appointments(app_id,full_name, phone, email, description) VALUES ('%s', '%s', '%s', '%s', '%s')" %
            (app_id, full_name, phone, email, description))
        return query_result

    @staticmethod
    def getApps(email):
        return dbManager.fetch("SELECT * FROM appointments WHERE email='%s'" % email)

