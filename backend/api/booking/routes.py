from flask import request
from flask import request
from flask_restx import Resource, Namespace
from flask_jwt_extended import jwt_required

import pymongo
import datetime
from database import db
from bson import ObjectId

api = Namespace('bookings', description='Appointments related operations')

@api.route('/available')
class Available(Resource):
    def get(self):
        ''' Endpoint to get all available hours admin has made ''' 
        # Delte outdated bookings
        db.get_collection('bookings').delete_many({'date': { '$lte': datetime.datetime.utcnow()}})

        # Get documents of available dates
        dates = list(db.get_collection('bookings').find({'booking': None}, {'_id': 0}))
        for date in dates:
            date['date'] = date['date'].isoformat()
        return {'dates': dates}

@api.route('/make')
class MakeBooking(Resource):
    def post(self):
        ''' Endpoint to make a booking '''
        date = datetime.datetime.strptime(request.json['date'], '%Y-%m-%dT%H:%M:%S.%fz')
        id = db.get_collection('bookings').find_one_and_update({'date': date}, {'$set': {'booking': request.json['booking']}}).get('_id')
        return {'id': str(id)}, 201

@api.route('/cancel')
class CancelBooking(Resource):
    def post(self):
        ''' Endpoint to cancel currenly made booking '''
        db.get_collection('bookings').find_one_and_update({'_id': ObjectId(request.json['id'])}, {'$set': {'booking': None}})
        return {}

@api.route('/admin/bookings')
class Bookings(Resource):
    @jwt_required()
    def get(self):
        ''' Endpoint to get bookings user has made '''
        # Delte outdated bookings
        db.get_collection('bookings').delete_many({'date': { '$lte': datetime.datetime.utcnow()}})

        # Get documents of current date
        bookings = list(db.get_collection('bookings').find({'booking': {'$ne': None}}, {'_id': 0}).sort('date', pymongo.ASCENDING))
        for booking in bookings:
            booking['date'] = booking['date'].isoformat()
        return {'bookings': bookings}

@api.route('/admin/added')
class AdminAvailable(Resource):
    @jwt_required()
    def get(self):
        ''' Endpoint to get admin added date hours '''
        hours = []
        day = datetime.datetime.strptime(request.args['day'], '%Y-%m-%dT%H:%M:%S.%fz')
        day_end = day + datetime.timedelta(days=1) - datetime.timedelta(seconds=1)

        dates = list(db.get_collection('bookings').find({'date': {'$lt': day_end, '$gte': day}}).sort('date', pymongo.ASCENDING))
        for date in dates:
            hours.append({
                'date': date['date'].isoformat(),
                'booked': date['booking'] is not None
            })
        
        return {'dates': hours}

@api.route('/admin/add')
class AddAvailble(Resource):
    @jwt_required()
    def post(self):
        ''' Endpoint to add available booking hour '''
        date = datetime.datetime.strptime(request.json['date'], '%Y-%m-%dT%H:%M:%S.%fz')
        if db.get_collection('bookings').find({'date': date}).count() > 0:
            return {'message': 'Already exists!'}, 409
        db.get_collection('bookings').insert_one({
            'date': date,
            'booking': None
        })
        return {}, 201