class Recipe():
    def __init__():
        pass
    def CreateRecipe(self, inputs, output, name):
        self.inputs = inputs
        self.values = inputs.values()
        self.keys = inputs.keys()
        self.output = {name, output}
        return self
base = Recipe()
ironPlate = Recipe.CreateRecipe(base, {'ironIngot':30}, 30, 'ironPlate')
ironRod = Recipe.CreateRecipe(base, {'ironIngot': 15}, 15, 'ironRod')
screws = Recipe.CreateRecipe(base, {'ironRod': 10}, 40, 'screws')
reinforcedPlates = Recipe.CreateRecipe(base, {'ironPlate': 30, 'screws': 60}, 5, 'reinforcedPlates')
rotors = Recipe.CreateRecipe(base, {'ironRod': 2, 'screws': 100}, 4, 'rotors')