from pathlib import Path
import pandas as pd

#FOLDER SETTING
DATA_FOLDER = Path('data')
ANNOTATION_FILE = DATA_FOLDER / 'annotation_master_latest.csv'
FEATURE_FILE    = DATA_FOLDER / 'feature_master_latest.csv'
MERGED_FILE     = DATA_FOLDER / 'lux_data.csv'

DATA_FOLDER.mkdir(exist_ok=True)

#show string
def text_show(text):
    print('=' * 80)
    print(text)
    print('=' * 80)

text_show('...Lux Data Load...')

#Load_Annotation_CSV
annotation = pd.read_csv(ANNOTATION_FILE)
text_show('Annotation Data Loaded')
print(f'Annotation Shape : {annotation.shape}')

#Load_Feature_CSV
feature = pd.read_csv(FEATURE_FILE)
text_show('Feature Data Loaded')
print(f'Feature Shape : {feature.shape}')

#Merge_On_filename(Join Key)
df = feature.copy()
text_show('Using Feature Master as Main Dataset')
print(f'Merged Shape : {df.shape}')

#Save_Merged_Data
df.to_csv(MERGED_FILE, index=False)
text_show('Data Saved to lux_data.csv')
print()
