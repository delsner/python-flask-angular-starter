from flask import Blueprint, make_response, jsonify, request

from app.models import Cluster

cluster_api = Blueprint('cluster_api', __name__)


def cluster_to_dict(cluster):
    return {
        'id': cluster.id,
        'name': cluster.name,
        'date_created': cluster.date_created,
        'date_modified': cluster.date_modified,
        'data': cluster.data
    }


@cluster_api.route("/", methods=['GET'])
def get_all_clusters():
    clusters = Cluster.get_all()
    results = jsonify(list(map(cluster_to_dict, clusters)))
    return make_response(results), 200


@cluster_api.route("/", methods=['POST'])
def create_cluster():
    cluster = request.get_json()
    cluster = Cluster(cluster['name'], cluster['data'])
    cluster.save()
    result = jsonify(cluster_to_dict(cluster))
    return make_response(result), 201


@cluster_api.route("/<int:id>", methods=['GET'])
def get_cluster(id, **kwargs):
    cluster = Cluster.get_single(id)
    result = jsonify(cluster_to_dict(cluster))
    return make_response(result), 200
