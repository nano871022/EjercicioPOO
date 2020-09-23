import unittest
from errores.error import ProductoNoEncontradoError
from errores.error import CompraNoTieneProductosError
from modelo.compra import Compra
from modelo.stock import Stock
from modelo.producto import Producto

class CompraTest(unittest.TestCase):
  def setUp(self):
    self.stock = Stock()
    self.stock.agregar(Producto("prod1",10,0))
    self.stock.agregar(Producto("prod2",5,10))
    self.stock.agregar(Producto("prod3",20,55))
    self.compra = Compra(self.stock)

  def testAgregarUnProductoThrowProductoNoEncontrado(self):
    producto="noexiste"
    self.assertRaises(ProductoNoEncontradoError,self.compra.agregar,producto)
  
  def testAgregarUnProductoReturnSubtotal10(self):
    producto="prod1"
    self.compra.agregar(producto)
    result=self.compra.subtotal()
    self.assertEqual(10,result)
  
  def testAgregarDosProductoReturnSubtotal20(self):
    producto="prod1"
    self.compra.agregar(producto)
    self.compra.agregar(producto)
    result=self.compra.subtotal()
    self.assertEqual(20,result)
  
  def testAgregarUnProductoReturnSubtotal5(self):
    producto="prod2"
    self.compra.agregar(producto)
    result=self.compra.subtotal()
    self.assertEqual(5,result)
  
  def testAgregarDosProductosDistintosReturnSubtotal15(self):
    self.compra.agregar("prod1")
    self.compra.agregar("prod2")
    result=self.compra.subtotal()
    self.assertEqual(15,result)

  def testAgregarTresProductosDistintosReturnSubtotal35(self):
    self.compra.agregar("prod1")
    self.compra.agregar("prod2")
    self.compra.agregar("prod3")
    result=self.compra.subtotal()
    self.assertEqual(35,result)

  def testObtenerSubTotalProductosReturn0(self):
    result=self.compra.subtotal()
    self.assertEqual(0,result)
  
  def testFinalizarSinProductosLanzaErrorCompraNoTieneProductosError(self):
    self.assertRaises(CompraNoTieneProductosError,self.compra.finalizar)
  
  def testFinalizarUnProductoEntoncesRetornaTotalProductoSinDescuento(self):
    self.compra.agregar("prod1")
    result=self.compra.finalizar()
    self.assertEqual(10,result)
  
  def testFinalizarUnProductoConDescuentoRetornaTotal(self):
    self.compra.agregar("prod2")
    result=self.compra.finalizar()
    self.assertEqual(5-5*10/100,result)

  def testFinalizarDosProductoConDescuentoRetornaTotal(self):
    descuento=(5-5*10/100) + (20-20*55/100)
    self.compra.agregar("prod2")
    self.compra.agregar("prod3")
    result=self.compra.finalizar()
    self.assertEqual(descuento,result)
  def testFinalizarTresProductoConDescuentoRetornaTotal(self):
    descuento=(5-5*10/100) + (20-20*55/100) + 10
    self.compra.agregar("prod2")
    self.compra.agregar("prod1")
    self.compra.agregar("prod3")
    result=self.compra.finalizar()
    self.assertEqual(descuento,result)


