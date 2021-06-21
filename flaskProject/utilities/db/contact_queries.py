from flaskProject.utilities.db.db_manager import dbManager
from datetime import datetime


class ContactManager:

    @staticmethod
    def addContactReq(first_name, last_name, email, message):
        query_result = dbManager.commit(
            "insert into contact_massages(first_name, last_name, email, message) VALUES ('%s', '%s', '%s', '%s')" %
            (first_name, last_name, email, message))
        return query_result

    @staticmethod
    def addAppointment(fullName, phone, email, message, date):
        query_result = dbManager.commit(
            "insert into contact_massages(fullName, phone, email, message, date) VALUES ('%s', '%s', '%s', '%s', '%s')" %
            (fullName, phone, email, message, date))
        return query_result

    @staticmethod
    def getApps(email):
        return dbManager.fetch("SELECT * FROM appointments WHERE email='%s'" % email)

