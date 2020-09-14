#!/usr/bin/python3
import sys
import io
import cgi
import pandas as pd
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
# -*- coding: utf-8 -*-
print("content-type: text/html; charset=utf-8\n")

df = pd.read_csv('/opt/lampstack-7.4.9-0/apache2/htdocs/data/total_disease2.csv', encoding='CP949')
print(df[0:1]['subject'])
