#! /usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from distriremesaparser import csvparser

class TestCSVParser(unittest.TestCase):
    def test__parseUFD__allOk(self):
        csv_file = [['FECHA','Nº FACTURA','C.U.P.S.','IMPORTE'],
                    ['01/01/2019', 'J419000000000', 'ES0022000000000000NE1P', '23,09'],
                    ['01/01/2019', 'J419000000001', 'ES0022000000000000NE1P', '53,09'], ] 
        p = csvparser.CSVParser()
        p.loadList(csv_file)

        result = p.parseUFD()

        self.assertEqual([['J419000000000', '23,09'], ['J419000000001', '53,09']], result)

    def test__parseERP__allOk(self):
        csv_file = [["J419000000000","57.91","No trobada"]]
        p = csvparser.CSVParser()
        p.loadList(csv_file)

        result = p.parseERP()

        self.assertEqual([['J419000000000', '57,91']], result)

    def test__procesFile__UFDAllOk(self):
        csv_file = [['\xef\xbb\xbfRELACI\xc3\x93N DE RECIBOS INCLUIDOS EN UN APUNTE \xc3\x9aNICO para XXXX en fecha 01/01/2019'], [],
                ['CLIENTE: F00000000-XXXX'], ['SOCIEDAD: 0703-UFD DISTRIBUCI\xc3\x93N ELECTRICIDAD, S.A.'],
                ['C\xc3\x93DIGO APUNTE \xc3\x9aNICO: 99999'], ['TIPO: REMESAS COBROS'], ['N\xc2\xba DE DOCUMENTOS: 99'],
                ['IMPORTE TOTAL: 23,09'], [], ['FECHA', 'N\xc2\xba FACTURA', 'C.U.P.S.', 'IMPORTE'],
                ['01/01/2019', 'J419000000000', 'ES0022000000000000NE1P', '23,09']]
        p = csvparser.CSVParser()
        p.loadList(csv_file)

        result = p.procesFile()

        self.assertEqual([['J419000000000', '23,09']], result)
