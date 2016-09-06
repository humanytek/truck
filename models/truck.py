from openerp import api, fields, models


class Truck(models.AbstractModel):
    _inherit = 'vehicle'
    _name = 'truck'

    driver = fields.Char()
    car_plates = fields.Char()

    input_kilos = fields.Float()
    output_kilos = fields.Float()

    @api.one
    @api.depends('input_kilos', 'output_kilos')
    def _compute_raw_kilos(self):
        self.raw_kilos = self.input_kilos - self.output_kilos
