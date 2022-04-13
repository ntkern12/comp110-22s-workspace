"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "YOUR PID HERE"


class Simpy:
    """Class Simpy."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Constructor."""
        self.values = values
    
    def __str__(self) -> str:
        """Produce a string representation of Simpy."""
        return f"Simpy({self.values})"

    def fill(self, value: float, num_values: int) -> None:
        """Fill Method."""
        vals = []
        i = 0
        while i < num_values:
            vals = vals + [value]
            i = i + 1
        self.values = vals
        
    def arange(self, start: float, stop: float, step: float = 1.0):
        """Arange Method."""
        assert step != 0.0
        i = 0
        rang_vals = []
        if step == 1.0:
            reps = stop - step
        else:
            reps = stop / step
        while i < reps:
            if i == 0:
                rang_vals = rang_vals + [start]
            else:
                rang_vals = rang_vals + [start + (step * i)]
            i = i + 1
        self.values = rang_vals

    def sum(self) -> float:
        """Sum Method."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overload add operator."""
        self_vals = self.values
        if isinstance(rhs, float):
            rhs_vals = []
            j = 0
            while j < len(self.values):
                rhs_vals = rhs_vals + [rhs]
                j = j + 1
            rhs = Simpy(rhs_vals)
        else:
            rhs = rhs
        assert len(self.values) == len(rhs.values)
        rhs_vals = rhs.values
        new_vals = []
        i = 0
        while i < len(self_vals):
            new_vals = new_vals + [(self_vals[i] + rhs_vals[i])]
            i = i + 1
        return Simpy(new_vals)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overload exponential operator."""
        self_vals = self.values
        if isinstance(rhs, float):
            rhs_vals = []
            j = 0
            while j < len(self.values):
                rhs_vals = rhs_vals + [rhs]
                j = j + 1
            rhs = Simpy(rhs_vals)
        else:
            rhs = rhs
        assert len(self.values) == len(rhs.values)
        rhs_vals = rhs.values
        new_vals = []
        i = 0
        while i < len(self_vals):
            new_vals = new_vals + [(self_vals[i] ** rhs_vals[i])]
            i = i + 1
        return Simpy(new_vals)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overload exponential operator."""
        self_vals = self.values
        if isinstance(rhs, float):
            rhs_vals = []
            j = 0
            while j < len(self.values):
                rhs_vals = rhs_vals + [rhs]
                j = j + 1
            rhs = Simpy(rhs_vals)
        else:
            rhs = rhs
        assert len(self.values) == len(rhs.values)
        rhs_vals = rhs.values
        new_vals = []
        i = 0
        while i < len(self_vals):
            new_vals = new_vals + [(self_vals[i] == rhs_vals[i])]
            i = i + 1
        return new_vals

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overload greater than operator."""
        self_vals = self.values
        if isinstance(rhs, float):
            rhs_vals = []
            j = 0
            while j < len(self.values):
                rhs_vals = rhs_vals + [rhs]
                j = j + 1
            rhs = Simpy(rhs_vals)
        else:
            rhs = rhs
        assert len(self.values) == len(rhs.values)
        rhs_vals = rhs.values
        new_vals = []
        i = 0
        while i < len(self_vals):
            new_vals = new_vals + [(self_vals[i] > rhs_vals[i])]
            i = i + 1
        return new_vals

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overload getitem operator."""
        value_list = self.values
        if isinstance(rhs, int):
            new_value = value_list[rhs]
            return new_value
        else:
            i = 0
            new_list = []
            while i < len(rhs):
                if rhs[i] is True:
                    new_list = new_list + [value_list[i]]
                    i = i + 1
                else:
                    i = i + 1
            return Simpy(new_list)