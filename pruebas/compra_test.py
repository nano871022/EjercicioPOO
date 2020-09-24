import unittest
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
    self.compra = Compra()

  def testAgregarUnProductoReturnSubtotal10(self):
    producto=self.stock.buscar("prod1")
    self.compra.agregar(producto)
    result=self.compra.subtotal()
    self.assertEqual(10,result)
  
  def testAgregarDosProductoReturnSubtotal20(self):
    producto=self.stock.buscar("prod1")
    self.compra.agregar(producto)
    self.compra.agregar(producto)
    result=self.compra.subtotal()
    self.assertEqual(20,result)
  
  def testAgregarUnProductoReturnSubtotal5(self):
    producto=self.stock.buscar("prod2")
    self.compra.agregar(producto)
    result=self.compra.subtotal()
    self.assertEqual(5,result)
  
  def testAgregarDosProductosDistintosReturnSubtotal15(self):
    producto1=self.stock.buscar("prod1")
    producto2=self.stock.buscar("prod2")
    self.compra.agregar(producto1)
    self.compra.agregar(producto2)
    result=self.compra.subtotal()
    self.assertEqual(15,result)

  def testAgregarTresProductosDistintosReturnSubtotal35(self):
    producto1=self.stock.buscar("prod1")
    producto2=self.stock.buscar("prod2")
    producto3=self.stock.buscar("prod3")
    self.compra.agregar(producto1)
    self.compra.agregar(producto2)
    self.compra.agregar(producto3)
    result=self.compra.subtotal()
    self.assertEqual(35,result)

  def testObtenerSubTotalProductosReturn0(self):
    result=self.compra.subtotal()
    self.assertEqual(0,result)
  
  def testSubtotalDescuentosSinProductosLanzaErrorCompraNoTieneProductosError(self):
    self.assertRaises(CompraNoTieneProductosError,self.compra.subtotalDescuentos)
  
  def testSubtotalDescuentosUnProductoEntoncesRetornaTotalProductoSinDescuento(self):
    producto=self.stock.buscar("prod1")
    self.compra.agregar(producto)
    result=self.compra.subtotalDescuentos()
    self.assertEqual(0,result)
  
  def testSubtotalDescuentosUnProductoConDescuentoRetornaTotal(self):
    producto=self.stock.buscar("prod2")
    self.compra.agregar(producto)
    result=self.compra.subtotalDescuentos()
    self.assertEqual(5*10/100,result)

  def testSubtotalDescuentosDosProductoConDescuentoRetornaTotal(self):
    descuento=(5*10/100) + (20*55/100)
    producto2=self.stock.buscar("prod2")
    producto3=self.stock.buscar("prod3")
    self.compra.agregar(producto2)
    self.compra.agregar(producto3)
    result=self.compra.subtotalDescuentos()
    self.assertEqual(descuento,result)
  
  def testSubtotalDescuentosTresProductoConDescuentoRetornaTotal(self):
    descuento=(5*10/100) + (20*55/100)
    producto2=self.stock.buscar("prod2")
    producto3=self.stock.buscar("prod3")
    producto1=self.stock.buscar("prod1")
    self.compra.agregar(producto2)
    self.compra.agregar(producto1)
    self.compra.agregar(producto3)
    result=self.compra.subtotalDescuentos()
    self.assertEqual(descuento,result)


