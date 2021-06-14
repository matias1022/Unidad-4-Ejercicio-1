from tkinter import *
from tkinter import ttk,font,messagebox
import tkinter as tk
class Aplicacion():
    __ventana=None
    __peso=None
    __altura=None
    __re1=None
    __re2=None
    def __init__(self) -> None:
        '''VENTANA'''
        self.__ventana=Tk()
        ancho_ventana = 500
        alto_ventana = 300

        x_ventana = self.__ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.__ventana.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        
        self.__ventana.geometry(posicion)
        self.__ventana.resizable(0,0)
        self.__ventana.title('\t\tCalculadora de IMC')
        '''FUENTES'''
        self.fuente1= font.Font(family='Arial', size=10,weight='bold')
        self.fuente2 = font.Font(family='Arial', size=10)
        self.fuente3 = font.Font(family='Arial', size=17)
        '''TEXTOS'''
        self.marco=tk.Frame(self.__ventana,bg='white') #FONDO BLANCO
        self.titulo=tk.Label(self.__ventana,text='Calculadora de IMC',font=self.fuente1,bg='light gray')
        self.alturaLbl=ttk.Label(self.__ventana,text='Altura: ',padding=(5,5),background='white')
        self.pesoLbl=ttk.Label(self.__ventana,text='Peso: ',padding=(5,5),background='white')
        self.cmLbl=tk.Label(self.__ventana,text='cm',bg='light gray')
        self.kgLbl=tk.Label(self.__ventana,text='kg',bg='light gray')
        self.__altura=StringVar()
        self.__peso=StringVar()
        self.__re1=StringVar()
        self.__re2=StringVar()
        '''ENTRYS'''
        self.entryA=ttk.Entry(self.__ventana,textvariable=self.__altura)
        self.entryP=ttk.Entry(self.__ventana,textvariable=self.__peso)
        '''SEPARADORES'''
        self.separ1 = ttk.Separator(self.__ventana, orient=HORIZONTAL)
        self.separ2 = ttk.Separator(self.__ventana, orient=HORIZONTAL)
        self.separ3 = ttk.Separator(self.__ventana, orient=HORIZONTAL)
        '''BOTONES'''
        self.boton1 =tk.Button(self.__ventana,text='Calcular',font=self.fuente1,bg='lime green',border=0.25,fg='white',command=self.calcular)
        self.boton2 =tk.Button(self.__ventana,text='Limpiar',font=self.fuente1,bg='lime green',border=0.25,fg='white',command=self.limpiar)
        '''RECUADRO RESULTADOS'''
        self.resultados=tk.Frame(self.__ventana,bg='white')
        self.resultado1=tk.Label(self.resultados,bg='white',fg='white',text='Tu Indice de Masa Corporal (IMC) es',font=self.fuente2)
        self.resultado2=tk.Label(self.resultados,bg='white',fg='white',textvariable=self.__re1,font=self.fuente1)
        self.resultado3=tk.Label(self.resultados,bg='white',fg='white',textvariable=self.__re2,font=self.fuente3)
        
        '''POSICION TEXTOS'''
        self.alturaLbl.place(x=0,y=60)
        self.pesoLbl.place(x=0,y=130)
        self.cmLbl.place(x=465,y=62,height=25,width=30)
        self.kgLbl.place(x=465,y=132,height=25,width=30)
        self.titulo.place(relwidth=1,height=40,anchor=tk.N + tk.W)
        self.marco.place(x=0,y=0,width=500,height=300)

        '''POSICION ENTRYS'''
        self.entryA.place(x=50,y=62,height=25,width=415)
        self.entryP.place(x=50,y=132,height=25,width=415)
        '''POSICION SEPARADORES'''
        self.separ1.place(relx=0.5,y=50,anchor=tk.N,bordermode=OUTSIDE, relwidth=0.95)
        self.separ2.place(relx=0.5,y=125,anchor=tk.N,bordermode=OUTSIDE, relwidth=0.95)
        self.separ3.place(relx=0.5,y=170,anchor=tk.N,bordermode=OUTSIDE, relwidth=0.95)
        '''POSICION BOTONES'''
        self.boton1.place(relx=0.25,y=175,width=175,height=30,anchor=tk.N)
        self.boton2.place(relx=0.75,y=175,width=175,height=30,anchor=tk.N)
        '''POSICION RESULTADOS'''
        self.resultados.place(relx=0.5,y=215,anchor=tk.N,relwidth=0.61,height=70)
        self.resultado1.place(x=2,y=10)
        self.resultado2.place(relx=0.9999999999,y=10,anchor=tk.N + tk.E)
        self.resultado3.place(relx=0.5,rely=0.95,anchor=tk.S)
        self.__ventana.mainloop()
    
    def calcular(self, *args):
        if self.entryA.get()!='' and self.entryP.get()!='':
            try:
                imc=float(float(self.entryP.get()) / (((float(self.entryA.get()))/100)**2))
                self.resultados['bg']='#D0EBC7'     #COLOREA EL RECUADRO YA QUE ESTABA EN BLANCO
                self.resultado1['bg']='#D0EBC7'     #COLOREA LAS FUENTES YA QUE ESTABA EN BLANCO
                self.resultado1['fg']='#41763D'
                self.resultado2['bg']='#D0EBC7'
                self.resultado2['fg']='#41763D'
                self.__re1.set('{:.2f} Kg/m2'.format(imc))
                if imc<18.5:
                    self.__re2.set('Peso inferior al normal')
                elif imc>=18.5 and imc<25:
                    self.__re2.set('Peso Normal')
                elif imc>=25.0 and imc<30:
                    self.__re2.set('Peso superior al normal')
                elif imc>=30:
                    self.__re2.set('Obesidad')
                self.resultado3['bg']='#D0EBC7'
                self.resultado3['fg']='#41763D'
            except ValueError:
                messagebox.showerror(title='Error de tipo',
                message='Debe ingresar un valor numérico')
                self.__peso.set('')
                self.__altura.set('')
                self.entryA.focus()
        else:
            messagebox.showerror(title='Error de tipo',
            message='Debe completar los campos')
            self.__peso.set('')
            self.__altura.set('')
            self.entryA.focus()

    def limpiar(self):
        self.resultados['bg']='white'
        self.resultado1['bg']='white'
        self.resultado1['fg']='white'
        self.resultado2['bg']='white'
        self.resultado2['fg']='white'
        self.resultado3['bg']='white'
        self.resultado3['fg']='white'
        self.__re1.set('')
        self.__re2.set('')
        self.__peso.set('')
        self.__altura.set('')
        self.entryA.focus()
        self.entryA.focus()

