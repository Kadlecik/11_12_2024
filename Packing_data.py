import pickle

class Airplane:
    def __init__(self, model, airline, capacity):
        self.model = model
        self.airline = airline
        self.capacity = capacity

    def __str__(self):
        return f"Model: {self.model}, Airline: {self.airline}, Capacity: {self.capacity}"

    def fly(self, destination):
        print(f"The airplane {self.model} operated by {self.airline} is flying to {destination}.")

    def board_passengers(self, passengers):
        if passengers <= self.capacity:
            print(f"{passengers} passengers have boarded the airplane.")
        else:
            print(f"Cannot board {passengers} passengers. Maximum capacity is {self.capacity}.")

# Funkce pro serializaci objektu Airplane
def pack_airplane(airplane, filename):
    with open(filename, 'wb') as file:
        pickle.dump(airplane, file)

# Funkce pro deserializaci objektu Airplane
def unpack_airplane(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

# Příklad použití
airplane1 = Airplane("Boeing 747", "Japan Airlines", 416)
print(airplane1)

# Uložení (serializace) objektu do souboru
pack_airplane(airplane1, "airplane.pkl")

# Načtení (deserializace) objektu ze souboru
loaded_airplane = unpack_airplane("airplane.pkl")
print(loaded_airplane)

# Volání metod objektu
loaded_airplane.fly("Tokyo")
loaded_airplane.board_passengers(300)
