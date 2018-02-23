# a=0.1
# b=0.2
# print(type(a))
# print(type(b))
# print(round(a+b,2))
import  decimal
# import  the  libray  "decimal"
# display  2  decimal  precision
print (round (3.1415 ,   2))   #  result  3. 14
print (round (9.995 ,   2))   #  result  9. 99

#call   function   "Decimal "  from lib "decimal"
print (decimal.Decimal (9.995))
# The last "print" returns
# 9.9949999999999992184029906638897955417633056640625,
# which is exactly how 9.995 is stored in the hardware.