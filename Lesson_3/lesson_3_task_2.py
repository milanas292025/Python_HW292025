from smartphone import Smartphone

catalog = [
    Smartphone("Sam", "D21", "+79002718265"),
    Smartphone("Sam", "E22", "+79002718264"),
    Smartphone("Sam", "I23", "+79002718263"),
    Smartphone("Sam", "Y24", "+79002718262"),
    Smartphone("Sam", "F25", "+79002718261")
]

for smartphone in catalog:
    print(f"{smartphone.phone_brand} - {smartphone.phone_model}"        
          f"- {smartphone.subscription_number}")




