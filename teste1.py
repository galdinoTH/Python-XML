#!/usr/bin/python
#coding:utf-8

from xml.dom.minidom import Document

doc = Document()

#<pais>
root = doc.createElement('pais')
sp = doc.createElement('estado')
rj = doc.createElement('estado')
frm = doc.createElement('Cidade')
fcr = doc.createElement('Cidade')
jund = doc.createElement('Cidade')

#Setei os atr das minhas tags
root.setAttribute('nome', 'Brasil')
sp.setAttribute('nome', 'São Paulo')
rj.setAttribute('nome', 'Rio de Janeiro')
frm.setAttribute('nome', 'Francisco Morato')
fcr.setAttribute('nome', 'Franco da Rocha')
jund.setAttribute('nome', 'Jundiai')

doc.appendChild(root)#ponto de partida
root.appendChild(sp)
root.appendChild(rj)
sp.appendChild(frm)
sp.appendChild(fcr)
sp.appendChild(jund)

#Criar habitantes em São Paulo
habf = doc.createElement('habitantes')
habfc = doc.createElement('habitantes')
habjund = doc.createElement('habitantes')
frm.appendChild(habf)
fcr.appendChild(habfc)
jund.appendChild(habjund)

txtf = doc.createTextNode('320.000')
txtfc = doc.createTextNode('280.000')
txtjund = doc.createTextNode('200.000')

habf.appendChild(txtf)
habfc.appendChild(txtfc)
habjund.appendChild(txtjund)

#Escrever xml
doc.writexml(open('test1.xml', 'w'),
             addindent='  ', newl='\n')

#limpar memoria
doc.unlink()