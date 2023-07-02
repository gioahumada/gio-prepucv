import pygame as py
import threading
import random
from pygame import time as pytime  

class Boton(py.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x,y):
        self.imagen_normal=imagen1
        self.imagen_seleccion=imagen2
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)
        
    def update(self,pantalla,cursor,Texto,x,y,valor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal
        
        pantalla.blit(self.imagen_actual,self.rect)
        pantalla.blit(Texto,(x,y))
class Cursor(py.Rect):
    def __init__(self):
        py.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top=py.mouse.get_pos()
def aud_inicio():
        pytime.wait(2000)
        sound = py.mixer.Sound("imagenes/tema1.ogg")
        sound.play()
        pytime.wait(1500)
        sound = py.mixer.Sound("imagenes/jugar.ogg")
        sound.play()
        pytime.wait(1500)
        sound = py.mixer.Sound("imagenes/instrucciones.ogg")
        sound.play()
        pytime.wait(1500)
        sound = py.mixer.Sound("imagenes/autores2.ogg")
        sound.play()
        pytime.wait(1500)
        sound = py.mixer.Sound("imagenes/salir.ogg")
        sound.play()
def audio(foo):
    if foo == 'a':
        aud_inicio()
    elif foo == 'b':
        pytime.wait(1000)
        sound = py.mixer.Sound("imagenes/autores.ogg")
        sound.play()
        pytime.wait(14500)
        sound = py.mixer.Sound("imagenes/salir.ogg")
        sound.play()
    elif foo == 'c':
        pytime.wait(1000)
        sound = py.mixer.Sound("imagenes/instrucciones2.ogg")
        sound.play()
        pytime.wait(14500)
        sound = py.mixer.Sound("imagenes/salir.ogg")
        sound.play()
def audio_preguntas(foo):
    if foo == 'a':
        aud_inicio()
    elif foo == 'b':
        pytime.wait(1000)
        sound = py.mixer.Sound("imagenes/autores.ogg")
        sound.play()
    elif foo == 'c':
        pytime.wait(1000)
        sound = py.mixer.Sound("imagenes/instrucciones2.ogg")
        sound.play()
def preguntas():
    pregunta1=["Cual es la abreviatura de kilometro","A: kl","B: klm","C: km","D: kmt",3,"imagenes/pregunta1.ogg"]
    pregunta2=["Quien salio de la lampara de Aladino","A: Un genio","B: Un principe","C: Una bruja","D: Un sapo",1,"imagenes/pregunta2.ogg"]
    pregunta3=["La antena de radio sirve para","A: Adornar el radio","B: Mejorar la senial","C: Regular la corriente","D: Eliminar el ruido",2,"imagenes/pregunta3.ogg"]
    pregunta4=["Cual es el simbolo quimico del aluminio","A: Ao","B: Am","C: Lm","D: Al",4,"imagenes/pregunta4.ogg"]
    pregunta5=["Las gotas heladas que caen en algunas tormentas se les llama","A: Granizo","B: Nieve","C: Lluvia","D: Rocio",1,"imagenes/pregunta5.ogg"]
    pregunta6=["De que color es una senial de Pare","A: verde y azul","B: rojo y blanco","C: amarillo y negro","D: rosa y verde",2,"imagenes/pregunta6.ogg"]
    pregunta7=["Cual de estos animales es un reptil","A: Cocodrilos","B: Serpientes","C: Lagartos","D: Todos",4,"imagenes/pregunta7.ogg"]
    pregunta8=["Cual de estas piedras es de color verde","A: Rubi","B: Topacio","C: Zafiro","D: Esmaraldas",4,"imagenes/pregunta8.ogg"]
    pregunta9=["Para que el pan se fermente o crezca debe llevar","A: Levadura","B: Agua","C: Uvas","D: Amor",1,"imagenes/pregunta9.ogg"]
    pregunta10=["Este perro es el mas alto de todos ellos. Tiene un pelaje delgado.","A: Lobero Irlandes","B: Gran danes","C: Deerhound Escoces","D: San Bernardo",1,"imagenes/pregunta10.ogg"]
    pregunta11=["El protagonita de este espectaculo tiene un abuelo llamado Lou","A: Los padrinos magicos","B: Doug","C: Rugrats","D: Clarissa lo explica todo",3,"imagenes/pregunta11.ogg"]
    pregunta12=["Cual es el continente mas grande del mundo","A: Asia","B: Europa","C: Africa","D: America",1,"imagenes/pregunta12.ogg"]
    pregunta13=["Cual es la forma completa de la abreviatura GMT","A: Greenwich Mean Time","B: Greenland Mean time","C: German Mean Time","D: Gippsland Mean Time",1,"imagenes/pregunta13.ogg"]
    pregunta14=["Cual es el oceano en el que llega el caudal del rio amazonas","A: El Artico","B: El indio","C: El Atlantico","D: El Pacifico",3,"imagenes/pregunta14.ogg"]
    pregunta15=["Cual es el aparato que facilita la refrigeracion en una nevera","A: Congelador","B: Barillas metalicas","C: Tener la puerta cerrada","D: Compresor",4,"imagenes/pregunta15.ogg"]
    pregunta16=["Cuantos jugadores conforman un equipo de voleibol en la cancha","A: 10","B: 5","C: 6","D: 4",3,"imagenes/pregunta16.ogg"]
    pregunta17=["En matematicas, diez milimetros son...","A: Un poquito","B: Un metro","C: Un decimetro","D: Un centimetro",4,"imagenes/pregunta17.ogg"]
    pregunta18=["Cuantos segundos tiene un minuto y medio","A: 45","B: 90","C: 60","D: 75",2,"imagenes/pregunta18.ogg"]
    pregunta19=["Los delfines son animales de sangre...","A: Caliente","B: Fria","C: Azul","D: Gris",1,"imagenes/pregunta19.ogg"]
    lista=[pregunta1,pregunta2,pregunta3,pregunta4,pregunta5,pregunta6,pregunta7,pregunta8,pregunta9,pregunta10,pregunta11,pregunta12,pregunta13,pregunta14,pregunta15,pregunta16,pregunta17,pregunta18,pregunta19]
    return lista   
def worker():
    py.mixer_music.load("imagenes/millonario.ogg")
    py.mixer_music.play(3000)
    py.mixer.music.set_volume(0.6)          
def ganancia():
    lista=[100,200,300,500,1000,2000,4000,8000,16000,32000,64000,125000,250000,500000,1000000]
    return lista
def imagen_autores(pantalla, cursor1,texto4):
    val="0"
    fondo = py.image.load("imagenes/fondo2.jpg")
    pantalla.blit(fondo,(220,60))
    fuente2=py.font.SysFont("Comic Sans MS", 16, True, False)
    blanco=(255,255,255)
    valor1=py.image.load("imagenes/remarcado.gif")
    valor2=py.image.load("imagenes/remarcado2.gif")
    boton5=Boton(valor1,valor2,260,415)
    Atext1 = fuente2.render("  QUIEN SABE, SABE!! HA SIDO CREADO POR :",1, blanco)
    Atext2 = fuente2.render("      TANIA SANCHEZ Y MARLON LOAYZA ",1, blanco) 
    Atext3 = fuente2.render("     COMO PROYECTO DE LA MATERIA DE :",1,blanco) 
    Atext4 = fuente2.render("          LENGUAJES DE PROGRAMACION",1,blanco)
    Atext5 = fuente2.render("             ESTE JUEGO FUE BASADO :", 1, blanco)
    Atext6 = fuente2.render("EN EL JUEGO QUIEN QUIERE SER MILLONARIO",1,blanco)
    Atext7 = fuente2.render("     http://analizame.com/test_millonario.php", 1, blanco)
    
    pantalla.blit(Atext1,(230,100))
    pantalla.blit(Atext2,(230,140))
    pantalla.blit(Atext3,(230,180))
    pantalla.blit(Atext4,(230,220))
    pantalla.blit(Atext5,(230,260))
    pantalla.blit(Atext6,(230,300))
    pantalla.blit(Atext7,(230,340))
    salir=False
    #LOOP PRINCIPAL
    while salir!=True:
        cursor1.update()
        boton5.update(pantalla,cursor1,texto4,345,415,"1")
        py.display.update()
        if val=="0":
            val="1"
            audio("b") 
        for event in py.event.get():
        # si el evento es del tipo 
        # pygame.QUIT( cruz de la ventana)
            if event.type == py.QUIT:
                salir=True
                py.mixer.stop()
            if event.type == py.KEYDOWN:
                if event.unicode == "s":
                    salir=True
                    py.mixer.stop()
            if event.type == py.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton5.rect):
                    salir=True
                    py.mixer.stop()
