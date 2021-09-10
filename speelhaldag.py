AmountPeople = 3
TimeGameSeat = 45

PriceTicket = 7.45
PriceGameSeat = 0.37 #per 5 min

TotalPrice = (AmountPeople * PriceTicket + TimeGameSeat / 5 * PriceGameSeat * AmountPeople)
print(TotalPrice)
