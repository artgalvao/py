import math
import sys

print('ENCERRAR PROGRAMA; Digite 0')
print('')
print('Numero de Arestas de um poligono; Digite 1')
print('Numero de Vertices de um poligono; Digite 2')
print('')
print('Area de um paralelepipedo; Digite 3')
print('Volume de um paralelepipedo; Digite 4')
print('')
print('Area de um prisma trapezoidal; Digite 5')
print('Volume de um prisma trapezoidal; Digite 6')
print('')
print('Area de um prisma com base de um triangulo retangulo; Digite 7')
va = int(input('::'))

if va == 0:
  sys.exit()
elif va == 1 :
  V = float(input('Vertices: '))
  F = float(input('Faces: '))
  A = 2 - F + V
  print(f'**Aresta : {A}')
elif va == 2:
  A = float(input('Arestas: '))
  F = float(input('Faces: '))
  V = 2 - F + A
  print(f'**Vertices = {V}')
elif va == 3:
  pL1 = float(input('(Base) 1o lado: '))
  pL2 = float(input('(Base) 2o lado: '))
  pH = float(input('(Prisma) Altura: '))
  pLr = (pL1 * pL2) * 2
  pLr1 = pL1 * pH
  pLr2 = pL2 * pH
  pAT = pLr + ((pLr1 * 2) + (pLr2 * 2))
  print(f'**Area total do prisma: {pAT}')
elif va == 4:
  vh = float(input('Altura: '))
  vc = float(input('Comprimento: '))
  vl = float(input('Largura: '))
  vr = vh * vc * vl
  print(f'**Volume total do prisma: {vr}')
elif va == 5:
  ap1 = float(input('(Base) Base Maior: '))
  ap2 = float(input('(Base) Base menor: '))
  ap3 = float(input('(Base) Altura do trapezio: '))
  apr = 1/2 * ( ap1 + ap2 ) * ap3
  apa = float(input('(Prisma) Altura do prisma: '))
  apa0 = float(input('(Prisma) Largura da face: '))
  ap = (2 * apr) + (apa * apa0)
  print(f'**Area do Trapezio: {apr}')
  print(f'**Area total do prisma: {ap}')
elif va == 6:
  ba1 = float(input('(Base) Base maior:'))
  ba2 = float(input('(Base) Base menor:'))
  h1 = float(input('(Base) Altura do trapezio: '))
  att0 = 1/2 * ( ba1 + ba2 ) * h1
  h2 = float(input('(Prisma) Altura do prisma: '))
  att = h2 * att0
  print(f'** Volume total do prisma: {att}')
  print(f'**   Area   do   trapezio: {att0}')
else:
  c1 = float(input('(Base) 1o Cateto: '))
  c2 = float(input('(Base) 2o Cateto: '))
  h = float(input('(Prisma) Altura: '))
  l = float(input('(Prisma) Largura: '))
  a = (2 * ((c1 * c2) / 2)) + (h * l)
  print(f'**Area total do prisma: {a}')