# -*- coding: utf-8 -*-
# from odoo import http


# class Carolina(http.Controller):
#     @http.route('/carolina/carolina/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/carolina/carolina/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('carolina.listing', {
#             'root': '/carolina/carolina',
#             'objects': http.request.env['carolina.carolina'].search([]),
#         })

#     @http.route('/carolina/carolina/objects/<model("carolina.carolina"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('carolina.object', {
#             'object': obj
#         })
