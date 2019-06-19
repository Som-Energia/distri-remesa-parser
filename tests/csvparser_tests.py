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