def imagen_instrucciones(pantalla, cursor1, texto4):
    fondo = py.image.load("imagenes/fondo2.jpg")
    val="0"
    pantalla.blit(fondo,(220,60))
    fuente2=py.font.SysFont("Comic Sans MS", 16, True, False)
    blanco=(255,255,255)
    valor1=py.image.load("imagenes/remarcado.gif")
    valor2=py.image.load("imagenes/remarcado2.gif")
    boton5=Boton(valor1,valor2,260,425)
    Atext1 = fuente2.render("  INSTRUCCIONES",1, blanco)
    Atext2 = fuente2.render("1.- Este es un juego de preguntas, donde",1, blanco) 
    Atext3 = fuente2.render("    tendras que elegir entre cuatro opciones.",1,blanco) 
    Atext4 = fuente2.render("2.- Para llegar al final, debes contestar",1,blanco)
    Atext5 = fuente2.render("    quince preguntas seguida sin equivocarte.", 1, blanco)
    Atext6 = fuente2.render("3.- Repetir el asistente pulse r",1,blanco)
    Atext7 = fuente2.render("4. Atravez de cada tres preguntas el dinero", 1, blanco)
    Atext8 = fuente2.render("   obtenido quedara asegurado", 1, blanco)
    
    pantalla.blit(Atext1,(230,100))
    pantalla.blit(Atext2,(230,140))
    pantalla.blit(Atext3,(230,180))
    pantalla.blit(Atext4,(230,220))
    pantalla.blit(Atext5,(230,260))
    pantalla.blit(Atext6,(230,300))
    pantalla.blit(Atext7,(230,340))
    pantalla.blit(Atext8,(230,380))
    salir=False
    
    #LOOP PRINCIPAL
    while salir!=True:
        cursor1.update()
        boton5.update(pantalla,cursor1,texto4,345,435,"1")
        py.display.update()
        if val=="0":
            val="1"
            audio("c")  
        for event in py.event.get():
        # si el evento es del tipo 
        # pygame.QUIT( cruz de la ventana)
            if event.type == py.QUIT:
                salir=True
                py.mixer.stop()
            if event.type == py.KEYDOWN:
                if event.unicode == "s":
                    salir=True
                    py.mixer.stop()
            if event.type == py.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton5.rect):
                    salir=True
                    py.mixer.stop()
