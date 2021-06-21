from flaskProject.utilities.db.db_manager import dbManager


class UserManager:

    # the function insert new user details
    def insertNewUser(first_name, last_name, user_name, email, password):
        dbManager.commit("INSERT INTO users(first_name, last_name, user_name, email, password) "
                         "VALUES ('%s', '%s', '%s', '%s', '%s')"
                         % (first_name, last_name, user_name, email, password))
        return True

    # the function checks if the email already exists in users table
    def checkIfUserExists(email):
        query_result = dbManager.fetch("SELECT * FROM users where email='%s'" % email)
        if len(query_result) == 0:
            return False
        return True

    @staticmethod
    def updateUser(first_name, last_name, user_name, password, email):
        query_result = dbManager.commit(
            'update users set  first_Name=%s, last_Name=%s, user_name=%s, password=%s where email=%s',
            (first_name, last_name, user_name, password, email))
        return query_result

    def getUserEmail(user_name):
        return dbManager.fetch("SELECT email FROM users WHERE user_name='%s'" % user_name)

    def getUsernamePass(email):
        return dbManager.fetch("SELECT user_name, password FROM users WHERE email='%s'" % email)

    def getUser(email):
        return dbManager.fetch("SELECT * FROM users WHERE email='%s'" % email)



