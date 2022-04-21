from flask import render_template
from flask.views import MethodView
import model

class Index(MethodView):
    def get(self):
        current_model = model.get_model()
        return render_template('index.html')
