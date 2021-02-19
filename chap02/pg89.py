#3.4
Guests = ['MGK', 'Chester Bennington', 'Lil Peep', 'Yungblud']
for Guest in Guests:
    print(f"\n\tDear {Guest}, You have been invited to my birthday dinner on the 13th of June 2021.\n\tPlease arrive fashionably late and with a lot of money in hand. Thank you {Guest}")

#3.5
not_coming = 'Chester Bennington'
print(f"\n\t{not_coming} will unfortunately not be joining our dinner")
Guests.remove(not_coming)
new_Guest = 'Ariana Grande'
Guests.append(new_Guest)
for Guest in Guests:
    print(f"\n\tDear {Guest}, You have been invited to my birthday dinner on the 13th of June 2021.\n\tPlease arrive fashionably late and with a lot of money in hand. Thank you {Guest}")
#3.6
print('\n\tHi all, I have found a bigger table so I will be inviting more people so stay tuned.')
Guests.insert(0, 'Alex')
Guests.insert(2, 'Sarah')
Guests.insert(6, 'Mia')
for Guest in Guests:
    print(f"\n\tDear {Guest}, You have been invited to my birthday dinner on the 13th of June 2021.\n\tPlease arrive fashionably late and with a lot of money in hand. Thank you {Guest}")

#3.9
length = len(Guests)
print(length)    

#3.7
print('\n\t Hello everyone...unfortunately we are unable to secure a big table so I will only be able to invite two people')
removed = Guests.pop(0)
print(f"\n\tHi {removed}, unfortunately you have been univited")
removed = Guests.pop(1)
print(f"\n\tHi {removed}, unfortunately you have been univited")
removed = Guests.pop(2)
print(f"\n\tHi {removed}, unfortunately you have been univited")
removed = Guests.pop(3)
print(f"\n\tHi {removed}, unfortunately you have been univited")
removed = Guests.pop(4)
print(f"\n\tHi {removed}, unfortunately you have been univited")
for Guest in Guests:
    print(f"\n\tHi {Guest}, You are still invited.")
    Guests.remove(Guest)

    #3.9
length = len(Guests)
print(length)
 
