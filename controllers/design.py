from odoo import http
from odoo.http import request
import re 


class DesignController(http.Controller):


    @http.route('/design', type="http", auth="public", website=True)
    def interior_design_enquiry(self, **kw):

        return request.render('interior.design_enquiry_form_template',{})


