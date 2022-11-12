#!/usr/bin/python
#coding:utf-8

from xml.dom.minidom import parse

#abriu
doc = parse('test1.xml')

xml = doc.documentElement

if xml.hasAttribute('nome'):
    print('Pais: %s' % xml.getAttribute('nome'))