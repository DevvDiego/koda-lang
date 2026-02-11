# koda-lang

### Aplicaciones
El proyecto tiene dos aplicaciones, una es la **interfaz web** y la otra es el **compilador**.
Para probar el proyecto yo recomiendo trabajar parte por parte. Es decir, ejecutar solo el lexer, parser y similares dentro de algun archivo que no dependa enteramente del flujo de trabajo de la aplicacion entera.

---

### Instalacion
Genera tu venv
**Windows/Linux**
```bash
python -m venv .venv
```

Despues inicializa el entorno virtual para instalar dentro las dependencias

**Windows**
```bash
.\.venv\Scripts\activate
```

**Linux (Debian)**
```bash
source .venv/bin/activate
```

Por ultimo ejecuta
```bash
pip install -r requirements.txt
```

Y listo, ya tienes las dependencias instaladas dentro de tu entorno virtual!

**Nota extra:** Si VsCode no reconoce los paquetes importados probablemente sea que esta usando el interprete global y no el de tu virtual enviroment (venv).

Prueba a ejecutar ``` Ctrl + shift + p -> Python: Select Interpreter``` y eliges el que tenga el "(.venv)" señalado.

---

### Ejecucion
**Antes de empezar**, recuerda activar el **venv** para que python identifique las dependencias del entorno y no se confunda si es que ya las tienes instaladas.

Para ver la interfaz del proyecto, levanta el servidor de Flask utilizando el siguiente comando: 
```bash
python app.py
```