import pandas as pd

class DataCleaningPipeline:
    def __init__(self, path):
        self.path = path

    def reading_data(self):
        df = pd.read_csv(self.path)
        df['time'] = df['time'].str.replace(' UTC', '', regex=False)
        df['time'] = pd.to_datetime(df['time'], utc=True)

        df= df.set_index('time')
        df = df.tz_convert('Europe/Rome')
        df.index = df.index.tz_convert('Europe/Rome').tz_localize(None)
        row_to_copy = df.loc['2005-01-01 01:00:00']
        row_to_duplicate = pd.DataFrame(row_to_copy).transpose()
        row_to_duplicate.index = pd.to_datetime(['2005-01-01 00:00:00'])
        df = pd.concat([row_to_duplicate, df]).sort_index()
        df['Avg_Temp'] = (df['temp_min']+df['temp_max'])/2
        df_filtered = df.drop(columns=['pressure', 'temp_min', 'temp_max', 'Gb(i)'])

        return df_filtered

    def run_pipeline(self):
        return self.reading_data()