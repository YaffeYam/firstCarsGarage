from icecream import ic

carsGarage=[]

def main ():
    while (True):
        ic("A - Add a car")
        ic("P - Print cars array")
        ic("X - Exit")
        user_selection = input("Your selection: ")

        if user_selection == 'a':carsGarage.append('red')
        if user_selection == 'p':ic(carsGarage)
        if user_selection == 'x':exit()

if __name__ == '__main__':
    main()