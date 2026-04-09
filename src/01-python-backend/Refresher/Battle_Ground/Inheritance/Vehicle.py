class Vehicle:

    def __init__(self, name:str | None = None, make: str | None = None, model: str | None = None, year: str | None = None,
                 miles: int | None = None, mpg: float | None = None, runs: bool | None = None, v_type: str | None = None) -> None:
                self.name = name
                self.make = make
                self.model = model
                self.year = year
                self.miles = miles
                self.mpg = mpg
                self.runs = runs
                self.v_type = v_type


    def ignition_on(self):
        print(f'{self.name} has turned on')

    def ignition_off(self):
        print('Vehicle has turned off')
