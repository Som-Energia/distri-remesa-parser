#!/usr/bin/env python
# -*- coding: utf-8 -*-
import StringIO
import csv
import sys

class CSVParser:
    def __init__(self):
        pass

    def loadCSV(self, file_name):
        with open(file_name, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                self.invoice_list.append(row)
    
    def loadList(self, invoice_list):
        self.invoice_list = invoice_list

    def parseUFD(self):
        i = 0
        dist_line = []
        while i<len(self.invoice_list):
            if len(self.invoice_list[i]) == 4:
                dist_line.append([self.invoice_list[i][1],self.invoice_list[i][3]])
            i += 1
        return dist_line[1:]

