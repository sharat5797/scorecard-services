from app.modals.measure_response import MeasureType
from app.service.measure_interface import Measure
from app.measures.release_issues_measure.release_issues import ReleaseIssuesMeasure
from app.measures.build_time_measure.build_time import BuildTimeMeasure
from app.measures.deployment_health_measure.deployment_health import DeploymentHealthMeasure
from app.measures.production_issues_measure.production_issues import ProductionIssuesMeasure
from app.measures.e2e_tests_success_rate_measure.e2e_tests_success_rate import E2ETestsSuccessRateMeasure

class MeasureFactory:

    @staticmethod
    def get_measure_instance(measure_type: MeasureType) -> Measure: 
        if measure_type == MeasureType.RELEASE_ISSUES:
            return ReleaseIssuesMeasure()
        elif measure_type == MeasureType.BUILD_TIME:
            return BuildTimeMeasure()
        elif measure_type == MeasureType.DEPLOYMENT_HEALTH:
            return DeploymentHealthMeasure()
        elif measure_type == MeasureType.PRODUCTION_ISSUES:
            return ProductionIssuesMeasure()
        elif measure_type == MeasureType.E2E_TESTS_SUCCESS_RATE:
            return E2ETestsSuccessRateMeasure()
        else:
            raise ValueError("Invalid measure type")