def imagen_jugar(pantalla, cursor1):
    reloj1= py.time.Clock()
    reloj=20
    precio2=0
    cont1=0
    precio=""
    gan= ganancia()
    fondo = py.image.load("imagenes/pregunta.jpg")
    parche= py.image.load("imagenes/parche.gif")
    pantalla.blit(fondo,(0,0))
    fuente2=py.font.SysFont("Comic Sans MS", 16, True, False)
    blanco=(255,255,255)
    valor1=py.image.load("imagenes/remarcado.gif")
    valor2=py.image.load("imagenes/remarcado2.gif")
    lista=preguntas()
    temp=19
    fuente1=py.font.SysFont("Comic Sans MS", 34, True, False)
    jboton1=Boton(valor1,valor2,46,421)
    jboton2=Boton(valor1,valor2,422,421)
    jboton3=Boton(valor1,valor2,46,496)
    jboton4=Boton(valor1,valor2,424,496)
    reloj1.tick(20)
    salir=False
    
    #LOOP PRINCIPAL
    while salir!=True:
        
        for event in py.event.get():
        # si el evento es del tipo 
        # pygame.QUIT( cruz de la ventana)
            if event.type == py.QUIT:
                salir=True
            if event.type == py.KEYDOWN:
                if event.unicode == "s":
                    salir=True
        if temp==1:
            salir=True
                        
        aleatorio = random.choice(range(temp))
        temp=temp-1
        preg=lista.pop(aleatorio)
        cursor1.update()
        pantalla.blit(fondo,(0,0))
        pantalla.blit(parche,(115,280))
        Atext =  fuente2.render(preg[0],1, blanco)
        Atext1 = fuente2.render(preg[1],1, blanco)
        Atext2 = fuente2.render(preg[2],1, blanco) 
        Atext3 = fuente2.render(preg[3],1,blanco) 
        Atext4 = fuente2.render(preg[4],1,blanco)
        precio= "Tu Score: "+str(precio2)
        precio_cont= fuente1.render(precio,1,blanco)
        pantalla.blit(precio_cont,(400,40))
        pantalla.blit(Atext,(80,300))
        jboton1.update(pantalla,cursor1,Atext1,65,430,"1")
        jboton2.update(pantalla,cursor1,Atext2,450,430,"1")
        jboton3.update(pantalla,cursor1,Atext3,65,508,"1")
        jboton4.update(pantalla,cursor1,Atext4,450,508,"1")
        py.display.update()
        sound = py.mixer.Sound(preg[6])
        sound.play()
        salir2=False
        resp=False
        py.time.set_timer(1,0)
        #LOOP PRINCIPAL
        while salir2!=True:
            
            for event2 in py.event.get():
        # si el evento es del tipo 
        # pygame.QUIT( cruz de la ventana)
                if event2.type == py.QUIT:
                    salir2=True
                    py.mixer.stop()
                if event2.type == py.KEYDOWN:
                    if event2.unicode == "s":
                        salir2=True
                        py.mixer.stop()
                    if event2.unicode == "a":
                        salir2=True
                        py.mixer.stop()
                        if preg[5]==1:
                            resp= True
                            sound = py.mixer.Sound("imagenes/acertas.ogg")
                            sound.play()
                            pytime.wait(1000)
                        else:
                            resp= False
                            sound = py.mixer.Sound("imagenes/perdistes.ogg")
                            sound.play()
                    if event2.unicode == "b":
                        salir2=True
                        py.mixer.stop()
                        if preg[5]==2:
                            resp= True
                            sound = py.mixer.Sound("imagenes/acertas.ogg")
                            sound.play()
                            pytime.wait(1000)
                        else:
                            resp= False
                            sound = py.mixer.Sound("imagenes/perdistes.ogg")
                            sound.play()
                    if event2.unicode == "c":
                        salir2=True
                        py.mixer.stop()
                        if preg[5]==3:
                            resp= True
                            sound = py.mixer.Sound("imagenes/acertas.ogg")
                            sound.play()
                            pytime.wait(1000)
                        else:
                            resp= False
                            sound = py.mixer.Sound("imagenes/perdistes.ogg")
                            sound.play()
                    if event2.unicode == "d":
                        salir2=True
                        py.mixer.stop()
                        if preg[5]==4:
                            resp= True
                            sound = py.mixer.Sound("imagenes/acertas.ogg")
                            sound.play()
                            pytime.wait(1000)
                        else:
                            resp= False
                            sound = py.mixer.Sound("imagenes/perdistes.ogg")
                            sound.play()
                if event2.type == py.MOUSEBUTTONDOWN:
                    if cursor1.colliderect(jboton1.rect):
                        salir2=True
                        py.mixer.stop()
                        if preg[5]==1:
                            resp= True
                            sound = py.mixer.Sound("imagenes/acertas.ogg")
                            sound.play()
                            pytime.wait(1000)
                        else:
                            resp= False
                            sound = py.mixer.Sound("imagenes/perdistes.ogg")
                            sound.play()
                    if cursor1.colliderect(jboton2.rect):
                        salir2=True
                        py.mixer.stop()
                        if preg[5]==2:
                            resp= True
                            sound = py.mixer.Sound("imagenes/acertas.ogg")
                            sound.play()
                            pytime.wait(1000)
                        else:
                            resp= False
                            sound = py.mixer.Sound("imagenes/perdistes.ogg")
                            sound.play() 
                    if cursor1.colliderect(jboton3.rect):
                        salir2=True
                        py.mixer.stop()
                        if preg[5]==3:
                            resp= True
                            sound = py.mixer.Sound("imagenes/acertas.ogg")
                            sound.play()
                            pytime.wait(1000)
                        else:
                            resp= False
                            sound = py.mixer.Sound("imagenes/perdistes.ogg")
                            sound.play()
                    if cursor1.colliderect(jboton4.rect):
                        salir2=True
                        py.mixer.stop()
                        if preg[5]==4:
                            resp= True
                            sound = py.mixer.Sound("imagenes/acertas.ogg")
                            sound.play()
                            pytime.wait(1000)
                            
                        else:
                            resp= False
                            sound = py.mixer.Sound("imagenes/perdistes.ogg")
                            sound.play()
                        
            cursor1.update()
            pantalla.blit(fondo,(0,0))
            pantalla.blit(parche,(115,280))
            pantalla.blit(precio_cont,(530,40))
            pantalla.blit(Atext,(80,300))
            jboton1.update(pantalla,cursor1,Atext1,65,430,"1")
            jboton2.update(pantalla,cursor1,Atext2,450,430,"1")
            jboton3.update(pantalla,cursor1,Atext3,65,508,"1")
            jboton4.update(pantalla,cursor1,Atext4,450,508,"1")
            reloj=(py.time.get_ticks()/1000)
            reloj= str(reloj)
            contador= fuente1.render("Tiempo: "+reloj,1,blanco)
            pantalla.blit(contador,(40,40))
            py.display.update()
        if resp == True:
            cont1=cont1+1
            precio2=gan[cont1]
        else: 
            salir=True
