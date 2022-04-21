from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import model

class Search_Zip(MethodView):
    def get(self):
        return render_template('search_zip.html')

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        current_model = model.get_model()
        current_model.search_city(request.form['zip'])
        return redirect(url_for('forecast'))

