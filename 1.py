# -*- coding: utf-8 -*-

import os
from sys import argv
import xml.etree.ElementTree as xml

if (len(argv) == 1):
    print('Не было передано аргументов!')
    exit

sourcePath = argv[1][7::]
destinationPath = argv[2][8::]

if (not os.path.isfile(sourcePath)):
    print("Не удалось открыть файл-источник, такого файла нет!")
    exit()

else:
    source = open(sourcePath, 'r')
    edges = []
    for x in source.read().split(sep='), '):
        edges.append(x[1:].split(sep=', '))

    edgesAmount = len(edges)
    edges[edgesAmount - 1][2] = edges[edgesAmount - 1][2][:-1:]

    for i in range(0, edgesAmount - 1):
        edge1 = edges[i]
        for edge2 in edges:
            if edge1 != edge2:
                if edge1[1] == edge2[1] and edge1[2] == edge2[2]:
                    print("Ошибка формата! Строка:", i + 1)
                    exit()

    edges.sort(key=lambda i: (i[1], i[2]))

    vertexList = []
    for i in range(edgesAmount):
        vertexList.append(edges[i][0])
        vertexList.append(edges[i][1])
    vertexList.sort()
    uniqueVertexList = []
    for x in vertexList:
        if x not in uniqueVertexList:
            uniqueVertexList.append(x)

    graph = xml.Element("graph")

    for i in uniqueVertexList:
        vertex = xml.SubElement(graph, "vertex")
        vertex.text = i

    for i in edges:
        arc = xml.SubElement(graph, "arc")
        fromValue = xml.SubElement(arc, "from")
        fromValue.text = i[0]
        toValue = xml.SubElement(arc, "to")
        toValue.text = i[1]
        orderValue = xml.SubElement(arc, "order")
        orderValue.text = i[2]

    tree = xml.ElementTree(graph)
    tree.write(destinationPath)