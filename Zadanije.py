# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 17:12:47 2020

@author: user
"""

class isik:
   
    def __init__(self,x,y,z,c):
        self.tarkus = x
        self.iseloom = y
        self.vanus = z
        self.sugu = c
        
    def display(self):
        print('tarkus: {} \niseloom: {} \nvanus: {} \nsugu: {}'.format(self.tarkus, self.iseloom, self.vanus, self.sugu))
        
    def bark(self):
        print(self.tarkus, 'üldse ei hakkanud meiega rääkima ja läks ära.')
        
    def bark2(self):
        print('Soovin teile õnne, ütles', self.sugu, 'ja vaatas meid ilusate silmadega.')
        
    def bark3(self):
        print('Mina olen targem, kui kõik teie koos, ütles', self.tarkus, 'ja keeras ringi.')
        
    def bark4(self):
        print('Mina olen loll, ütles', self.tarkus, 'ja hakkas naerma')
        
 
print('Это первый человек, он очень умный!')
print()
    
firstisik=isik('Tark', 'liiga uhke', 25, 'bisex')
firstisik.display()
firstisik.bark()

print()
print('Второй, конечно, не такой умный, за то красивый.')
print('')

secondisik=isik('keskmine', 'väga lahe', 30, 'naine')
secondisik.display()
secondisik.bark2()

print()
print('Этот глуповатый, но самоуверенный.')
print('')

isik3=isik('rumal', 'enesekindel', 30, 'mees')
isik3.display()
isik3.bark3()

print()
print('Ну а этот вообще дурак!')
print('')

isik4=isik('täitsa loll', 'puudub', 45, 'tuvastamine on rasketud')
isik4.display()
isik4.bark4()

print('')
print("Мне просто удобнее было писать в коде на латинице, неудобно переключать клавиатуру.", " ", "Спасибо за внимание и с Рождеством Вас!")