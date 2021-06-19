# -*- encoding: utf-8 -*-

from odoo import api, models, fields
from datetime import date
import datetime
import time
import dateutil.parser
from dateutil.relativedelta import relativedelta
from dateutil import relativedelta as rdelta
from odoo.fields import Date, Datetime
import pytz
import logging
import operator
from operator import itemgetter

class ReporteVentas(models.AbstractModel):
    _name = 'report.pos_ticket_cierre.reporte_cierre'


    def _get_cierre(self,session_id):
        return False

    def fecha_actual(self):
        timezone = pytz.timezone(self._context.get('tz') or self.env.user.tz or 'UTC')
        fecha_hora = datetime.datetime.now().astimezone(timezone).strftime('%d/%m/%Y')
        return fecha_hora

    @api.model
    def _get_report_values(self, docids, data=None):
        return self.get_report_values(docids, data)

    @api.model
    def get_report_values(self, docids, data=None):
        self.model = 'pos.session'
        # fecha = data.get('form', {}).get('fecha', False)
        # linea_negocio_id = data.get('form', {}).get('linea_negocio_id', False)
        # formato_planilla_id = data.get('form', {}).get('formato_planilla_id', False)
        docs = self.env[self.model].browse(docids)
        logging.warn(docs)


        return {
            'doc_ids': docids,
            'doc_model': self.model,
            'docs': docs,
            # 'fecha': fecha,
            # 'linea_negocio_id': linea_negocio_id,
            '_get_cierre': self._get_cierre,
            'fecha_actual': self.fecha_actual,
        }
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
