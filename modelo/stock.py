from errores.error import ProductoNoEncontradoError
class Stock(object):
  def __init__(self):
     self.productos = []

  def cantidadProductos(self):
    "Retorna la cantidad de productos que tiene en el listado"
    return len(self.productos)

  def agregar(self,producto):
    "Agrega la un product al listado en el stock"
    self.productos.append(producto)

  def buscar(self, codigoProducto):
    "Realiza la busqueda sobre el stock"
    for producto in self.productos:
      if codigoProducto == producto.codigo:
        return producto
    else:
      raise ProductoNoEncontradoError()
 