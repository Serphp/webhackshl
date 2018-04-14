#!/usr/bin/python2
# encoding: utf-8
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import subprocess
import os
isgzip=os.path.isfile("/usr/bin/gzip") or os.path.isfile("/bin/gzip")
isjohn=os.path.isfile("/usr/bin/john") or os.path.isfile("/usr/sbin/john")
istor=os.path.isfile("/usr/bin/tor")
isrb=os.path.isfile("/usr/bin/ruby")
isnm=os.path.isfile("/usr/bin/nmap")
isfierce=os.path.isfile("/usr/bin/fierce") or os.path.isfile("/usr/bin/fierce.pl")
ismap=os.path.isfile("/usr/bin/sqlmap")
isenum=os.path.isfile("/usr/bin/dnsenum")
isnikto=os.path.isfile("/usr/bin/nikto")
iswhatw=os.path.isfile("/usr/bin/whatweb")
iswp=os.path.isfile("/usr/bin/wpscan")
iscurl=os.path.isfile("/usr/bin/curl")
isgit=os.path.isfile("/usr/bin/git")

def distribucion():
    iskalideb=os.path.isfile("/etc/debian_version") or os.path.isfile("/etc/apt/sources.list")
    isarch=os.path.isfile("/etc/arch-release") or os.path.isfile("/etc/pacman.conf")
    global DISTRO
    if iskalideb:
        print "Usted está usando una distribución basada en Debian!\n"
        DISTRO="kalideb"
    elif isarch:
        print "Usted está usando ArchLinux!\n"
        DISTRO="ArchLinux"
    else:
        print "Distribución Linux desconocida."


def cRojo(prt): print("\033[91m {}\033[00m" .format(prt))
def cVerde(prt): print("\033[92m {}\033[00m" .format(prt))
def cAmarillo(prt): print("\033[93m {}\033[00m" .format(prt))
def cMoradoclaro(prt): print("\033[94m {}\033[00m" .format(prt))
def cMorado(prt): print("\033[95m {}\033[00m" .format(prt))
def cCian(prt): print("\033[96m {}\033[00m" .format(prt))
def cGrisclaro(prt): print("\033[97m {}\033[00m" .format(prt))
def cNegro(prt): print("\033[98m {}\033[00m" .format(prt))

def checkarch():
    global archb
    cCian("verificando si existen los repositorios de BlackArch")
    archb=os.system("cat /etc/pacman.conf | grep 'blackarch'")
    if archb == 0:
        cRojo("Los repositorios de BlackArch Existen")
    else:
        cRojo("Los Repositorios de BlackArch No existen y se añadiran para continuar")
        os.system("sudo echo -e '\n[blackarch]\nSigLevel = Never\nServer = https://www.blackarch.org/blackarch/$repo/os/$arch' | sudo tee -a /etc/pacman.conf")


def checkali():
    cCian("verificando si existen los repositorios de kali-rolling")
    global kalic
    kalic=os.system("cat /etc/apt/sources.list | grep 'deb http://http.kali.org/kali kali-rolling main contrib non-free'")
    if kalic == 0:
        cRojo("Los repositorios de Kali-rolling Existen")
    else:
        cRojo("Los Repositorios de Kali-rolling No existen y se añadiran para continuar")
        os.system("sudo echo -e '\ndeb http://http.kali.org/kali kali-rolling main contrib non-free' | sudo tee -a /etc/apt/sources.list")
        cAmarillo("Importando las claves de GNU/Kali Linux para ejecutar la instalacion...")
        os.system("sudo wget -q -O - archive.kali.org/archive-key.asc | sudo apt-key add")

