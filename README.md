
<!-- ----------------------------------------------------------------------- -->

<br>

<div align='center'>

``` ocaml
PLATAFORMA DE ANALISIS PROBABILISTICO PARA LA PREDICCION TEMPRANA DEL CARCINOMA PULMONAR
```

</div>

<br>

<!-- ----------------------------------------------------------------------- -->

<h1 align='center'>
    <a href='https://github.com/lord-of-castamere/Irithyll'>
        <img src='./WEB/statics/images/Siegward.webp' width='25%'
            alt='¿Quién soy yo para juzgar caminos ajenos? Si yo mismo camino como un hombre imperfecto' />
    </a>
</h1>

> **Contexto:** Se busca identificar pacientes propensos a desarrollar cáncer de pulmón, basándose en factores personales y clínicos

<div align='center'>
    <img src='https://img.shields.io/badge/Proyecto-Académico-blue?style=for-the-badge' alt='Tipo de proyecto' />
    <img src='https://img.shields.io/badge/Estado-En%20desarrollo-important?style=for-the-badge' alt='Estado actual' />
    <img src='https://img.shields.io/badge/Dev-Ed%20Rubio-critical?style=for-the-badge' alt='Desarrollador' />
</div>

<br>

<!-- ----------------------------------------------------------------------- -->

<pre align='center'>
    <a href='#estructura'>ESTRUCTURA</a> • <a href='#configuración'>CONFIGURACIÓN</a> • <a href='#avances'>AVANCES</a> • <a href='#agradecimientos'>AGRADECIMIENTOS</a>
</pre>

<br>

<!-- ----------------------------------------------------------------------- -->

## <samp>ESTRUCTURA</samp>
> **Nota:** A continuación se presenta una visión de la organización de carpetas del proyecto.

``` bash
ML ''' Machine Learning. '''
├── Dataset/
│   └── SurveyLungCancer.csv
├── Notebook/
│   └── ...
├── Models/
│   └── ...
└── Requirements.txt
WEB ''' Aplicación WEB '''
├── apps/
│   ├── users/
│   │   ├── ...
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── templates/
│   └── ...
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── statics/
│   ├── css/
│   ├── images/
│   ├── fonts/
│   └── scripts/
├── templates/
│   └── ...
├── manage.py
└── Requirements.txt
```

<br>

<!-- ----------------------------------------------------------------------- -->

## <samp>CONFIGURACIÓN</samp>
> **Nota:** Los siguientes pasos detallan la configuración e inicialización del proyecto desde Windows.

<br>

#### CLONA EL REPOSITORIO
``` bash
# Si deseas clonar el repositorio completo y cambiar entre ramas.

git clone https://github.com/lord-of-castamere/Aldrich.git
git checkout <Nombre de la rama>
```

``` bash
# Si deseas clonar una única rama del repositorio.

git clone --single-branch --branch <Nombre de la rama> https://github.com/lord-of-castamere/Aldrich.git
```

<br>

#### ACTIVA EL ENTORNO VIRTUAL
``` bash
# Tanto ML como WEB tienen su enotorno virtual propio,
# Cada entorno ha de ser creado y activado en su respectiva carpeta.

python -m venv venv
venv\Scripts\Activate
```

``` bash
# Posteriormente, instala las dependecias, igualmente de manera separada en ML y WEB.

pip install -r Requirements.txt
```

<br>

#### INICIA LAS APLICACIONES
``` bash
# Aplicación WEB:
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

# Machine Learning (análisis de datos):
jupyter notebook
```

<br>

<!-- ----------------------------------------------------------------------- -->

## <samp>AVANCES</samp>
Este listado representa el estado de desarrollo del proyecto, de manera sencilla y visual.

<br>

* [x] Pre-procesamiento de datos (Completado)
* [x] Entrenamiento y evaluación de modelos - ML (Completado)
* [ ] Desarrollo de aplicación WEB (En progreso...)

<br>

<!-- ----------------------------------------------------------------------- -->

## <samp>AGRADECIMIENTOS</samp>
Esta sección es un reconocimiento sincero a las personas y entidades que han contribuido significativamente al desarrollo de este proyecto.

* **Mysar Ahmad Bhat:** Por compartir generosamente el *Dataset de Lung Cancer* y hacerlo accesible a la comunidad.
    * **Fuente:** [https://www.kaggle.com/datasets/mysarahmadbhat/lung-cancer](https://www.kaggle.com/datasets/mysarahmadbhat/lung-cancer)

<br>

<!-- ----------------------------------------------------------------------- -->

#### ***- When Aldrich ruminated on the fading of the fire, it inspired visions of a coming age of the deep sea. He knew the path would be arduous, but he had no fear. He would devour the gods himself...***

<!-- ----------------------------------------------------------------------- -->
