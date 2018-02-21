# -*- coding: utf-8 -*-
from odoo import http

# class /home/odoo-ps/code/openacademy/openacademy(http.Controller):
#     @http.route('//home/odoo-ps/code/openacademy/openacademy//home/odoo-ps/code/openacademy/openacademy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//home/odoo-ps/code/openacademy/openacademy//home/odoo-ps/code/openacademy/openacademy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/home/odoo-ps/code/openacademy/openacademy.listing', {
#             'root': '//home/odoo-ps/code/openacademy/openacademy//home/odoo-ps/code/openacademy/openacademy',
#             'objects': http.request.env['/home/odoo-ps/code/openacademy/openacademy./home/odoo-ps/code/openacademy/openacademy'].search([]),
#         })

#     @http.route('//home/odoo-ps/code/openacademy/openacademy//home/odoo-ps/code/openacademy/openacademy/objects/<model("/home/odoo-ps/code/openacademy/openacademy./home/odoo-ps/code/openacademy/openacademy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/home/odoo-ps/code/openacademy/openacademy.object', {
#             'object': obj
#         })