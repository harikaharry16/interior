from odoo import fields,models,api



class CrmLead(models.Model):
    _inherit = 'crm.lead'

    # Define your additional fields here
    floor_plan = fields.Char(string="floor_plan")
    room = fields.Char(string="room")

# class SaleOrder(models.Model):
#     _inherit = 'sale.order'

#     floor_plan = fields.Char(string="floor_plan")
#     room = fields.Char(string="room")


    # @api.multi
    # def create_sale_order_from_crm_lead(self, crm_lead_id):
    #     crm_lead = self.env['crm.lead'].browse(crm_lead_id)
    #     return {
    #         'name': 'New Quotation',
    #         'type': 'ir.actions.act_window',
    #         'res_model': 'sale.order',
    #         'view_mode': 'form',
    #         'context': {
    #             'default_floor_plan': crm_lead.floor_plan,
    #             'default_room': crm_lead.room,
    #         },
    #     }
