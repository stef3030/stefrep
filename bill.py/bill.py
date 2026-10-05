Bill_total = float (input ("What was the meal total"))
tip = input ("How was your service?")
if tip == "bad":
    input (1.0*Bill_total)
elif tip == "okay":
    input (1.15*Bill_total)
elif tip == "good":
    input (1.20*Bill_total)
elif tip == "great":
    input (1.25*Bill_total)


