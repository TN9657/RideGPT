import random
from typing import Optional
from datetime import datetime


class BaseProviderSimulator:
    def __init__(self, name: str, base_price: float, reliability: float, cancel_prob: float):
        self.name = name
        self.base_price = base_price
        self.reliability = reliability
        self.cancel_prob = cancel_prob
        self.vehicles = ["Sedan", "SUV", "Hatchback", "Auto", "Bike"]
        self.driver_names = ["Ramesh Kumar", "Suresh Patel", "Amit Singh", "Raj Sharma", "Vikram Nair"]
        self.driver_phones = ["+91-98765-43210", "+91-91234-56789", "+91-80123-45678", "+91-70987-65432", "+91-60123-78901"]

    def get_ride(self, pickup: str, destination: str, vehicle_preference: Optional[str] = None) -> dict:
        surge = round(random.uniform(1.0, 2.0), 2)
        distance_factor = random.uniform(0.8, 1.5)
        price = round(self.base_price * distance_factor * surge, 2)
        eta = random.randint(3, 20)
        rating = round(random.uniform(3.5, 5.0), 1)
        availability = random.random() > 0.15
        vehicle = vehicle_preference if vehicle_preference and vehicle_preference in self.vehicles else random.choice(self.vehicles)
        driver_idx = random.randint(0, len(self.driver_names) - 1)

        return {
            "provider": self.name,
            "price": price,
            "eta": eta,
            "rating": rating,
            "vehicle": vehicle,
            "availability": availability,
            "reliability": self.reliability + random.uniform(-5, 5),
            "cancellation_probability": self.cancel_prob + random.uniform(-0.05, 0.05),
            "surge_multiplier": surge,
            "driver_name": self.driver_names[driver_idx] if availability else None,
            "driver_phone": self.driver_phones[driver_idx] if availability else None,
        }

    def simulate_cancellation(self) -> bool:
        return random.random() < self.cancel_prob

    def simulate_ride_status(self) -> str:
        outcomes = ["active", "active", "active", "active", "completed", "cancelled"]
        return random.choice(outcomes)


class UberSimulator(BaseProviderSimulator):
    def __init__(self):
        super().__init__("Uber", base_price=320, reliability=92, cancel_prob=0.08)
        self.vehicles = ["Sedan", "SUV", "Premier", "Auto"]


class OlaSimulator(BaseProviderSimulator):
    def __init__(self):
        super().__init__("Ola", base_price=260, reliability=85, cancel_prob=0.12)
        self.vehicles = ["Sedan", "Mini", "Auto", "Bike", "Outstation"]


class RapidoSimulator(BaseProviderSimulator):
    def __init__(self):
        super().__init__("Rapido", base_price=180, reliability=78, cancel_prob=0.15)
        self.vehicles = ["Bike", "Auto", "Cab"]


uber_simulator = UberSimulator()
ola_simulator = OlaSimulator()
rapido_simulator = RapidoSimulator()

PROVIDER_MAP = {
    "Uber": uber_simulator,
    "Ola": ola_simulator,
    "Rapido": rapido_simulator,
}


def get_all_providers(pickup: str, destination: str, vehicle_preference: Optional[str] = None) -> list:
    results = []
    for simulator in PROVIDER_MAP.values():
        ride = simulator.get_ride(pickup, destination, vehicle_preference)
        results.append(ride)
    return results
