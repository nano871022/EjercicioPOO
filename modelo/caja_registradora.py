from modelo.compra import Compra
from errores.error import CompraNoTieneProductosError

class CajaRegistradora(object):
  def __init__(self,stock):
    self.stock = stock
    self.compra = Compra()

  def agregar(self,codigoProducto):
    producto = self.stock.buscar(codigoProducto)  
    self.compra.agregar(producto)
    return self.compra.subtotal()
  
  def finalizar(self):
    subtotal=self.compra.subtotal()
    if subtotal == 0:
      raise CompraNoTieneProductosError() 
    descuentos=self.compra.subtotalDescuentos()
    return subtotal - descuentos
    
  def pagar(self,montoPagado):
    total = self.finalizar()
    if total == 0:
      raise CompraNoTieneProductosError() 
    else:
      return montoPagado - total
  
  def cerrarCompra(self):
    self.compra = Compra()
