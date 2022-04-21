"""
A simple Weather Forecast flask app.
"""
import flask, os
from flask.views import MethodView
from index import Index
from search_city import Search_City
from search_zip import Search_Zip
from forecast import Forecast

app = flask.Flask(__name__)       # our Flask app

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

app.add_url_rule('/search_city',
                 view_func=Search_City.as_view('search_city'),
                 methods=['GET', 'POST'])

app.add_url_rule('/search_zip',
                 view_func=Search_Zip.as_view('search_zip'),
                 methods=['GET', 'POST'])

app.add_url_rule('/forecast',
		  view_func=Forecast.as_view('forecast'),
		  methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT',5000)))
