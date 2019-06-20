#!/usr/bin/env python
# -*- coding: utf-8 -*-
import StringIO
import sys
import pandas as pd

class XLSParser:
    def __init__(self):
        pass

    def loadList(self, invoice_list):
        self.invoice_list = invoice_list

    def procesFile(self, file_name):
        xl = pd.ExcelFile(file_name)
        if len(xl.sheet_names) < 2:
            self.parseIberdrola(xl) 
        elif filter(lambda x: 'Facturacion' in x, [xl.sheet_names[1]]):
            self.parseEndesa(xl)
        else:
            raise Exception("File don't match with any suported")

    def parseEndesa(self, xl):
        df1 = xl.parse(xl.sheet_names[1])
        df_obj = df1.select_dtypes(['object'])
        df1[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())
        df1 = df1.iloc[:-2]
        df1.to_csv(path_or_buf='output_endesa.csv', sep=';', columns=['Codigo_Fiscal_de_Factura','Importe_Total_de_la_Factura'], header=False, index=False, decimal=',')

    def parseIberdrola(self, xl):
        df1 = xl.parse()
        df1.to_csv(path_or_buf='output_iberdrola.csv', sep=';', columns=['NUMFACTRUA','IMPORTE EUR'], header=False, index=False, decimal=',')