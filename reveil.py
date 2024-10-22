import datetime
import time
import winsound # permet d'accéder au mecanisme du son fourni par Windows 
from tkinter import * # module integré à la bibliothéque standard de python qui permet de creer des interface graphiques

    
def alarm(heure_definie):
    while True:
        time.sleep(1) # la prochaine instruction s'execute apres 1 seconde 
        heure_actuele = datetime.datetime.now().strftime("%H:%M:%S")
        date = datetime.datetime.now().strftime("%d:%m:%Y")
        print(date,heure_actuele)

        if(heure_actuele == heure_definie):
             print("C'est l'heure de se reveiller !! ")
             winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
             break
        
def heure_actuel():
      heure_definie = f"{hour.get()}:{minute.get()}:{seconde.get()}"
      alarm(heure_definie)    

# creation de l'interface graphique
alarme = Tk()

alarme.title("Horloge")
alarme.geometry("400x200")  
alarme.iconbitmap("alarme.ico")



# ajouter les etiquettes
Label(alarme,text="Alarm",font=("Helvetica 20 bold"),fg="red").pack()
Label(alarme,text="Definir l'heure",font=("Helvetica 15 bold")).pack()
# conteneur cadre
frame = Frame(alarme)
frame.pack()
hour = StringVar(alarme)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
        )
hour.set(hours[0])
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(alarme)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0]) 
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

seconde = StringVar(alarme)
secondes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
seconde.set(secondes[0])
sec = OptionMenu(frame, seconde, *secondes)
sec.pack(side=LEFT)

Button(alarme,text="Enregistrer",font=("Helvetica 15"),command= heure_actuel ).pack(pady=20)


alarme.mainloop()

    
    