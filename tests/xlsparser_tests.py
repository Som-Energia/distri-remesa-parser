#! /usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from distriremesaparser import xlsparser
import csv

class TestXLSParser(unittest.TestCase):

    def fromCSVtoList(self, file_name):
        invoice_list = []
        with open(file_name, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                invoice_list.append(row)
        return invoice_list
    
    def test__procesFile__IberdrolaAllOk(self):
        p = xlsparser.XLSParser()

        p.procesFile('test_iberdrola.xlsx')

        result = self.fromCSVtoList('output_iberdrola.csv')
        self.assertEqual([['100000000000000001', '342,82'],
            ['100000000000000002', '343,82'],
            ['100000000000000003', '344,82'],
            ['100000000000000004', '345,82']], result)

    def test__procesFile__IberdrolaAllOk(self):
        p = xlsparser.XLSParser()

        p.procesFile('test_endesa.xlsx')

        result = self.fromCSVtoList('output_endesa.csv')
        self.assertEqual([['F3901N00000008', '26,24'],
            ['F3901N00000009', '27,88'],
            ['F3901N00000010', '21,71'],
            ['F3901N00000011', '30,25'],
            ['F3901N00000012', '25,31']], result)
