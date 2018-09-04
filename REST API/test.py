
from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

APP = Flask(__name__)

APP.config['MONGO_DBNAME'] = 'fav'
APP.config['MONGO_URI'] = 'mongodb://localhost:27017/fav'

MONGO = PyMongo(APP)

@APP.route('/accounts', methods=['GET'])
def GET_ALL_FAVLIST():
    FAV = MONGO.db.favdata
    OUTPUT = []
    for S in FAV.find():
        OUTPUT.append({'FavCountry' : S['FavCountry'], 'AccountId' : S['AccountId'], 'hhid' : S['hhid'], 'DeviceType' : S['DeviceType'], 'ManufacturerName' : S['ManufacturerName'], 'GModelName' : S['GModelName'], 'GlobalDeviceId' :S['GlobalDeviceId'], 'postal' : S['postal'], 'locale' : S['locale'], 'operatorName' : S['operatorName'], 'FullName' : S['FullName'], 'srid' : S['srid'], 'Servicetype' : S['Servicetype'], 'location' : S['location']})
    return jsonify({'result' : OUTPUT})

@APP.route('/accounts/<int:ACID>', methods=['GET'])
# ACID=2954790
def GET_ONE_ACCOUNT(ACID):
    FAV = MONGO.db.favdata
    S = FAV.find_one({'AccountId' : ACID})
    if S:
        OUTPUT = {'FavCountry' : S['FavCountry'], 'AccountId' : S['AccountId'], 'hhid' : S['hhid'], 'DeviceType' : S['DeviceType'], 'ManufacturerName' : S['ManufacturerName'], 'GModelName' : S['GModelName'], 'GlobalDeviceId' :S['GlobalDeviceId'], 'postal' : S['postal'], 'locale' : S['locale'], 'operatorName' : S['operatorName'], 'FullName' : S['FullName'], 'srid' : S['srid'], 'Servicetype' : S['Servicetype'], 'location' : S['location']}
    else:
        OUTPUT = "No Such Records"
    return jsonify({'result' : OUTPUT})


@APP.route('/country= <C>/', methods=['GET'])
# ACID=2954790
def GET_COUNTRY(C):
    FAV = MONGO.db.favdata
    S = FAV.find({'FavCountry' : C})
    if S:
        OUTPUT = {'FavCountry' : S['FavCountry'], 'AccountId' : S['AccountId'], 'hhid' : S['hhid'], 'DeviceType' : S['DeviceType'], 'ManufacturerName' : S['ManufacturerName'], 'GModelName' : S['GModelName'], 'GlobalDeviceId' :S['GlobalDeviceId'], 'postal' : S['postal'], 'locale' : S['locale'], 'operatorName' : S['operatorName'], 'FullName' : S['FullName'], 'srid' : S['srid'], 'Servicetype' : S['Servicetype'], 'location' : S['location']}
    else:
        OUTPUT = "No Such Records"
    return jsonify({'result' : OUTPUT})

if __name__ == '__main__':
    APP.run(debug=True)