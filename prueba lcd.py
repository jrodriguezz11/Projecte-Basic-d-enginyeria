import i2clcd
class Puzzle1: 
	def __init__(selflcd):
		selflcd.lcd = i2clcd.i2clcd(i2c_bus=1, i2c_addr= 0x27, lcd_width= 20)
		selflcd.lcd.init()
	def Llegirinput(selflcd):
		text = input("Cal ingresar un string: ")
		while(len(text)>80): 
			print("Has posat mes caracters dels que pots, reescriu un altre string ")
			text= input ("Escriu un altre string: ")
		return text
	
	def Imprimir(selflcd, text):
		i=0
		linea=1
		while(i!=len(text)):
			if len(text)-i>20:
				selflcd.lcd.print_line(text[i:(linea*20)], linea-1, 'CENTER')
				i=i+20
				linea=linea+1
			else:
				selflcd.lcd.print_line(text[i:len(text)], linea-1, 'CENTER')
				i=len(text)
				linea=linea+1
	def Main(selflcd):
		selflcd.__init__()
		text= selflcd.Llegirinput()
		selflcd.Imprimir(text)

prova = Puzzle1()
prova.Main()
