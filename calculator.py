from tkinter import *
from tkinter import ttk


cor1 = "#000000"
cor2 = "#7110CC"
cor3 = "#C1CDCD"
cor4 = "#0000FF"
cor5 = "2332DB"


janela = Tk()
janela.title('Calculadora')
janela.geometry('235x318')
janela.config(background= cor1)


## criando frames da calculadora ( parte de estilo)
frame_da_tela = Frame (janela, width=235, height = 50, bg= cor4)
frame_da_tela.grid(row = 0, column = 0)

frame_corpo = Frame(janela, width=235, height= 318)
frame_corpo.grid(row = 1, column = 0)

todos_valores = ''
def entrar_valor(bot2):
    global todos_valores

    todos_valores = todos_valores + str(bot2)



    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

def media ():
    global valor_media
    try:
        valores = valor_media.split(',')  # Divide os valores separados por vírgula
        valores = [float(valor.strip()) for valor in valores]  # Converte para floats

        if valores:
            resultado = sum(valores) / len(valores)
            valor_texto.set(str(resultado))
        else:
            valor_texto.set("N/D")
    except:
        valor_texto.set("N/D")

def limpar():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")




valor_texto = StringVar()
app_label = Label(frame_da_tela, textvariable= valor_texto , width=15, height=2, padx= 7, relief= FLAT, anchor= "e", justify= RIGHT, font= ('Ivy 18'))
app_label.place(x=0, y=0)

#criando bototes

bot1= Button(frame_corpo, command= limpar, text= "C", width= 6, height=2, bg= cor3, font= "bold")
bot1.place(x= 0, y=0)
bot2= Button(frame_corpo, command= lambda: entrar_valor('/'), text= "/", width= 7, height=2, bg= cor3)
bot2.place(x= 90, y=0)
bot3= Button(frame_corpo, command= lambda: entrar_valor('%') ,text= "%", width= 7, height=2, bg= cor3)
bot3.place(x= 177, y=0)
bot4= Button(frame_corpo,  command= lambda: entrar_valor('7'),text= "7", width= 7, height=2, bg= cor3)
bot4.place(x= 0, y=52)
bot5= Button(frame_corpo,  command= lambda: entrar_valor('8'), text= "8", width= 7, height=2, bg= cor3)
bot5.place(x= 59, y=52)
bot6= Button(frame_corpo,  command= lambda: entrar_valor('9'),text= "9", width= 7, height=2, bg= cor3)
bot6.place(x= 118, y=52)
bot7= Button(frame_corpo,  command= lambda: entrar_valor('*'), text= "*", width= 7, height=2, bg= cor3)
bot7.place(x= 177, y=52)
bot8= Button(frame_corpo,  command= lambda: entrar_valor('4'), text= "4", width= 7, height=2, bg= cor3)
bot8.place(x= 0, y=104)
bot9= Button(frame_corpo, command= lambda: entrar_valor('5'), text= "5", width= 7, height=2, bg= cor3)
bot9.place(x= 59, y=104)
bot10= Button(frame_corpo,  command= lambda: entrar_valor('6'), text= "6", width= 7, height=2, bg= cor3)
bot10.place(x= 118, y=104)
bot11= Button(frame_corpo,  command= lambda: entrar_valor('-'),text= "-", width= 7, height=2, bg= cor3)
bot11.place(x= 177, y=104)
bot12= Button(frame_corpo,  command= lambda: entrar_valor('1'),  text= "1", width= 7, height=2, bg= cor3)
bot12.place(x= 0, y=156)
bot13= Button(frame_corpo, command= lambda: entrar_valor('2'), text= "2", width= 7, height=2, bg= cor3)
bot13.place(x= 59, y=156)
bot14= Button(frame_corpo,  command= lambda: entrar_valor('3'),text= "3", width= 7, height=2, bg= cor3)
bot14.place(x= 118, y=156)
bot15= Button(frame_corpo,  command= lambda: entrar_valor('+'),text= "+", width= 7, height=2, bg= cor3)
bot15.place(x= 177, y=156)
bot16= Button(frame_corpo, command= lambda: entrar_valor('0'), text= "0", width= 7, height=2, bg= cor3)
bot16.place(x= 0, y=208)
bot17= Button(frame_corpo,  command= lambda: entrar_valor(','), text= ",", width= 7, height=2, bg= cor3)
bot17.place(x= 59, y=208)
bot18= Button(frame_corpo,  command= calcular,text= "=", width= 7, height=2, bg= cor3)
bot18.place(x= 118, y=208)
bot19= Button(frame_corpo, command= media, text= "m", width= 7, height=2, bg= cor3)
bot19.place(x= 177, y=208)








janela.mainloop()