# coding:UTF-8
import resource.vm as VMres
import resource.pool as Poolres
import resource.migrate as Migrates

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

api.add_resource(VMres.VM, '/vm')
api.add_resource(VMres.VMname, '/vm/<string:name>')
api.add_resource(VMres.VMclone, '/vm/<string:name>/clone')
api.add_resource(Poolres.Pool, '/pool')
api.add_resource(Poolres.Poolname, '/pool/<string:name>')
api.add_resource(Migrates.migrate, '/migrate')
api.add_resource(Migrates.migrate, '/migrate/local')
api.add_resource(Migrates.migrate, '/migrate/host')


if __name__ == '__main__':
    app.config["ERROR_404_HELP"] = False
    app.run(debug=True, host='0.0.0.0', port=5000)
