test=input("please enter something:")
if test[0]=="[" and test[-1]=="]":
    print(test)
    print(type(list(test)))
else:
      if "." in test:
       try:
        print(test)
        print(type(float(test)))
       except:
          print(type(test))
      else:
       try:
          print(test)
          print(type(int(test)))
       except:
          print(type(test))  