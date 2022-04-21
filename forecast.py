from flask import render_template
from flask.views import MethodView
import model

class Forecast(MethodView):
    def get(self):
        current_model = model.get_model()
        data = current_model.get_data();
        return render_template('forecast.html',data=data)
        
    def post(self):
    	current_model = model.get_model()
    	return redirect('index.html')
