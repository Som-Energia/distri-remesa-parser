#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from six.moves import StringIO
import sys
import pandas as pd

class XLSParser:
    def __init__(self):
        pass

    def loadList(self, invoice_list):
        self.invoice_list = invoice_list

    def procesFile(self, file_name, output_name=None):
        xl = pd.ExcelFile(file_name)
        if len(xl.sheet_names) < 2:
            self.parseIberdrola(xl, output_name) 
        elif list(filter(lambda x: 'Facturacion' in x, [xl.sheet_names[1]])):
            self.parseEndesa(xl, output_name)
        else:
            raise Exception("File don't match with any suported")

    def parseEndesa(self, xl, output_name=None):
        if not output_name:
            output_name = 'output_endesa.csv'
        df1 = xl.parse(xl.sheet_names[1])
        df_obj = df1.select_dtypes(['object'])
        df1[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())
        df1 = df1.iloc[:-2]
        if 'Codigo_Fiscal_de_Factura' in df1 and 'Importe_Total_de_la_Factura' in df1:
            df1.to_csv(path_or_buf=output_name, sep=str(';'), columns=['Codigo_Fiscal_de_Factura','Importe_Total_de_la_Factura'], header=False, index=False, decimal=',')
        else:
            raise Exception("Invalid column names in Endesa Excel")

    def parseIberdrola(self, xl, output_name=None):
        if not output_name:
            output_name='output_iberdrola.csv'
        df1 = xl.parse()
        if 'NUMFACTRUA' in df1 and 'IMPORTE EUR' in df1:
            df1.to_csv(path_or_buf=output_name, sep=str(';'), columns=['NUMFACTRUA','IMPORTE EUR'], header=False, index=False, decimal=',')
        else:
            raise Exception("Invalid column names in Iberdrola Excel")

# vim: et ts=4 sw=4
