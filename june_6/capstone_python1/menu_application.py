import csv

with open("orders.csv", "r") as file:
    orders = list(csv.DictReader(file))

while True:

    print("\n===== E-Commerce Order Analytics =====")
    print("1. View Orders")
    print("2. Revenue Analysis")
    print("3. Product Analysis")
    print("4. City Analysis")
    print("5. Export Reports")
    print("6. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:

        print("\nAll Orders\n")

        for order in orders:
            print(order)

    elif choice == 2:

        total_revenue = 0
        highest_order = 0
        lowest_order = float("inf")

        for order in orders:

            revenue = (
                int(order["quantity"]) *
                int(order["price"])
            )

            total_revenue += revenue

            if revenue > highest_order:
                highest_order = revenue

            if revenue < lowest_order:
                lowest_order = revenue

        average_order = (
            total_revenue / len(orders)
        )

        print("\nRevenue Analysis")
        print("Total Revenue =", total_revenue)
        print("Highest Order Value =", highest_order)
        print("Lowest Order Value =", lowest_order)
        print("Average Order Value =", average_order)

    elif choice == 3:

        product_quantity = {}

        for order in orders:

            product = order["product"]

            if product in product_quantity:
                product_quantity[product] += int(order["quantity"])
            else:
                product_quantity[product] = int(order["quantity"])

        print("\nProduct Analysis")

        for product, quantity in product_quantity.items():
            print(product, "=", quantity)

    elif choice == 4:

        city_revenue = {}

        for order in orders:

            city = order["city"]

            revenue = (
                int(order["quantity"]) *
                int(order["price"])
            )

            if city in city_revenue:
                city_revenue[city] += revenue
            else:
                city_revenue[city] = revenue

        print("\nCity Analysis")

        for city, revenue in city_revenue.items():
            print(city, "=", revenue)

    elif choice == 5:

        total_revenue = 0

        for order in orders:
            total_revenue += (
                int(order["quantity"]) *
                int(order["price"])
            )

        with open(
            "sales_summary_report.txt",
            "w"
        ) as report:

            report.write(
                f"Total Orders = {len(orders)}\n"
            )

            report.write(
                f"Total Revenue = {total_revenue}\n"
            )

        print("Report Exported Successfully")

    elif choice == 6:

        print("Thank You")
        break

    else:

        print("Invalid Choice")