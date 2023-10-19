from app.modals.measure_response import MeasureResponse, MeasureDetail, MeasureType
from app.service.measure_interface import Measure


class BuildTimeMeasure(Measure):
    _measure_type: MeasureType

    def get_measure_type(self) -> MeasureType:
        self._measure_type = MeasureType.BUILD_TIME
        return self._measure_type

    def generate_score(self) -> MeasureResponse:
        return MeasureResponse(score=10,
                               measure_type=self.get_measure_type().name,
                               service="services",
                               org="orgs",
                               measure_details=[MeasureDetail(measure_unit="unit", measure_value=10)])