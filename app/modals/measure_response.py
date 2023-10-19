from dataclasses import dataclass
from enum import Enum
from typing import List

from marshmallow import Schema, fields, validate


class MeasureType(Enum):
    RELEASE_ISSUES = "release_issues"
    BUILD_TIME = "build_time"
    DEPLOYMENT_HEALTH = "deployment_health"
    PRODUCTION_ISSUES = "production_issues"
    E2E_TESTS_SUCCESS_RATE = "e2e_tests_success_rate"


class Org(Enum):
    ORG_1 = "org_1"
    ORG_2 = "org_2"


@dataclass
class MeasureDetail:
    measure_unit = str
    measure_value = int

    def __init__(self, measure_unit: str, measure_value: int):
        self.measure_unit = measure_unit
        self.measure_value = measure_value


# class MeasureDetailSchema(Schema):
#     measure_unit = fields.Str
#     measure_value = fields.Int


@dataclass
class MeasureResponse:
    """ Data class for Measure Response """
    score = int
    measure_type = str
    service = str
    org = str
    measure_details = List[MeasureDetail]
    meta_data = dict

    def __init__(self, score: int, measure_type: str, service: str, org: str, measure_details: List[MeasureDetail]):
        self.score = score
        self.measure_type = measure_type
        self.service = service
        self.org = org
        self.measure_details = measure_details
        self.meta_data = list()


# class MeasureResponseSchema(Schema):
#     status = fields.Int
#     measure_type = fields.Str(validate=validate.OneOf([e.value for e in Measure]))
#     service = fields.Str
#     org = fields.Enum(enum=Org)
#     measure_details = fields.List(fields.Raw)
#     meta_data = fields.Dict(keys=fields.Str, values=fields.Raw)
