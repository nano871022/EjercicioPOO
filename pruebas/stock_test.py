import unittest
from errores.error import ProductoNoEncontradoError
from modelo.stock import Stock
from modelo.producto import Producto

class StockTest(unittest.TestCase):
  def setUp(self):
    self.stock = Stock()
  def testCantidadProductosRetorna0(self):
    result=self.stock.cantidadProductos()
    self.assertEqual(0,result)
  def testAgregarProductoYObtenerCantidadProductosRetorna1(self):
    producto=Producto("prod1",10,0)
    self.stock.agregar(producto)
    result=self.stock.cantidadProductos()
    self.assertEqual(1,result)
  def testAgregar5ProductoDiferentesYObtenerCantidadProductosRetorna5(self):
    self.stock.agregar(Producto("prod1",10,0))
    self.stock.agregar(Producto("prod2",5,0))
    self.stock.agregar(Producto("prod3",20,0))
    self.stock.agregar(Producto("prod4",30,0))
    self.stock.agregar(Producto("prod5",50,0))
    result=self.stock.cantidadProductos()
    self.assertEqual(5,result)
  def testBuscarProductoNoExisteLanzarProductoNoEncontrado(self):
    producto="prod6"
    self.assertRaises(ProductoNoEncontradoError,self.stock.buscar,producto)
  def testBuscarProductoExisteRetornaProducto(self):
    producto=Producto("prod1",10,0)
    self.stock.agregar(producto)
    result=self.stock.buscar("prod1")
    self.assertEqual(producto,result)
