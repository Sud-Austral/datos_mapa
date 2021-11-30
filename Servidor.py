import ee
import geemap
import pandas as pd



if __name__ == '__main__':
    print('Iniciado proceso...')
    studyArea = ee.FeatureCollection("users/APP_DATA_I/limites/CHL_regiones_sim")
    print('Proceso finalizado.')