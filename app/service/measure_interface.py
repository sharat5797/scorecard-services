from abc import ABC, abstractmethod
from app.modals.measure_response import MeasureResponse, MeasureType


# Define an abstract base class (interface)
class Measure:
    _measure_type: MeasureType

    @abstractmethod
    def generate_score(self) -> MeasureResponse:
        pass

    @abstractmethod
    def get_measure_type(self) -> MeasureType:
        pass
