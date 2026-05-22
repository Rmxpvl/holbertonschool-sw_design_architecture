#!/usr/bin/env python3
"""Decorator pattern example with beverage toppings."""


class Beverage:
    """Base beverage interface."""

    def cost(self):
        raise NotImplementedError

    def description(self):
        raise NotImplementedError


class Coffee(Beverage):
    """Plain coffee."""

    def cost(self):
        return 50

    def description(self):
        return "Coffee"


class MilkDecorator(Beverage):
    """Add milk to a beverage."""

    def __init__(self, inner):
        self._inner = inner

    def cost(self):
        return self._inner.cost() + 10

    def description(self):
        return self._inner.description() + " + milk"


class SugarDecorator(Beverage):
    """Add sugar to a beverage."""

    def __init__(self, inner):
        self._inner = inner

    def cost(self):
        return self._inner.cost() + 5

    def description(self):
        return self._inner.description() + " + sugar"


class CaramelDecorator(Beverage):
    """Add caramel to a beverage."""

    def __init__(self, inner):
        self._inner = inner

    def cost(self):
        return self._inner.cost() + 15

    def description(self):
        return self._inner.description() + " + caramel"


def main():
    beverage = MilkDecorator(SugarDecorator(Coffee()))
    print(beverage.description(), beverage.cost())

    beverage = CaramelDecorator(MilkDecorator(SugarDecorator(Coffee())))
    print(beverage.description(), beverage.cost())


if __name__ == "__main__":
    main()
