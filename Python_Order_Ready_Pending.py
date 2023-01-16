# Written by Emin Ayyıldız
print("Written by Emin Ayyıldız")

import time

orders = []
ready_orders = []


def check_admin_credentials(username, password):
    if username == "admin" and password == "1234":
        print("Logging into account, please wait...")
        time.sleep(1.5)
        print("Login to the system.")
        return True
    elif username == "cafe" and password == "0000":
        print("Logging into account, please wait...")
        time.sleep(1.5)
        print("Login to the system.")
        return True
    elif username == "q" or username == "Q" or password == "Q" or password == "q":
        print("The system has been logged out.")
        quit()
    else:
        print("Wrong username or password...")
        return False

while True:
    print("Welcome to restaurant system. We wish you a nice day..")
    username = input("Please enter username :")
    password = input("Please enter password : ")
    if check_admin_credentials(username, password):
        while True:

            table_number = input("\nPlease enter table number : ")

            if any(item["table_number"] == table_number and item["status"] == "pending" for item in orders):
                print("This table is already waiting for an order...")
                continue
            elif any(item["table_number"] == table_number and item["status"] == "ready" for item in ready_orders):
                ready_orders = [order for order in ready_orders if order["table_number"] != table_number]
            if table_number == "q" or table_number == "Q":
                print("Exiting...")
                time.sleep(1.5)
                print("BYE BYE :)) ")
                break
            if len(table_number) < 1:
                pass
            else:
                order_details = input("Please enter order details : ")
                pay_method = input("Select payment method \n1-CREDIT CARD \n2-PAYPAL \n3-CASH \n-----> ")
                if pay_method == "1":
                    card_number = input("Enter your 16 digit card number : ")
                    card_password = input("Enter your 4 digit card password  : ")
                    if len(card_number) >= 15 and len(card_password) == 4:
                        print("Payment is progress, please wait...")
                        time.sleep(1.5)
                        print("Credit card payment processed.")

                        orders.append({"table_number": table_number, "order_details": order_details, "status": "pending"})
                        print("The order has been confirmed.")
                    else:
                        print("Invalid card number...")
                elif pay_method == "2":
                    paypal_card_number = input("Enter your 16 digit card number : ")
                    paypal_card_password = input("Enter your 4 digit card password  : ")
                    if len(paypal_card_number) >= 15 and len(paypal_card_password) == 4:
                        if len(paypal_card_number) >= 15 and len(paypal_card_password) == 4:
                            print("Payment is progress, please wait...")
                            time.sleep(1.5)
                            print("Paypal payment processed.")
                            orders.append({"table_number": table_number, "order_details": order_details, "status": "pending"})
                            print("The order has been confirmed.")
                        else:
                            print("Invalid card number...")
                elif pay_method == "3":
                    print("Cash payment processed.")
                    orders.append({"table_number": table_number, "order_details": order_details, "status": "pending"})
                    print("The order has been confirmed.")
                else:
                    print("Invalid payment method.")

            update_order = input("Enter the ready order number : ")
            if update_order == "q" or update_order == "Q":
                print("Exiting...")
                time.sleep(1.5)
                print("BYE BYE :)) ")
                break
            if update_order:
                if update_order in [order["table_number"] for order in orders]:
                    for order in orders:
                        if order["table_number"] == update_order:
                            order["status"] = "ready"
                            ready_orders.append(order)
                            orders.remove(order)
            print("\nPending orders:")
            for order in orders:
                print("Orders Number : ", order["table_number"], "  Orders Details : ", order["order_details"])

            print("\nReady orders:")
            for order in ready_orders:
                print("Orders Number : ", order["table_number"], "  Orders Details : ", order["order_details"])
