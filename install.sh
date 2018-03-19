#!/usr/bin/bash

ROOT_UID=0

function webhackinstall() {
	if [ -f /etc/debian_version ] ; then
		echo -e "Procediendo con la instalación en tu sistema Debian o basado en Debian."
		mkdir /opt/webhackshl/
		cp -R * /opt/webhackshl/
		echo -e "\n#!/usr/bin/bash\npython /opt/webhackshl/webhackshl.py" | sudo tee -a /usr/bin/webhackshl > /dev/null
		chmod +x /usr/bin/webhackshl
		echo -e "Instalación finalizada, ahora puedes ejecutar el comando "webhackshl" directamente desde tu terminal.\n"

	elif [ -f /etc/arch-release ] ; then
		echo -e "Procediendo con la instalación en tu sistema ArchLinux o basado en ArchLinux.\n"
		mkdir /opt/webhackshl/
		cp -R * /opt/webhackshl/
		echo -e "\n#!/usr/bin/bash\npython2 /opt/webhackshl/webhackshl.py" | sudo tee -a /usr/bin/webhackshl > /dev/null
		chmod +x /usr/bin/webhackshl
		echo -e "Instalación finalizada, ahora puedes ejecutar el comando "webhackshl" directamente desde tu terminal.\n"
	else
		echo -e "\nSistema no identificado, saliendo."
		exit
	fi
}

if [ "$UID" -ne "$ROOT_UID" ]; then
	esroot=false
	echo "Necesitas tener privilegios root o sudo para la instalación, saliendo..."
else
	esroot=true
    webhackinstall
fi

