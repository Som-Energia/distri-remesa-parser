#!/usr/bin/env python
# -*- coding: utf-8 -*-
import StringIO
import csv
import sys

class CSVParser:
    def __init__(self):
        self.invoice_list = []

    def loadCSV(self, file_name):
        with open(file_name, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                self.invoice_list.append(row)
    
    def loadList(self, invoice_list):
        self.invoice_list = invoice_list

    def procesFile(self):
        if not self.invoice_list:
            raise Exception("No invoice loaded. Please, load an invoice list or a file before use procesFile")
        i = 0
        while i<len(self.invoice_list):
            if filter(lambda x: 'SOCIEDAD: 0703-UFD' in x, self.invoice_list[i]):
                return self.parseUFD()
            if filter(lambda x: 'No trobada' in x, self.invoice_list[i]):
                return self.parseERP()
            i += 1

    def parseUFD(self):
        i = 0
        dist_line = []
        while i<len(self.invoice_list):
            if len(self.invoice_list[i]) == 4:
                dist_line.append([self.invoice_list[i][1],self.invoice_list[i][3]])
            i += 1
        return dist_line[1:]

    def parseERP(self):
        i = 0
        dist_line = []
        while i<len(self.invoice_list):
            if len(self.invoice_list[i]) == 3:
                dist_line.append([self.invoice_list[i][0],self.invoice_list[i][1].replace('.',',')])
            i += 1
        return dist_line
# vim: et ts=4 sw=4
