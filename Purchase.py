purchase = int(input("Enter the purchase price: "))

if purchase >=5000:
    if  purchase >= 20000:
        print("Gift-1")
    elif 12000 <= purchase <=19999:
        print("Gift-2")
    elif 7000 <= purchase <=11999:
        print("Gift-3")
else:
    if 2000 < purchase <= 3000:
        print("Voucher worth Rs 750")
    elif 1000<=purchase <= 2000:
        print("Voucher worth Rs 500")
    else:
        print("No Voucher or Gift eligible.")
