AmountCroissant = 17
AmountStickBread = 2
AmountCoupon = 3

PriceCroissant = 0.39
PriceStickBread = 2.78
CouponWorth = 0.50

TotalPrice = (AmountCroissant * PriceCroissant + AmountStickBread * PriceStickBread - AmountCoupon * CouponWorth)
print("De feestlunch kost je bij de bakker", TotalPrice , "euro voor de", AmountCroissant , "croissantjes en de", AmountStickBread , "stokbroden als de", AmountCoupon , "kortingsbonnen nog geldig zijn!")