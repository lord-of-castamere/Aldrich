
# -- VIEWS ------------------------------------------------------------------- #

import joblib
import pandas as pd

from pathlib import Path
from django.views import View
from django.conf import settings
from django.shortcuts import render, redirect

# ---------------------------------------------------------------------------- #

# Ruta base del proyecto:
BASE_DIR = Path(settings.BASE_DIR)

# Ruta hacia el folde que contiene los modelos:
MODELS_PATH = BASE_DIR.parent / 'ML' / 'Models'

try: # Modelo & Scaler:
    model = joblib.load(MODELS_PATH / 'randomForest.joblib')
    scaler = joblib.load(MODELS_PATH / 'standardScaler.joblib')
    print('Modelitos cargados...\n')
except FileNotFoundError:
    print('ERROR: No se han encontrado los archivos del modelo.')
    model = None
    scaler = None

# Nombres de las columnas:
COLUMN_NAMES = [
    'GENDER', 'AGE', 'SMOKING', 'YELLOW_FINGERS', 'ANXIETY',
    'PEER_PRESSURE', 'CHRONIC_DISEASE', 'FATIGUE', 'ALLERGY', 'WHEEZING',
    'ALCOHOL_CONSUMING', 'COUGHING', 'SHORTNESS_OF_BREATH',
    'SWALLOWING_DIFFICULTY', 'CHEST_PAIN'
]

# ---------------------------------------------------------------------------- #

''' VISTA: Predicción... '''
def predict_view(request):
    context = {}
    template = 'testing/home.html'

    if request.method == 'POST':

        # Para evitar errores:
        if not model or not scaler:
            context['result'] = 'ERROR: Los modelos no han podido ser cargados...'
            context['alert_class'] = 'alert-warning'
            return render(request, template, context)

        try: # Si todo está bien, continuamos...
            data_dict = {}
            for col in COLUMN_NAMES:
                data_dict[col] = int(request.POST.get(col))

            # Dado que Pandas espera un DataFrame...
            df = pd.DataFrame([data_dict])
            age_scaled = scaler.transform(df[['AGE']])
            df['AGE'] = age_scaled


            # Iniciamos con la predicción...
            prediction = model.predict(df)[0]
            probability = model.predict_proba(df)[0][1]

            # Formatear el resultado para mostrarlo en el template.
            prob_percent = probability * 100
            context['probability'] = f'{prob_percent:.2f}'


            # En caso de obtener una predicción positiva:
            if prediction == 1:
                context['result'] = 'POSITIVO'
                context['description'] = (
                    'Se han detectado indicios que podrían ser asociados a un mayor riesgo de cáncer de pulmón. '
                    'Cabe aclarar que este **NO es un diagnóstico médico**, sino una señal para considerar una revisión con un especialista. '
                    'Se recomienda acudir con un profesional de la salud para una evaluación más detallada y estudios complementarios.'
                )
                context['alert_class'] = 'alert-positive'

            else: # En caso de obtener una predicción negativa:
                context['result'] = 'NEGATIVO'
                context['description'] = (
                    'No se han identificado señales relevantes asociadas al cáncer de pulmón según los datos analizados. '
                    'Esto sugiere un riesgo bajo, aunque **no descarta completamente la posibilidad**. '
                    'Mantén hábitos saludables y, ante cualquier síntoma o duda, consulta a tu médico de confianza.'
                )
                context['alert_class'] = 'alert-negative'
                
        except Exception as error: # Manejo de errorcillos.
            context['result'] = f'No se ha podido procesar la solicitud: {e}'
            context['alert_class'] = 'alert-negative'

        return render(request, template, context)


    return render(request, template)

# ---------------------------------------------------------------------------- #