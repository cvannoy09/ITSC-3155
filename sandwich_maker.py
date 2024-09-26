
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
         for ingredient, amount_needed in ingredients.items():
            if self.machine_resources.get(ingredient, 0) < amount_needed:
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
      sandwich_recipe = self.recipes[sandwich_size]
        ingredients = sandwich_recipe["ingredients"]

        if self.check_resources(ingredients):
          
            for ingredient, amount_needed in ingredients.items():
                self.machine_resources[ingredient] -= amount_needed
            return True  
        else:
            return False 
