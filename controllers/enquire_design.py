from odoo import http
from odoo.http import request

class DesignEnquireController(http.Controller):

    @http.route('/submit_design', type='http', auth='user', website=True)
    def submit_design(self, **kwargs):
        contact_name = kwargs.get('contact_name')
        phone = kwargs.get('phone')
        # mobile = kwargs.get('mobile') 
        email_from = kwargs.get('email_from')
        floor_plan = kwargs.get('floor_plan')
        rooms = kwargs.get('room')
        print("LLLLLLLLLLLLLLLLLL",phone,contact_name,email_from,rooms)
        name = "interior design enquiry" # Corrected from Kwargs to kwargs


        partner_id = self._get_partner_id(contact_name)

        new_lead = request.env['crm.lead'].sudo().create({
            'contact_name': contact_name, 
            'phone': phone,
            'email_from': email_from,
            'name': name,
            'floor_plan':floor_plan,
            'room': rooms,
            'partner_id': partner_id,  
        })

        # new_lead_fields = request.env['sale.order'].sudo().create({
        # 	'floor_plan':floor_plan,
        #     'room': rooms,
        # 	})

        return request.render('interior.design_enquiry_thankyou_template',{})

    def _get_partner_id(self, contact_name):
        partner = request.env['res.partner'].sudo().create({'name': contact_name})
        return partner.id

    