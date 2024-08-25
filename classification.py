import pandas as pd
import os

FILE_PATH = './DATA.csv'
df = pd.read_csv(FILE_PATH)

def classificar_chave_novo(row):
    estilo = row['estilo-vinho'].lower()

    if estilo == 'leve':
        return 'Calor'
    elif estilo == 'aromático':
        return 'Calor'
    elif estilo == 'doce':
        return 'Calor'
    elif estilo == 'fresco':
        return 'Calor'
    elif estilo == 'leve a médio':
        return 'Calor, Versátil'
    elif estilo == 'médio':
        return 'Versátil'
    elif estilo == 'médio a encorpado':
        return 'Versátil, Frio'
    elif estilo == 'encorpado':
        return 'Frio'
    else:
        return 'Outro'

df['chave'] = df.apply(classificar_chave_novo, axis=1)

OUTPUT_PATH_UPDATED = './DOWNLOADS/arquivo_atualizado.csv'

os.makedirs(os.path.dirname(OUTPUT_PATH_UPDATED), exist_ok=True)

df.to_csv(OUTPUT_PATH_UPDATED, index=False)

print("Arquivo processado e salvo em:", OUTPUT_PATH_UPDATED)
