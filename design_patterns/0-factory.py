#!/usr/bin/python3
"""Factory registry example

Implements a simple VehicleFactory that maps string keys to classes so
new vehicle types can be registered without modifying the `create` logic.
"""


class Bus:
    def mode(self):
        return "road"


class Train:
    def mode(self):
        return "rails"


class Bike:
    def mode(self):
        return "lane"


class Scooter:
    def mode(self):
        return "scooter_lane"


class VehicleFactory:
    """Registry-based factory for vehicles."""

    def __init__(self):
        self._registry = {}

    def register_kind(self, name, cls):
        """Register a vehicle class under the given name."""
        self._registry[name] = cls

    def create(self, kind):
        """Create an instance of the registered kind.

        Raises a ValueError if the kind is not registered.
        """
        cls = self._registry.get(kind)
        if cls is None:
            raise ValueError(f"Unknown vehicle kind: {kind}")
        return cls()


def main():
    factory = VehicleFactory()

    # register built-in vehicle kinds
    factory.register_kind("bus", Bus)
    factory.register_kind("train", Train)
    factory.register_kind("bike", Bike)

    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())

    # register the new type without changing VehicleFactory.create
    factory.register_kind("scooter", Scooter)
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()
