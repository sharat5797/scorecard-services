from abc import ABC, abstractmethod
from typing import Tuple

from app.modals.measure_response import MeasureResponse, MeasureType
from app.modals.measure_source import MeasureSource


# Define an abstract base class (interface)
class SourceInterface:
    _measure_type: MeasureType
    _measure_source: MeasureSource

    def __int__(self, measure_type: MeasureType, measure_source: MeasureSource):
        self._measure_type = measure_type
        self._measure_source = measure_source

    @abstractmethod
    def get_measure_response(self, service_data: dict, measure_type: MeasureType) -> MeasureResponse:
        pass

    def get_source_measure_type(self) -> Tuple[MeasureType, MeasureSource]:
        return self._measure_type, self._measure_source
