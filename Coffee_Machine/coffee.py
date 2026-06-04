report={
    "water":300,
    "milk":200,
    "coffee":100,
    "money":0
}

menu={
    "espresso":{
        "water":50,
        "coffee":18,
        "cost":1.5
    },
    "cappuccino":{
        "water":250,
        "milk":100,
        "coffee":24,
        "cost":3.0
    },
    "latte":{
        "water":200,
        "milk":150,
        "coffee":24,
        "cost":2.5
    }
}

def espresso():
    quarter=int(input("Enter the no of QUARTER: "))
    quarter=0.25*quarter
    dime=int(input("Enter the no of DIME: "))
    dime=0.10*dime
    nickel=int(input("Enter the no of NICKEL: "))
    nickel=0.05*nickel
    penny=int(input("Enter the no of PENNY: "))
    penny=0.01*penny

    total_price=quarter+dime+nickel+penny

    if total_price>=menu["espresso"]["cost"] and report["water"]>=menu["espresso"]["water"] and report["coffee"]>=menu["espresso"]["coffee"]:
        print("Here is your espresso. Enjoy!")
        total_price-=menu["espresso"]["cost"]
        print(f"There is ${round(total_price,2)} change!")
        report["water"]-=50
        report["coffee"]-=18
        report["money"]+=1.5

    elif total_price<menu["espresso"]["cost"] and report["water"]<menu["espresso"]["water"] and report["coffee"]<menu["espresso"]["coffee"]:
        print("Not enough money and ingredients")

    elif total_price<menu["espresso"]["cost"]:
        print("There is not enough money.")

    else:
        print("Not enough ingredient")


def latte():
    quarter=int(input("Enter the no of QUARTER: "))
    quarter=0.25*quarter
    dime=int(input("Enter the no of DIME: "))
    dime=0.10*dime
    nickel=int(input("Enter the no of NICKEL: "))
    nickel=0.05*nickel
    penny=int(input("Enter the no of PENNY: "))
    penny=0.01*penny

    total_price=quarter+dime+nickel+penny

    if total_price>=menu["latte"]["cost"] and report["water"]>=menu["latte"]["water"] and report["coffee"]>=menu["latte"]["coffee"] and report["milk"]>=menu["latte"]["milk"]:
        print("Here is your latte. Enjoy!")
        total_price-=menu["latte"]["cost"]
        print(f"There is ${round(total_price,2)} change!")

        report["water"]-=200
        report["coffee"]-=24
        report["milk"]-=150
        report["money"]+=2.5

    elif total_price<menu["latte"]["cost"] and report["water"]<menu["latte"]["water"] and report["coffee"]<menu["latte"]["coffee"] and report["milk"]<menu["latte"]["milk"]:
        print("Not enough money and ingredients")

    elif total_price<menu["latte"]["cost"]:
        print("There is not enough money.")

    else:
        print("Not enough ingredient")


def cappuccino():
    quarter=int(input("Enter the no of QUARTER: "))
    quarter=0.25*quarter
    dime=int(input("Enter the no of DIME: "))
    dime=0.10*dime
    nickel=int(input("Enter the no of NICKEL: "))
    nickel=0.05*nickel
    penny=int(input("Enter the no of PENNY: "))
    penny=0.01*penny

    total_price=quarter+dime+nickel+penny

    if total_price>=menu["cappuccino"]["cost"] and report["water"]>=menu["cappuccino"]["water"] and report["coffee"]>=menu["cappuccino"]["coffee"] and report["milk"]>=menu["cappuccino"]["milk"]:
        print("Here is your cappuccino. Enjoy!")
        total_price-=menu["cappuccino"]["cost"]
        print(f"There is ${round(total_price,2)} change!")

        report["water"]-=250
        report["coffee"]-=24
        report["milk"]-=100
        report["money"]+=3.0

    elif total_price<menu["cappuccino"]["cost"] and report["water"]<menu["cappuccino"]["water"] and report["coffee"]<menu["cappuccino"]["coffee"] and report["milk"]<menu["cappuccino"]["milk"]:
        print("Not enough money and ingredients")

    elif total_price<menu["cappuccino"]["cost"]:
        print("There is not enough money.")

    else:
        print("Not enough ingredient")


coff1=True

while coff1 is True:
    coffee=input("What would you like? (espresso/latte/cappuccino): ")

    if coffee=="espresso":
        espresso()

    elif coffee=="cappuccino":
        cappuccino()

    elif coffee=="latte":
        latte()

    elif coffee=="report":
        for key in report:
            print(f"{key}: {report[key]}")

    elif coffee=="off":
        coff1=False
        print("Coffee machine turned off.")

    else:
        print("Invalid option.")