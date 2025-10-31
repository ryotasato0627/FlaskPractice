from flask import Blueprint, jsonify, request
from ..models.note import Note
from .. import db

main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=["GET"])
def root():
    return jsonify({"message" : "Hello Flask!!!"})