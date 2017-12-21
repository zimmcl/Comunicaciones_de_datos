# TP1: Capa de Aplicación

**Objetivos:** Comprender el funcionamiento del protocolo de la capa de aplicación HTTP y aprender comandos básicos de la consola de linux.

**Bibliografía:** Computer Networking de Kurose y Ross, Capítulo 1 y 2

Instrucciones para la instalación del Software:
1. Descargar e instalar wireshark de la [página oficial](https://www.wireshark.org/);
2. Instalar y descargar netcat para linux con el comando _"sudo apt-get install netcat"_. Para usuarios de Windows 10, seguir el tutorial para instalar bash en Windows de [aquí](https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows
-10/). Una vez que se puede utilizar bash, también ejecutar _"sudo apt-get install netcat"_;
3. Descargar e instalar la última versión de virtual box de la [página oficial](https://www.virtualbox.org/);
4. Descargar ubuntu server 16.04.3 LTS de la [página](https://www.ubuntu.com/download/server);
5. Instalar ubuntu server en una máquina virtual: alcanzan los 10gb de espacio de disco que el virtual box propone y 1GB de memoria. (Si tienen problemas con este paso, entren a la BIOS de su máquina y aseguren que esté habilitada la virtualización);
6. Una vez instalado el ubuntu server, ingresar con usuario y contraseña y ejecutar los siguientes comandos: _"sudo apt install python-pip"_. Cuando termine el proceso de instalación, ejecutar _"pip install flask"_. Apagar la máquina con el comando _"sudo shutdown now"_;
7. en la parte de configuración de la máquina virtual, vayan a Red (network), adaptador 1 y cambien lo que dice NAT a adaptador puente (bridged adapter).


Puede continuar con la actividad propuesta en clase, acceda al siguiente enlace [TP1](wiki/Demo.md).

# TP2: 

1. Fork or copy [this repository](https://github.com/drassil/git-wiki)

2. copy and rename _config.yml.dist in _config.yml changing settings inside

3. create your index.md in root directory

4. push your changes in your repository, then configure the github pages in your repository settings

5. Your wiki is ready!

**Note:**

We suggest the creation of a /wiki/ subfolder that collects all your .md pages (except index.md)

# TP3: 

* Non-existent wiki page links are not "[red](wiki/red.md)".

* You can't use the wiki link format: [[example]]. Please, use gh-pages links instead: \[example\](example) 

# TP4: 

You can create following files in _includes folder to costumize git-wiki without patching original code:

* head.html  -> this file will be included in <head> tag allowing you to add css/js and any kind of head tags
* sidebar.html -> this file will be included in left sidebar allowing you to create your widgets
* comments.html -> this is mostly used to integrate social comments under page contents
* footer.html -> this file will be included in left side of the footer.

# TP5: 

Do you like this project? then, contact us via [chat](https://gitter.im/Drassil/general?utm_source=share-link&utm_medium=link&utm_campaign=share-link) , <a href="mailto:staff-drassil@googlegroups.com">email</a>  or send us a PR to improve it.

Thank you!

# TP6: 

- [jekyll-table-of-contents](https://github.com/ghiculescu/jekyll-table-of-contents)

- [jQuery](https://jquery.com/)


[MIT LICENSE](LICENSE)

# TP7:
