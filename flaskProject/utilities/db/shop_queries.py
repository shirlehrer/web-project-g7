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

        # the function checks if the product is already in the user's current order (cart)

    def checkProductInCart(p_name, user_name):
        query_result = dbManager.fetch(
                "SELECT p_name FROM cart WHERE p_name='%s' AND user_name='%s'" % (p_name, user_name))
        if len(query_result) > 0:
            return True
        return False

    @staticmethod
    def getOrdersproducts(email):
        return dbManager.fetch("SELECT * FROM orders WHERE email='%s'" % email)

    def insertProductsToOrders(p_name, quantity):
        query1 = dbManager.fetch("SELECT * FROM orders")
        order_id = len(query1) + 1
        dbManager.commit("INSERT INTO products_in_order (p_name,order_id, quantity) VALUES ('%s', '%s', '%s')"
                     % (p_name, order_id, quantity))
        return True

    def insertCart(p_name, user_name, quantity):
        price = dbManager.fetch("SELECT price FROM products WHERE p_name='%s'" % p_name)[0][0]
        dbManager.commit("INSERT INTO cart (p_name, user_name, quantity, price) VALUES ('%s', '%s', '%s', '%s')"
                     % (p_name, user_name, quantity, int(price)))
        return True

    def createNewOrder(user_name, first_name, last_name, email, cc, cvv):
        amount = ShopManager.calculateAmount(user_name)
        query1 = dbManager.fetch("SELECT * FROM orders")
        order_id = 1
        if len(query1) > 0:
            order_id = len(query1) + 1
        dbManager.commit("INSERT INTO orders (order_id, first_name, last_name, email, cc, cvv , amount) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (order_id, first_name, last_name, email, cc, cvv, amount))
        return order_id

    def getCart(user_name):
        return dbManager.fetch("SELECT * FROM cart WHERE user_name='%s'" % user_name)

    def updateProductQuantity(p_name, user_name, quantity):
        dbManager.commit("UPDATE cart SET quantity='%s' WHERE p_name='%s' AND user_name='%s'" % (
            quantity, p_name, user_name))
        return True

    def moveFromCartToOrder(user_name, order_id):
        cart = dbManager.fetch("SELECT * FROM cart WHERE user_name='%s'" % user_name)
        for c in cart:
            dbManager.commit("INSERT INTO products_in_order (p_name,order_id, quantity, price) VALUES ('%s', '%s', '%s', '%s')"
                     % (c.p_name, order_id, c.quantity, c.price))
        return True

    def calculateAmount(user_name):
        return dbManager.fetch("SELECT SUM(price*quantity) as orderTotal FROM cart WHERE user_name='%s'" % user_name)[0][0]


    def deleteCart(user_name):
        return dbManager.commit("DELETE FROM cart WHERE user_name='%s'" % ( user_name))

    def removeProductsFromCart(p_name, user_name):
        return dbManager.commit("DELETE FROM cart WHERE p_name='%s' AND user_name='%s'" % (p_name, user_name))
