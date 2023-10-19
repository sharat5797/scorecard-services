from injector import inject, Binder, Module, InstanceProvider, singleton
from app.modals.measure_response import MeasureType
from app.service.measure_interface import Measure
from app.measures.release_issues_measure.release_issues import ReleaseIssuesMeasure


class MeasureFactory:

    @inject
    def __init__(self, measure_providers: Binder):
        self.measure_providers = measure_providers

    def get_measure_instance(self, measure_type: MeasureType) -> Measure:
        measure_provider = self.measure_providers.get_binding(Measure)
        if measure_provider:
            return measure_provider[0]
        else:
            raise ValueError("Invalid measure type")

# Define a Module for Flask-Injector
class MeasureModule(Module):
    def configure(self, binder):
        # Automatically discover and bind MeasureType enum values to their implementation classes
        measure_providers = {
            MeasureType.RELEASE_ISSUES: ReleaseIssuesMeasure,
        }
        for measure_type, measure_provider in measure_providers.items():
            binder.bind(MeasureType, to=InstanceProvider({measure_type: measure_provider}))