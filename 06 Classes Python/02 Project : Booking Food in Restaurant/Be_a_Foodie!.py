#Business Class
class Business:
  #Constructor
  def __init__(self,name,franchises):
      self.name=name
      self.franchises=franchises

  #String Representation
  def __repr__(self):
      return f"Business name is {self.name} and the franchises are {self.franchises}"

#Franchise Class
class Franchise():
  #Constructor
  def __init__(self,address,menus):
      self.address=address
      self.menus=menus

  #String Representation
  def __repr__(self):
      return self.address

  #Checking the entire menu for the time given
  def available_menus(self,time):
      available_list=[]
      for item in self.menus:
          if time >= item.start_time and time<=item.end_time:
              available_list.append(item)
      return available_list
      

#Menu Class   
class Menu:
  #Constructor
  def __init__(self,name,items,start_time,end_time):
      self.name=name
      self.items=items
      self.start_time=start_time
      self.end_time=end_time
  #String Representation
  def __repr__(self):
      return f" {self.name} menu available from {self.start_time}am to {self.end_time-12}pm"

  #Gives the bill of the purchased items
  def calculate_bill(self,purchased_items):
      total=0
      for item in self.items:
          if item in purchased_items:  
              total+=(self.items[item])
      return total

#Brunch Menu
brunch=Menu("brunch",{
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
},11,16)
print(brunch)

#Calculating the bill for brunch with following items only
print(brunch.calculate_bill(['pancakes','home fries','coffee']))

#Early Bird Menu
early_bird=Menu("early_bird",{
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
},15,18)

print(early_bird.calculate_bill(['salumeria plate','mushroom ravioli (vegan)']))

#Dinner Menu
dinner=Menu("dinner",{
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
},17,23)
#Kids Menu
kids=Menu("kids",{
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
},11,21)

#All menus in a list 
menus=[brunch,early_bird,dinner,kids]

#Creating the new Independent Franchises
flagship_store=Franchise("1232 West End Road",menus)
new_installment=Franchise("12 East Mulberry Street",menus)

#Checking for the availability of menu items for the time : 17 which is 5pm
my_time=flagship_store.available_menus(17)

#Creating the first business 
first_business=Business("Basta Fazoolin' with my Heart",[flagship_store,new_installment])

#Creating Client's order: Arepas menu
arepas_menu=Menu("Take a’ Arepa",{
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
},10,20)

#Ccreating Client's order: Arepas Franchise
arepas_place=Franchise("189 Fitzgerald Avenue",[arepas_menu])

#Creating Client's order : Arepas Franchise 
arepas_businees=Business("Take a' Arepa",[arepas_place])
print(arepas_businees.franchises[0].menus[0])
