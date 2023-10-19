from flask import Blueprint, jsonify, request
from app.modals.measure_response import MeasureResponse, MeasureDetail, MeasureType
from app.service.measure_factory import MeasureFactory

# Create a Flask Blueprint which will define the routes
controller_blueprint = Blueprint('controller', __name__)

# schema = MeasureResponseSchema()


@controller_blueprint.route('/')
def hello():
    return jsonify({"message": "Hello, World!"})


@controller_blueprint.route('/api/v1/score/update', methods=['PUT'])
def update_score():
    # Retrieve the query parameters
    measure = request.args.get('measure')
    services = request.args.get('services')
    orgs = request.args.get('orgs')

    # For this example, we're just echoing the received parameters.
    # In a real-world scenario, you'd likely use these parameters to update data in a database or some other action.
    measure = MeasureType(measure)
    measure_factory = MeasureFactory()
    measure_instance = measure_factory.get_measure_instance(measure)
    response = measure_instance.generate_score()
    # print(measure_instance.get_measure_type())
    # response = MeasureResponse(score=10,
    #                            measure_type=measure_instance.get_measure_type().name,
    #                            service=services,
    #                            org=orgs,
    #                            measure_details=[MeasureDetail(measure_unit="unit", measure_value=10)])

    return jsonify(response.__dict__)
