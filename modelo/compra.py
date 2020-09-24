from errores.error import CompraNoTieneProductosError
from modelo.producto import Producto

class Compra(object):
  def __init__(self):
    self.productos=[]
    
  def agregar(self,producto):
    self.productos.append(producto)
  
  def subtotal(self):
    subtotal=0
    for producto in self.productos:
      subtotal+=producto.valor
    return subtotal
  
  def subtotalDescuentos(self):
    total=0
    if len(self.productos) == 0:
      raise CompraNoTieneProductosError
    else:
      for producto in self.productos:
        total += producto.valor * producto.descuento / 100
    return total
    

      