from flask_restful import Resource


class Hello(Resource):
    def get(self):
        return {"message": "Hello, World! From get."}

    def post(self):
        return {"message": "Hello, World! From post."}
