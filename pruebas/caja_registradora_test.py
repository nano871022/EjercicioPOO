import unittest
from errores.error import ProductoNoEncontradoError
from modelo.stock import Stock
from modelo.producto import Producto
from modelo.caja_registradora import CajaRegistradora 
from errores.error import CompraNoTieneProductosError

class CajaRegistradoraTest(unittest.TestCase):
  def setUp(self):
    self.stock = Stock()
    self.stock.agregar(Producto("prod1",10,0))
    self.stock.agregar(Producto("prod2",5,10))
    self.stock.agregar(Producto("prod3",20,55))
    self.cajaRegistradora = CajaRegistradora(self.stock)
  
  def testCajaRegistradoraNoEncontrarProducto(self):
    producto="noexiste"
    self.assertRaises(ProductoNoEncontradoError,self.cajaRegistradora.agregar,producto)
  
  def testCajaRegistradoraAgregarUnProductoACompraObtenerSubTotal(self):
    producto = "prod1"
    result = self.cajaRegistradora.agregar(producto)
    self.assertEqual(10, result)
  
  def testCajaRegistradoraAgregarTresProductoACompraObtenerSubTotal(self):
    result = self.cajaRegistradora.agregar("prod1")
    result = self.cajaRegistradora.agregar("prod2")
    result = self.cajaRegistradora.agregar("prod3")
    self.assertEqual(35, result)
  
  def testCajaRegistradoraSinProductoEnCompraAlFinalizar(self):
    self.assertRaises(CompraNoTieneProductosError,self.cajaRegistradora.finalizar)

  def testCajaRegistradoraFinalizarObtenerTotal(self):
    self.cajaRegistradora.agregar("prod1")
    self.cajaRegistradora.agregar("prod3")
    subtotal=self.cajaRegistradora.agregar("prod2")
    result=self.cajaRegistradora.finalizar()
    self.assertEqual(10+(5-5*10/100)+(20-20*55/100),result)
    self.assertEqual(35,subtotal)
  
  def testCajaRegistradoraPagarLanzarCompraNoTieneProductosError(self):
    self.assertRaises(CompraNoTieneProductosError,self.cajaRegistradora.pagar,0)
  
  def testCajaRegistradoraPagarRetorna0(self):
    self.cajaRegistradora.agregar("prod1")
    self.cajaRegistradora.agregar("prod3")
    subtotal=self.cajaRegistradora.agregar("prod2")
    total=self.cajaRegistradora.finalizar()
    result=self.cajaRegistradora.pagar(total)
    self.assertEqual(0,result)
    self.assertEqual(10+(5-5*10/100)+(20-20*55/100),total)
    self.assertEqual(10+20+5,subtotal)

  def testCajaRegistradoraPagarMasDinero50(self):
    self.cajaRegistradora.agregar("prod1")
    self.cajaRegistradora.agregar("prod3")
    subtotal=self.cajaRegistradora.agregar("prod2")
    total=self.cajaRegistradora.finalizar()
    result=self.cajaRegistradora.pagar(50)
    self.assertEqual(50-total,result)
    self.assertEqual(10+(5-5*10/100)+(20-20*55/100),total)
    self.assertEqual(10+20+5,subtotal)

def testCajaRegistradoraCerrarCompra(self):
    self.cajaRegistradora.agregar("prod1")
    self.cajaRegistradora.agregar("prod3")
    subtotal=self.cajaRegistradora.agregar("prod2")
    total=self.cajaRegistradora.finalizar()
    devolucion=self.cajaRegistradora.pagar(50)
    self.cajaRegistradora.cerrarCompra()
    total2=self.cajaRegistradora.finalizar()
    self.assertEqual(0,total2)
    self.assertEqual(50-total,devolucion)
    self.assertEqual(10+(5-5*10/100)+(20-20*55/100),total)
    self.assertEqual(10+20+5,subtotal)
  