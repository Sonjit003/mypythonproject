class home_appliance():
    def __init__(self, brand:str, model:str) -> None:
        self.brand = brand
        self.model = model
        self.name_n_brand = self.brand +  self.model
    def conect(self):
        return self.brand + self.model
       



connection = home_appliance(brand= "Amazon:", model= "Alexa") 
# print(connection.name_n_brand +  " is connected")
