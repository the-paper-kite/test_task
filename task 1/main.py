from technic import Technic

camera = Technic(name="Camera", price=55000, availability=True)
phone = Technic(name="Phone", price=46000, availability=True)
camera.display_technic
phone.display_technic
Technic.__ge__(camera.name, phone.name)

