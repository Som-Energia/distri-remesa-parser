#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from six.moves import StringIO
import csv
import sys

class CSVParser:
    def __init__(self):
        self.invoice_list = []

    def loadCSV(self, file_name):
        with open(file_name, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=str(';'))
            for row in reader:
                self.invoice_list.append(row)
    
    def loadList(self, invoice_list):
        self.invoice_list = invoice_list

    def procesFile(self, input_name=None, output_name=None):
        records = []
        if input_name:
            self.loadCSV(input_name)

        if not output_name:
            output_name = '/tmp/output.csv'

        if not self.invoice_list:
            raise Exception("No invoice loaded. Please, load an invoice list or a file before use procesFile")
        i = 0
        while i < len(self.invoice_list):
            if list(filter(lambda x: 'SOCIEDAD: 0703-UFD' in x, self.invoice_list[i])):
                records = self.parseUFD()
                break
            if list(filter(lambda x: 'No trobada' in x, self.invoice_list[i])):
                records = self.parseERP()
                break
            if len(self.invoice_list[0]) == 2:
                records = self.invoice_list
            i += 1

        if not records:
            raise Exception("File don't match with any suported")

        with open(output_name, mode='w') as writer_report:
            writer_report = csv.writer(writer_report, delimiter=str(';'))
            for row in records:
                writer_report.writerow(row)

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
