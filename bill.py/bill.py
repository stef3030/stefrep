Bill_total = float (input ("What was the meal total"))
tip = input ("How was your service?")
if tip == "bad":
    print (1.0*Bill_total)
elif tip == "okay":
     print (1.15*Bill_total)
elif tip == "good":
     print (1.20*Bill_total)
elif tip == "great":
     print (1.25*Bill_total)
