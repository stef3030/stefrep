Bill_total = float (input ("What was the meal total"))
tip = input ("How was your service?")
if tip == "bad":
    input (1.0)
elif tip == "okay":
    input (1.15)
elif tip == "good":
    input (1.20)
elif tip == "great":
    input (1.25)

print ((Bill_total*tip)+Bill_total)
