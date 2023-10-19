from app.service.measure_interface import Measure
from app.measures.release_issues_measure.release_issues import ReleaseIssuesMeasure
from app.measures.build_time_measure.build_time import BuildTimeMeasure
from app.measures.deployment_health_measure.deployment_health import DeploymentHealthMeasure
from app.measures.production_issues_measure.production_issues import ProductionIssuesMeasure
from app.measures.e2e_tests_success_rate_measure.e2e_tests_success_rate import E2ETestsSuccessRateMeasure

class MeasureFactory:

    @staticmethod
    def get_measure_instance(measure_type: str) -> Measure:
        measure_type = measure_type.lower()  # Convert to lowercase to ensure case-insensitive matching

        if measure_type == "release_issues":
            return ReleaseIssuesMeasure()
        elif measure_type == "build_time":
            return BuildTimeMeasure()
        elif measure_type == "deployment_health":
            return DeploymentHealthMeasure()
        elif measure_type == "production_issues":
            return ProductionIssuesMeasure()
        elif measure_type == "e2e_tests_success_rate":
            return E2ETestsSuccessRateMeasure()
        else:
            raise ValueError("Invalid measure type")

\
