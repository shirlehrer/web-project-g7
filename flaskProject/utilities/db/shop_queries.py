from flaskProject.utilities.db.db_manager import dbManager
from flaskProject.utilities.db.user_queries import UserManager


class ShopManager:

    # the function searches products that fit the input search
    def getProducts(p_name: str):
        query_result = dbManager.fetch('SELECT * FROM products WHERE p_name=%s', p_name)
        return query_result

    def checkCartExists(email):
        order = dbManager.fetch("SELECT order_id FROM orders WHERE email='%s' AND finished=0" % email)
        if len(order) == 0:  # there is no open order (current cart)
            return False
        print(order[0].order_id)
        return order[0].order_id  # there is an open order for the user

    def createNewCart(user_name, datetime):
        user_email = UserManager.getUserEmail(user_name)
        dbManager.commit("INSERT INTO orders (email, date) VALUES ('%s', '%s')" % (user_email, datetime.now()))
        order_id = dbManager.fetch("SELECT order_id FROM orders WHERE email='%s' AND finished=0" % user_email)
        return order_id

    def insertProductsToOrders(p_name, order_id, quantity):
        dbManager.commit("INSERT INTO products_in_order (p_name,order_id, quantity) VALUES ('%s', '%s', '%s')"
                         % (p_name, order_id, quantity))
        return True

        # the function checks if the product is already in the user's current order (cart)
    def checkProductInOrder(user_name, p_name):
        user_email = UserManager.getUserEmail(user_name)
        if len(user_email) == 0:
            return False ## cant make an order if not a user
        exits = ShopManager.checkCartExists(user_email[0].email)
        if not exits:  # there is no open order (current cart)
            return False
        else:
            query_result = dbManager.fetch(
                    "SELECT p_name FROM products_in_order WHERE p_name='%s' AND order_id='%s'" % (p_name, exits))
            if len(query_result) > 0:
                return True
        return False

    def removeProductsFromOrder(user_name, p_name):
        email = UserManager.getUserEmail(user_name)
        order_id = ShopManager.checkCartExists(email[0].email)
        dbManager.commit("DELETE FROM products_in_order WHERE p_name='%s' AND order_id='%s'" % (p_name, order_id))
        return True


    def updateProductQuantity(p_name, updated_quantity, order_id):
        dbManager.commit("UPDATE products_in_order SET quantity='%s' WHERE p_name='%s' AND order_id='%s'" % (
            p_name, order_id, updated_quantity))
        return True

    @staticmethod
    def getOrdersproducts(email):
        return dbManager.fetch("SELECT * FROM products_in_order as po JOIN orders as o WHERE o.email='%s' "
                               "and po.order_id=o.order_id" % email)




    # def createPayment(first_name, last_name, amount, email, phoneNum, datetime, CC, CVV, expirationDate):
    #
    #     query_result = dbManager.commit(
    #         "update orders set first_name='%s', last_name='%s', amount='%s', email='%s', phoneNum='%s', datetime='%s', CC='%s', CVV='%s', expirationDate='%s' where email='%s' and finished='False'" %
    #         (first_name, last_name, amount, email, phoneNum, datetime, CC, CVV, expirationDate))
    #     return query_result

        # we use in "payment"
        # the function insert new order details
        # @staticmethod
        # def updatePayment(pay_name, pay_last_name, pay_ID, cash, serial_number, email_for_bill, pay_phone, amount,
        #                   email):
        #     print('in DBBBBBBBBBBBBBBBBBBBB')
        #     if cash == '0':
        #         dbManager.commit(
        #             "UPDATE orders SET pay_name='%s', pay_last_name='%s', pay_ID='%s', cash='%s', serial_number='%s', email_for_bill='%s' , pay_phone='%s', amount='%s' WHERE email='%s' AND submitted = 0" % (
        #                 pay_name, pay_last_name, pay_ID, cash, serial_number, email_for_bill, pay_phone, amount, email))
        #     else:
        #         print('מזומן')
        #         dbManager.commit(
        #             "UPDATE orders SET pay_name='%s', pay_last_name='%s', pay_ID='%s', cash='%s', email_for_bill='%s' , pay_phone='%s', amount='%s' WHERE email='%s' AND submitted = 0" % (
        #                 pay_name, pay_last_name, pay_ID, cash, email_for_bill, pay_phone, amount, email))
        #     dbManager.commit("UPDATE orders SET submitted = 1 WHERE email='%s'" % email)
        #     return True
