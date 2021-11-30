import ee
import geemap
import pandas as pd



if __name__ == '__main__':
    print('Iniciado proceso...')
    #service_account = 'foo-project@appspot.gserviceaccount.com'
    service_account = '722158313283-gem3r97no94a7fgdchjaj11qanhv3i2p.apps.googleusercontent.com'    
    credentials = ee.ServiceAccountCredentials(service_account, 'secret.json')
    ee.Initialize(credentials)

    studyArea = ee.FeatureCollection("users/APP_DATA_I/limites/CHL_regiones_sim")
    print('Proceso finalizado.')