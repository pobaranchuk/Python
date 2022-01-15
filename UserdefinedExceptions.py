#Customizing User-defined Exceptions

class InventoryError(Exception):
  def __init__(self, supply):
    self.supply = supply
  def __str__(self):
    return 'Available supply is only ' + str(self.supply)
   
inventory = {
  'Piano': 3,
  'Lute': 1,
  'Sitar': 2
}

def submit_order(instrument, quantity):
  supply = inventory[instrument]

  if quantity > supply:
    raise InventoryError(supply)
  else:
    inventory[instrument] -= quantity
    print('Successfully placed order! Remaining supply: ' + str(inventory[instrument]))

submit_order("Piano", 5)

