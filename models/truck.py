from openerp import api, fields, models


class Truck(models.AbstractModel):
    _inherit = 'vehicle'
    _name = 'truck'

    driver = fields.Char()
    car_plates = fields.Char()
    date = fields.Date(default=fields.Date.today)

    input_kilos = fields.Integer()
    output_kilos = fields.Integer()

    @api.one
    @api.depends('input_kilos', 'output_kilos')
    def _compute_raw_kilos(self):
        self.raw_kilos = self.input_kilos - self.output_kilos
