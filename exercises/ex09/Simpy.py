"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730391824"


class Simpy:
    """Class that is helpful for numerical data."""
    values: list[float]

    def __init__(self, start: list[float]):
        """Constructor."""
        self.values = start

    def __str__(self) -> str:
        """Make list into str."""
        return f"Simpy({self.values})"

    def fill(self, filling: float, n: int) -> None:
        """Repeat "filling" as many times as n."""
        new_list: list[float] = []
        i: int = 0
        while i < n:
            new_list.append(filling)
            i += 1
        self.values = new_list
 
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """First value is start and add step amount till stop point."""
        assert step != 0.0
        self.values = []
        if step > 0:
            while start < stop:
                self.values.append(start)
                start += step
        else:
            while start > stop:
                self.values.append(start)
                start += step

    def sum(self) -> float:
        """Sum of all values."""
        sum_value: float = 0
        for value in self.values:
            sum_value += value
        return sum_value

    def __add__(self, other: Union[Simpy, float]) -> Simpy:
        """Add two different simpys."""
        new_simp: Simpy = Simpy([])
        if isinstance(other, Simpy):
            assert len(other.values) == len(self.values)
        if isinstance(other, float):
            for item in self.values:
                new_simp.values.append(item + other)
            return new_simp
        else:
            i: int = 0
            for item in self.values:
                new_simp.values.append(item + other.values[i])
                i += 1
        return new_simp

    def __pow__(self, other: Union[Simpy, float]) -> Simpy:
        """Raise the self to the power of the corresponding other value."""
        new_simp: Simpy = Simpy([])
        if isinstance(other, Simpy):
            assert len(other.values) == len(self.values)
        if isinstance(other, float):
            for item in self.values:
                new_simp.values.append(item ** other)
            return new_simp
        else:
            i: int = 0
            for item in self.values:
                new_simp.values.append(item ** other.values[i])
                i += 1
        return new_simp

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """If each value in self is equal to (==) the flost or same value in other Simpy."""
        bool_list: list[bool] = []
        i: int = 0
        if isinstance(rhs, float):
            for item in self.values:
                if item == rhs:
                    bool_list.append(True)
                else:
                    bool_list.append(False)
        else:
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    bool_list.append(True)
                else:
                    bool_list.append(False)
                i += 1
        return bool_list

    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """If each value in self is greater than (>) the flost or same value in other Simpy."""
        bool_list: list[bool] = []
        i: int = 0
        if isinstance(rhs, float):
            for item in self.values:
                if item > rhs:
                    bool_list.append(True)
                else:
                    bool_list.append(False)
        else:
            while i < len(self.values):
                if self.values[i] > rhs.values[i]:
                    bool_list.append(True)
                else:
                    bool_list.append(False)
                i += 1
        return bool_list

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Can extract certain values that apply."""
        if isinstance(rhs, int):
            wanted: float = self.values[rhs]
            return wanted
        else:
            new_simp: Simpy = Simpy([])
            i: int = 0
            for item in self.values:
                if rhs[i]:
                    new_simp.values.append(item)
                i += 1
            return new_simp