def main():
    
    py.init() # inicializo el modulo
    pytime.wait(500)
    t = threading.Thread(target=worker, name='audio')
    t.start()
    val="0"
    pantalla=py.display.set_mode((833,559))
    py.display.set_caption("Quien Sabe, Sabe!!!") # Titulo de la Ventana
    icon = py.image.load("imagenes/espol.gif")
    fondo = py.image.load("imagenes/fondo.jpg")
    valor1=py.image.load("imagenes/remarcado.gif")
    valor2=py.image.load("imagenes/remarcado2.gif")
    boton1=Boton(valor1,valor2,28,410)
    boton2=Boton(valor1,valor2,444,410)
    boton3=Boton(valor1,valor2,444,495)
    boton4=Boton(valor1,valor2,28,495)
    cursor1=Cursor()
    fuente1=py.font.SysFont("Comic Sans MS", 34, True, False)
    py.display.set_icon(icon)
    blanco=(255,255,255)
    texto1 = fuente1.render("         Jugar", 1, blanco)
    texto2 = fuente1.render("    Instrucciones", 1, blanco)
    texto3 = fuente1.render("        Autores", 1, blanco)
    texto4 = fuente1.render("         Salir", 1, blanco)
    texto5 = fuente1.render("    Salir", 1, blanco)
    salir=False
    
    #LOOP PRINCIPAL
    while salir!=True:
        #recorro todos los eventos producidos
        #en realidad es una lista
        pantalla.blit(fondo,(0,0))
        cursor1.update()
        boton1.update(pantalla,cursor1,texto1,28,415,"1")
        boton2.update(pantalla,cursor1,texto2,444,415,"2")
        boton3.update(pantalla,cursor1,texto4,444,500,"3")
        boton4.update(pantalla,cursor1,texto3,28,500,"4")
        py.display.update() #actualizo el display
            
        for event in py.event.get():
            # si el evento es del tipo 
            # pygame.QUIT( cruz de la ventana)
            if event.type == py.QUIT:
                salir=True
                py.mixer.stop()
            if event.type == py.KEYDOWN:
                if event.unicode == "s":
                    py.quit()
                    py.mixer.stop()
                if event.unicode == "j":
                    py.mixer.stop()
                    imagen_jugar(pantalla,cursor1)
                if event.unicode == "a":
                    py.mixer.stop()
                    imagen_autores(pantalla,cursor1,texto5)
                if event.unicode == "i":
                    py.mixer.stop()
                    imagen_instrucciones(pantalla,cursor1,texto5)
            if event.type == py.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton3.rect):
                    py.mixer.stop()
                    py.quit()   
            if event.type == py.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton2.rect):
                    py.mixer.stop()
                    imagen_instrucciones(pantalla,cursor1,texto5)
            if event.type == py.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton4.rect):
                    py.mixer.stop()
                    imagen_autores(pantalla,cursor1,texto5)
            if event.type == py.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    py.mixer.stop()
                    imagen_jugar(pantalla,cursor1)
        if val=="0":
            val="1"
            audio("a")   
    py.quit()
    
main() 