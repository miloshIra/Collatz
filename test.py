import datetime
import os
import csv

user = None

def get_user():
    return input("Enter User :")


def gun_read():
    barcode1 = input("Please read the first barcode!?")
    print(barcode1)
    barcode2 = input("Plese read the secdon barcode?!")
    print(barcode2)
    today=datetime.datetime.now()
    if barcode1 == barcode2:
        print("GREEN LIGHT!!")
        with open('log.csv', 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            export_tup1 = (user,barcode1,barcode2,str(today.strftime('%d-%m-%y')),str(today.strftime('%H:%M')),'Tochno')
            csv_writer.writerow(export_tup1)
        return True
    else:
        print("you fcked up broooo!!")
        with open('log.csv', 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            export_tup2 = (user,barcode1,barcode2,str(today.strftime('%d %m %y')),str(today.strftime('%H:%M')),'Ne tochno')
            csv_writer.writerow(export_tup2)
        return False


def main():
    global user  # so we can write to the global user variable
    user = get_user()  # grab the username and write it
    while True:  # repeat gun reads until the end of time
        gun_read()


if __name__ == "__main__":
    main()
