from flask import request
from flask_restplus import Resource
from ..api import ns

process_route = "/predict_construction_time"


@ns.route(process_route)
class PredictModelVersions(Resource):
    def get(self):
        """
        Return the list of all applicable model versions, optionally with their creation dates?
        :return: Map<model_version_label, date_created>
        """
        #  DO WORK HERE
        pass


@ns.route(process_route + '/<int:model_ref>/cnc_quick_materials')
class CNCQuickMaterials(Resource):
    def get(self):
        """
        <Meaningful comment here>
        """
        arg = request.json["market_based_lead_time_price"]
        #  DO WORK HERE
        pass


@ns.route(process_route + '/<int:model_ref>/cnc_nonquick_materials')
class CNCNonQuickMaterials(Resource):
    def get(self):
        """
        <Meaningful comment here>
        """
        arg = request.json["market_based_lead_time_price"]
        #  DO WORK HERE
        pass


@ns.route(process_route + '/<int:model_ref>/sheet_metal')
class SheetMetal(Resource):
    def get(self):
        """
        <Meaningful comment here>
        """
        arg = request.json["market_based_lead_time_price"]
        #  DO WORK HERE
        pass


