from openerp.osv import osv, fields

class ProductProduct(osv.osv):
    _inherit = 'product.product'
    _columns = {
	'default_code' : fields.char('Sku', select=True),
    }
