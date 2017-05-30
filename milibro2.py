# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

def _sel_func(self, cr, uid, context=None):
    obj = self.pool.get('milibro2.categorias')
    ids = obj.search(cr, uid, [])
    res = obj.read(cr, uid, ids, ['nombre', 'id'], context)
    for r in res:
        resultado= r['nombre']
    return resultado

class milibro2_categorias(osv.osv):
    _name = 'milibro2.categorias'
    _columns = {
        'nombre': fields.char('Descripcion',size=150,requerided=True),
        'libros_ids': fields.one2many('milibro2', 'categoria', 'Categorias'),
    }
milibro2_categorias()

class milibro2(osv.osv):
    _inherit = 'milibro'
    _name = 'milibro2'
    _columns={
        'isbn': fields.char('ISBN',size=15,requerided=True),
        'precio': fields.float('Precio',digits=(4,2)),
        'resumen': fields.text('Descripcion'),
        'fecha': fields.date('Fecha'),
        'revisado': fields.boolean('Revisado'),
        'aprobado': fields.selection((('S','Si'),('N','No'),('P','Pendiente')),'Aprobado'),
        'categoria': fields.selection(_sel_func,'Categoria')
        #,selection = _sel_func, ondelete='cascade'),
    }
milibro2()
