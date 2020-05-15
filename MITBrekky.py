def main():
    print(30*"_ ")
    print("\tWelcome  to the MIT Brekky! Resturant")
    print(30*"_ ")
    print('''Please choose your item.\n\n 1. Small Breakfast Deal,    ($10)\n 2. Regular Breakfast Deal,  ($20)\n 3. Big Breakfast Deal,      ($30)\n\n Or select individual food and beverage items:\n\n +  4. Egg                   ($0.99 each),\n +  5. Mix fruit salad       ($2.5 per box),\n +  6. sausage               ($3.5 each),\n +  7. hash brown            ($1.19 each),\n +  8. toast                 ($0.79 per slice),\n +  9. coffee                ($1.09 per cup),\n + 10. tea                   ($0.89 per tea bag)\n''')
    print("Enter '000' to quit. Enter '111' to finalize for payment.")
    #item dic
    items = {'1':10,'2':20,'3':30,'4':0.99,'5':2.5,'6':3.5,'7':1.19,'8':0.79,'9':1.09,'10':0.89}
    temptotal =0
    #calculate total
    def totcal():
        tax=round(temptotal * 0.13, 2)
        total=temptotal + tax   
        print(30*"_", "\n\nUsing total + tax to print recipt.")
        print("Cost    : $ " + str(temptotal))
        print("Tax     : $ " + str(tax))
        print("Total   : $ "+str(total),
                "\nProcess finished. Enjoy!")
        print(30*"_ ")      
    #get order
    while(True):
        user_input = input('item :')
        if (user_input.isnumeric()):
            if (int(user_input) <= 10 or int(user_input)== 111):
                user_input=int(user_input)
                if user_input == 111:
                    totcal()
                    break
                elif int(user_input) in range(1,11):
                    quntity = input('Quntity:')
                    if quntity.isnumeric():
                        temptotal = temptotal+(int(items[str(user_input)])*int(quntity))
                    else:
                        print("Enter a valid input agian!")
                elif (user_input==000):
                    print("Quitting !!")
                    break
                else:
                    print("Enter a valid input agian!")
            else:
                print("Enter a valid input agian!")
        else:
            print("Enter a valid input agian!")

main()
                    