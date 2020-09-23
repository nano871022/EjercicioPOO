from errores.error import CompraNoTieneProductosError

class Compra(object):
  def __init__(self,stock):
    self.productos=[]
    self.stock = []
    self.stock = stock

  def agregar(self,codigoProducto):
    producto=self.stock.buscar(codigoProducto)
    self.productos.append(producto)
  
  def subtotal(self):
    subtotal=0
    for producto in self.productos:
      subtotal+=producto.valor
    return subtotal
  
  def finalizar(self):
    total=0
    if len(self.productos) == 0:
      raise CompraNoTieneProductosError
    else:
      for producto in self.productos:
        total += producto.valor - producto.valor * producto.descuento / 100
    return total
      