print("Hello World!")

name = input("What is your name? ").strip().title()

print(f"Nice to meet you, {name}!") 

while True:
    try:
        hours = int(input("How many hours do you game? "))
        break
    except ValueError:
        print("Please enter a valid number, dork! ")

if hours > 7:
    print(f"Wow {hours}?! That's more than an hour a day, Nerd! ")
    
elif hours ==7:
    print(f"Wow so an hour a day, I guess that's aight! Mediocre! ")
    
else:
    print(f"{hours}?! {hours}?!?!?!?! That's it?!? Step it up loser! Sheesh ")


    
