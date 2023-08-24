from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from celery_test import add, star, task_update


app = Flask(__name__)


api = Api(app, version='0.0.1', title='Celery_project', doc='/api')


# get輸出方式
basic_output = api.model(
    'star',{
        'task_id': fields.String(required=True)
})


@api.route('/star')
class MyResource(Resource):
    @api.doc(params={'star': 'star'})
    @api.marshal_with(basic_output)  # 傳出格式
    def get(self):
        get_task = int(request.args.get('star'))
        task = star.apply_async(args=[get_task], countdown=20)
        response = {
            'task_id': task.id
        }
        return response


# post傳入方式
post_input = api.model('add', {
    'num1': fields.Integer(required=True, default=1),
    'num2': fields.Integer(required=True, default=2)
})


@api.route('/add')
class post_test(Resource):
    @api.expect(post_input)  # 傳入格式
    def post(self):
        data = api.payload
        print(f"{data['num1']} + {data['num2']} 處理中...")
        task = add.apply_async(
            args=(
                data['num1'],
                data['num2']
            ),
            countdown=50
        )
        return jsonify({'task_id': task.id})


@api.route('/celery_test')
class celery_test(Resource):
    @api.doc(params={'task_id': 'task_id'})
    def get(self):
        get_task = request.args.get('task_id')
        response = task_update.delay(get_task)
        return {
            'state': response.get()
            }


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port="5000")
