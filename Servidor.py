import ee
import geemap
import pandas as pd



if __name__ == '__main__':
    print('Iniciado proceso...')
    #service_account = 'foo-project@appspot.gserviceaccount.com'
    #credentials = ee.ServiceAccountCredentials(service_account, 'secret.json')
    #ee.Initialize(credentials)
    from google.auth import compute_engine
    import ee
    credentials = compute_engine.Credentials(scopes=['https://www.googleapis.com/auth/earthengine'])
    ee.Initialize(credentials)
    studyArea = ee.FeatureCollection("users/APP_DATA_I/limites/CHL_regiones_sim")
    print('Proceso finalizado.')