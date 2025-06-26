from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('reviews', description='Review operations')

review_model = api.model('Review', {
    'text': fields.String(required=True),
    'rating': fields.Integer(required=True),
    'user_id': fields.String(required=True),
    'place_id': fields.String(required=True)
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    def post(self):
        data = api.payload
        try:
            review = facade.create_review(data)
            if not review:
                return {"error": "Invalid user or place ID"}, 400
            return review.to_dict(), 201
        except ValueError as e:
            return {"error": str(e)}, 400

    def get(self):
        reviews = facade.get_all_reviews()
        return [r.to_dict() for r in reviews], 200

@api.route('/<review_id>')
class ReviewResource(Resource):
    def get(self, review_id):
        review = facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404
        return review.to_dict(), 200

    @api.expect(review_model)
    def put(self, review_id):
        data = api.payload
        try:
            updated = facade.update_review(review_id, data)
            if not updated:
                return {"error": "Review not found"}, 404
            return {"message": "Review updated successfully"}, 200
        except ValueError as e:
            return {"error": str(e)}, 400

    def delete(self, review_id):
        deleted = facade.delete_review(review_id)
        if not deleted:
            return {"error": "Review not found"}, 404
        return {"message": "Review deleted successfully"}, 200

@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    def get(self, place_id):
        reviews = facade.get_reviews_by_place(place_id)
        return [r.to_dict() for r in reviews], 200
