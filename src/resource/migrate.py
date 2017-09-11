# coding:utf-8
import operation.migrate as Mg

from flask_restful import Resource, reqparse


class MigrateLocal(Resource):
    """
    move from the local to the local
    mv data
    """

    def post(self, name, srcpath, dstpath):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, location='json', required=True)
        parser.add_argument('srcpath', type=str, location='json', required=True)
        parser.add_argument('dstpath', type=str, location='json', required=True)
        args = parser.parse_args()
        name = args['name']
        srcpath = args['srcpath']
        dstpath = args['dstpath']
        srcpath = srcpath + name
        result = Mg.local(srcpath, dstpath)
        if(result is not True):
            return {"message": result}, 422
        return {"message": "successful"}, 201


class MigrateHost(Resource):
    """
    move from the local to the other host
    wake rsync on recieve server
    send image data using fabric
    """

    def post(self, name, srcpath, dstip, dstpath):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, location='json', required=True)
        parser.add_argument('srcpath', type=str, location='json', required=True)
        parser.add_argument('dstip', type=str, location='json', required=True)
        parser.add_argument('dstpath', type=str, location='json', required=True)
        args = parser.parse_args()
        name = args['name']
        srcpath = args['srcpath']
        dstpath = args['dstip']
        dstpath = args['dstpath']
        srcpath = srcpath + name
        result = Mg.host(srcpath, dstip, dstpath)
        if(result is False):
            return {"message": "failed"}, 422
        return {"message": "successful"}, 201
