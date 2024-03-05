money=0
while True :
    flag=int(input("please enter number:(1-variz 2-bardasht 3-moojoodi)"))
    if flag==1:
        mablagh=float(input("mablagh varizi ra vared konid:"))
        money+=mablagh
        print(f"mablagh {mablagh} variz shod")
    elif flag==2:
        mablagh=float(input("mablagh bardashti ra vared koniid:"))
        if money>=mablagh:
            money-=mablagh
            print(f"mablagh {mablagh} az hesab shoma bardashte shod")
        else:
            print("moojoodi hesab shoma kafi nist")
    elif flag==3:
        print(f"moojoodi hesab shoma {money}")
    else:
        print("opperation invalid")
    cheak=input("do you want continue?(yes/no):")
    if cheak=='no':
        break                       