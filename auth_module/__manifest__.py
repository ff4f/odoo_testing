##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2013 OpenERP S.A. (<http://openerp.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Auth Module',
    'version': '14.0.0.1',
    'category': 'Tools',
    'description': """Authentification User""",
    'author': "FF",
    'depends': ['base', 'resource', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_users_view.xml',
        'views/webclient_templates.xml',
        'data/scheduler.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
