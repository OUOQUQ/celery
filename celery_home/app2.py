from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from celery_test import add, star, task_update


app = Flask(__name__)


api = Api(app, version='0.0.1', title='Celery_project', doc='/api')


# get傳入方式
basic_input = api.model('star_in',{
    'star': fields.Integer(required=True, default=5)
    })

#basic_output = api.model('star_out', {
    # 'task_id': fields.String(required=True)
    # })

@api.route('/star')
class MyResource(Resource):
    @api.doc(params={'my_input': 'my_input'})  # 傳入格式
    def get(self):
        data_star = request.args.get('star')
        task = star.apply_async(args=[data_star], countdown=20)
        response ={
            'task_id' : task.id
            }
        return task.id


# post傳入方式
post_input = api.model('add', {
    'num1': fields.Integer(required=True, default=1),
    'num2': fields.Integer(required=True, default=2)
})


@api.route('/add')
class post_test(Resource):
    @api.expect(post_input)  # 傳入格式
    def post(self):
        data_sum = api.payload
        print(f"{data_sum['num1']} + {data_sum['num2']} 處理中...")
        task = add.apply_async(args=[data_sum['num1'], data_sum['num2']], countdown=100)
        return jsonify({'task_id': task.id})


# celery取得進度
celery_see = api.model('celery_see', {
    'state': fields.String(required=True, default='3b3c6950-d2e8-4ecb-900c')
})


@api.route('/celery_test')
class celery_test(Resource):
    @api.expect(celery_see)  # 傳入格式
    def get(self):
        data_celery = request.args.get('state')
        response = task_update.apply_async(args=[data_celery], priority=0)
        return {
            'state': response.get()
            }


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port="5000")
