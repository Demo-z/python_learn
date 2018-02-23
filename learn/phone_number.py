def phone_number():
    number=input("Enter Your number :")
    number=str(number)
    num_len=len(number)
    CN_mobile = [134,135,136,137,138,139,150,151,152,157,158,159,182,183,184,187,188,147,178,1705]
    CN_union = [130,131,132,155,156,185,186,145,176,1709]
    CN_telecom = [133,153,180,181,189,177,1700]
    quduan=number[:3]
    quduan1=number[:4]
    if num_len!=11:
        print("number should be in 11 digits")
    else:
        if int(quduan) in CN_mobile or int(quduan1) in CN_mobile:
            print("CN_mobile")
            print("you number",number)
        elif int(quduan) in CN_union or int(quduan1) in CN_union:
            print("CN_union")
        elif int(quduan) in CN_telecom or int(quduan1) in CN_telecom:
            print("CN_telecom")
        else:
            print("None")
phone_number()