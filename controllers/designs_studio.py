from odoo import http
from odoo.http import request
import re 


class DesignStudioController(http.Controller):


    @http.route('/designs studio', type="http", auth="public", website=True)
    def interior_designs_studio(self, **kw):

        return request.render('interior.designs_studio_form_template',{})

