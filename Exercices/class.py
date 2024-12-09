class Car:
    def __init__(self, name_color="unknown", name_brand="unknown", name_model="unknown", year="unknown", nbr_km="unknown"):
        self.brand = name_brand
        self.color = name_color
        self.model = name_model
        self.year = year
        if nbr_km.replace('.', '').isdigit() and nbr_km.count('.') <= 1:
            self.nbr_km = nbr_km
        else:
            self.nbr_km = 'unknown'

    def text(self):
        print("hello")

    def describe(self) :
        print(f"""Car Information:
              \ncolor: {self.color}
              \nbrand: {self.brand}
              \nmodel: {self.model}
              \nyear: {self.year}
              \nnumbre of mileage: {self.nbr_km}
              """)


class Electricecar(Car):
    def __init__(self, name_color="unknown", name_brand="unknown", name_model="unknown", year="unknown", nbr_km="unknown", electrice="nothing"):
        super().__init__(name_color, name_brand, name_model, year, nbr_km)
        self.electrice = electrice
        self.text()

    def describe(self):
        print(f"Electric car with extra feature: {self.electrice}")
        super().describe()


my_electric_car = Electricecar('green', 'Tesla', 'Model X', '2023', '12000', 'electric')
my_electric_car.describe()
