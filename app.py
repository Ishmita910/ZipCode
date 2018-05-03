from flask import Flask, Response
from ZipCodes import loadData, ZipCode
data = loadData()
app = Flask(__name__, static_url_path='', static_folder='.')
app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))

@app.route('/vis/<int:zip>')
def hello(zip):
	df = data
	response = ''
	if df is not None:
		response = ZipCode(df, zip).to_json()

	return Response(response,
		mimetype='application/json',
		headers={
			'Cache-Control': 'no-cache',
			'Access-Control-Allow-Origin': '*'
		}
	)

if __name__ == '__main__':
	app.run(port=8000)