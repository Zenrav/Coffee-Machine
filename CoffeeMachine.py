MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 100,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 130,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit=0
check=True

def coffee_maker():
    global coffee_type
    coffee_type={}
    global coffee_resource
    coffee_resource={}
    if user_input=='espresso':
        coffee_type=MENU['espresso']
    if user_input=='latte':
        coffee_type=MENU['latte']
    if user_input=='cappuccino':
        coffee_type=MENU['cappuccino']
    coffee_resource=coffee_type['ingredients']
    for i in coffee_resource:
        if coffee_resource[i]>resources[i]:
            print('Sorry! There is not enough',i)
            return False
    return True

def bill():
    profit=coffee_type['cost']
    print('Bill: ',profit)    
    hundred_note=int(input('Enter number of 100Rs notes: '))
    fifty_note=int(input('Enter number of 50Rs notes: '))
    ten_note=int(input('Enter number of 10Rs notes: '))
    total_money=(hundred_note)*100+(fifty_note)*50+(ten_note)*10
    if total_money< profit:
        print('Not Sufficient Money. Coffee Cannot be made.')
    else:
        refund=total_money-profit
        print('Your Change: Rs',refund)
        print('Here is your ',user_input,'!')
        for i in coffee_resource:
            resources[i]-=coffee_resource[i]
             

while check==True:
    user_input=input('What would you like to have (espresso/latte/cappuccino) : ')
    if user_input=='off':
        print('GoodBye!')
        check=False
    elif user_input=='Report':
        print('Water: ',resources['water'],'ml')
        print('Milk: ',resources['milk'],'ml')
        print('Coffee: ',resources['coffee'],'g')
    else:
        if coffee_maker():
            bill()
        