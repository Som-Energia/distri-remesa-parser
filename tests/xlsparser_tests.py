#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from distriremesaparser import xlsparser
import csv


class TestXLSParser(unittest.TestCase):

    def fromCSVtoList(self, file_name):
        invoice_list = []
        with open(file_name, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=str(';'))
            for row in reader:
                invoice_list.append(row)
        return invoice_list
    
    def test__procesFile__IberdrolaAllOk(self):
        p = xlsparser.XLSParser()

        p.procesFile('./tests/data/test_iberdrola.xlsx')

        result = self.fromCSVtoList('output_iberdrola.csv')
        self.assertEqual([['100000000000000001', '342,82'],
            ['100000000000000002', '343,82'],
            ['100000000000000003', '344,82'],
            ['100000000000000004', '345,82']], result)

    def test__procesFile__EndesaAllOk(self):
        p = xlsparser.XLSParser()

        p.procesFile('./tests/data/test_endesa.xlsx')

        result = self.fromCSVtoList('output_endesa.csv')
        self.assertEqual([['F3901N00000008', '26,24'],
            ['F3901N00000009', '27,88'],
            ['F3901N00000010', '21,71'],
            ['F3901N00000011', '30,25'],
            ['F3901N00000012', '25,31']], result)

    def test__procesFile__EndesaColumnErr(self):
        p = xlsparser.XLSParser()

        with self.assertRaises(Exception): p.procesFile('./tests/data/test_endesa_err_columname.xlsx')

    def test__procesFile__IberdrolaColumnErr(self):
        p = xlsparser.XLSParser()

        with self.assertRaises(Exception): p.procesFile('./tests/data/test_iberdrola_err_columname.xlsx')

    def test__procesFile__EndesaSheetErr(self):
        p = xlsparser.XLSParser()

        with self.assertRaises(Exception): p.procesFile('./tests/data/test_endesa_err_sheetname.xlsx')


if __name__ == '__main__':
    unittest.main(verbosity=2)

# vim: et ts=4 sw=4
