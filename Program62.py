
CB = 10000

while True:
    WA = int(input("Enter a Withdraw Amount:"))

    if WA <= CB:
          CB = CB-WA
          print("Transcation sucessful...")
          print("Current Balance:",CB)
    else:
        print("Insufficient Balance...")
        print("Current Balance:",CB)
        break