def updatetools(DISTRO):
    respuesta=raw_input("Introduce tu opcion y=continua con la instalación, n=anula la instalación. y/n: ")
    if respuesta=="y" and DISTRO== "kalideb":
        cAmarillo("Para realizar esta instalación necesitas privilegios root o sudo, por favor introduzca tus credenciales cuando se le soliciten.")
        cAmarillo("Añadiendo el repositorio temporal de Kali a tu lista de repositorios ...")
        print ""
        cAmarillo("Actualizando tu lista de paquetes ...")
        os.system("sudo apt update")
        cAmarillo("actualizando Herramientas del sistema...")
        correctinstall=os.system("sudo apt install nmap fierce sqlmap dnsenum nikto whatweb wpscan ruby ruby-dev git curl tor gzip john python  python-requests  python-yaml  python-flask libc6-dev zlib1g-dev zlib1g && cd modules/tplmap/ && git pull && cd joomlavs/ && git pull")
        if correctinstall==0:
            print ""
            cVerde("La actualizacion se realizo correctamente.")
            cVerde("Todo lo necesario esta actualizado, procediendo.")
        else:
            cVerde("Ha ocurrido un error.")

    elif respuesta=="y" and DISTRO== "ArchLinux":
        cAmarillo("Para realizar esta instalación necesitas privilegios root o sudo, por favor introduzca tus credenciales cuando se le soliciten.")
        print ""
        cAmarillo("Actualizando tu lista de paquetes ...")
        os.system("sudo pacman -Sy")
        cAmarillo("Actualizando Herramientas del sistema...")
        correctinstall=os.system("sudo pacman --needed --asdeps -S nmap fierce sqlmap dnsenum nikto whatweb wpscan ruby git curl tor gzip john python2  python2-requests  python2-yaml  python2-flask && cd modules/tplmap/ && git pull")
        if correctinstall==0:
            print ""
            cVerde("La actualizacion se realizo correctamente.")
            cVerde("Todo lo necesario esta actualizado, procediendo.")
        else:
            cRojo("Ha ocurrido un error.")
    elif respuesta == "n":
        cAmarillo("Actualizacion abortada, saliendo ...")
        os._exit(0)
    else:
        cRojo("Opcion incorrecta.")
        updatetools(DISTRO)

def repokali():
    respuesta=raw_input("Introduce tu opcion y=continua con la instalación, n=anula la instalación. y/n: ")
    if respuesta=="y":
        cAmarillo("Para realizar esta instalación necesitas privilegios root o sudo, por favor introduzca tus credenciales cuando se le soliciten.")
        print ""
        cAmarillo("Actualizando tu lista de paquetes ...")
        os.system("sudo apt update")
        cAmarillo("actualizando Herramientas del sistema...")
        installcorrect=os.system("sudo apt install nmap fierce sqlmap dnsenum nikto whatweb wpscan ruby ruby-dev git curl tor gzip john python  python-requests  python-yaml  python-flask libc6-dev zlib1g-dev zlib1g")
        if installcorrect == 0:
            print ""
            cRojo("La actualizacion se realizo correctamente.")
            cRojo("Todo lo necesario esta actualizado, procediendo.")
        else:
            print "Ha ocurrido un error, intentando nuevamente."
            repokali()
    elif respuesta == "n":
        cAmarillo("Actualizacion abortada, saliendo ...")
        os._exit(0)
    else:
        cRojo("Opcion incorrecta.")
        updatetools(DISTRO)

def repoarch():
    respuesta=raw_input("Introduce tu opcion y=continua con la instalación, n=anula la instalación. y/n: ")
    if respuesta=="y":
        cAmarillo("Para realizar esta instalación necesitas privilegios root o sudo, por favor introduzca tus credenciales cuando se le soliciten.")
        print ""
        cAmarillo("Actualizando tu lista de paquetes ...")
        os.system("sudo pacman -Sy")
        cAmarillo("Actualizando herramientas del sistema...")
        installcorrect=os.system("sudo pacman --needed --asdeps -S nmap fierce sqlmap dnsenum nikto whatweb wpscan ruby git curl tor gzip john python2  python2-requests  python2-yaml  python2-flask")
        if installcorrect == 0:
            print ""
            cRojo("La actualizacion se realizo correctamente.")
            cRojo("Todo lo necesario esta actualizado, procediendo.")
        else: 
            print "Ha ocurrido un error, intentandolo de nuevo."
            repoarch()
    elif respuesta == "n":
        cAmarillo("Actualizacion abortada, saliendo ...")
        os._exit(0)
    else:
        cRojo("Opcion incorrecta.")
        updatetools(DISTRO)

def installall(DISTRO):
    cRojo("""Para que este framework funcione correctamente, necesitas tener instaladas las siguientes herramientas:
    nmap, fierce, sqlmap, dnsenum, nikto, john, gzip, tor, curl, ruby, whatweb & wpscan. Al parecer hay herramientas faltantes en tu sistema!.
    """)
    decision=raw_input("Introduce tu opcion y=continua con la instalación, n=anula la instalación. y/n: ")
    if decision=="y" and DISTRO == "kalideb":
        cRojo("Para realizar esta instalación necesitas privilegios root o sudo, por favor introduzca tus credenciales cuando se le soliciten.")
        print ""
        cAmarillo("Actualizando tu lista de paquetes ...")
        os.system("sudo apt update")
        os.system("clear")
        cAmarillo("Instalando los paquetes ...")
        os.system("sudo apt install nmap fierce sqlmap dnsenum nikto whatweb wpscan ruby ruby-dev git curl tor gzip john python  python-requests  python-yaml  python-flask libc6-dev zlib1g-dev zlib1g")

        print ""
        os.system("clear")
        cVerde("La instalacion se realizo correctamente.")
        cVerde("Todo lo necesario esta instalado, procediendo.")
    elif decision == "y" and DISTRO == "ArchLinux":
        cRojo("Para realizar esta instalación necesitas privilegios root o sudo, por favor introduzca tus credenciales cuando se le soliciten.")
        print ""
        cAmarillo("Actualizando tu lista de paquetes ...")
        os.system("sudo pacman -Sy")
        os.system("clear")
        cAmarillo("Instalando los paquetes ...")
        correctinstall=os.system("sudo pacman --needed --asdeps -S nmap fierce sqlmap dnsenum nikto whatweb wpscan ruby git curl tor gzip john python2  python2-requests  python2-yaml  python2-flask")
        if correctinstall == 0:
            print ""
            os.system("clear")
            cVerde("La instalacion se realizo correctamente.")
            cVerde("Todo lo necesario esta instalado, procediendo.")
        else:
            cRojo("Ha ocurrido un error, intentando de nuevo.")
            installall(DISTRO)
    elif decision == "n":
        print "Instalación abortada, saliendo ..."
        os._exit(0)
    else:
        print "Opcion incorrecta."
        installall(DISTRO)

def check():
    if isnm and isfierce and ismap and isenum and isnikto and iswhatw and iswp and isrb and isgit and iscurl and istor and isgzip and isjohn:
        cVerde("Todo lo necesario esta instalado, procediendo.")
    else:
        distribucion()
        if DISTRO == "kalideb":
            checkali()
            if kalic == 0:
                repokali()
            else:
                installall(DISTRO)
        elif DISTRO == "ArchLinux":
            checkarch()
            if archb == 0:
                repoarch()
            else:
                installall(DISTRO)

def dtor():
    cVerde("Verificando que el servicio TOR esté activo...")
    tor=os.system("systemctl status tor | grep -qw active")
    if tor == 0:
        cVerde("0K - TOR")
        pass
    else:
        cRojo("Necesitas iniciar TOR")
        resp = raw_input("¿Deseas ininiciar el servicio ahora? y/n : ")
        if resp=="y":
            cAmarillo("Iniciando TOR...")
            os.system("sudo systemctl start tor")
            dtor()
        elif resp=="n":
            cRojo("Algunas opciones no funcionaran.")
            pass
        else:
            print "Opción invalida.\n"
            dtor()

def gems():
    os.system("PATH=`ruby -e 'puts Gem.user_dir'`/bin:$PATH")
    cVerde("Verificando que Bundler está en el sistema, esto puede tomar varios minutos la primera vez...")
    gem=os.system("bundle | grep -q 'Bundle complete!'")
    if gem == 0:
        cVerde("0K - Bundler")
        pass
    else:
        def gemsinstall():
            cRojo("""Necesitas instalar Bundler, procediendo a la instalación.
    Bundler es requerido por un escanner de vulnerabilidades, necesitas privilegios root o sudo para instalarlo.
    Esto puede tomar un tiempo.""")
            inst = raw_input("Deseas continuar con la instalación? y/n : ")
            if inst=="y":
                os.system("PATH=`ruby -e 'puts Gem.user_dir'`/bin:$PATH")
                cAmarillo("Instalando bundler...")
                correctgem=os.system("sudo gem install bundler && bundle install")
                if correctgem==0:
                    pass
                else:
                    cRojo("Las gemas no se instalaron correctamente, por favor asegurate de estar dentro de la carpeta de webhackshl. esto traera problemas en la opcion d) del menú usando joomlavs. Continuando...")
                    pass
            elif inst=="n":
                cRojo("Instalacion cancelada, esto traera problemas en la opcion d) del menú usando joomlavs. Continuando...")
                pass
            else:
                print "Opción incorrecta.\n"
                gemsinstall()
        gemsinstall()

def utools():
    distribucion()
    updatetools(DISTRO)
