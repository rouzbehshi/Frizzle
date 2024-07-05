import pandas as pd
import numpy as np
import pytz
from astral import LocationInfo
from astral.sun import sun

class DataProcessingPipeline:
    def __init__(self, df, variable, latitude, longitude, start_date='2005-01-01', end_date='2020-12-31'):
        self.df = df
        self.variable = variable
        self.latitude = latitude
        self.longitude = longitude
        self.start_date = start_date
        self.end_date = end_date
        self.daily_averages = None
        self.input_data = []
        self.output_label = []

    @staticmethod
    def calculate_sunrise_sunset(latitude, longitude, date):
        location = LocationInfo(latitude=latitude, longitude=longitude)
        timezone = pytz.timezone('Europe/Rome')
        s = sun(location.observer, date=date, tzinfo=timezone)
        sunrise = s['sunrise'].hour + s['sunrise'].minute / 60
        sunset = s['sunset'].hour + s['sunset'].minute / 60
        return sunrise, sunset

    def filter_data(self):
        self.df_filtered = self.df.loc[self.start_date:self.end_date]

    def calculate_daily_averages(self):
        self.daily_averages = self.df_filtered.resample('D').mean()

    def add_sunrise_sunset_times(self):
        unique_dates = self.daily_averages.index.date
        sun_times = [self.calculate_sunrise_sunset(self.latitude, self.longitude, date) for date in unique_dates]
        sun_times_df = pd.DataFrame(sun_times, columns=['sunrise', 'sunset'], index=unique_dates)
        sun_times_df.index.name = 'date'

        self.daily_averages['date'] = self.daily_averages.index.date
        self.daily_averages = self.daily_averages.merge(sun_times_df, left_on='date', right_index=True, how='left')
        self.daily_averages.drop(columns=['date'], inplace=True)

    def process_input_output(self):
        for i in range(len(self.daily_averages)):
            daily_avg = self.daily_averages.iloc[i]
            hourly_values = self.df_filtered[self.variable][i*24:(i+1)*24]
            if len(hourly_values) == 24:
                self.input_data.append(daily_avg.values)
                self.output_label.append(hourly_values.values)

    def split_data(self, test_year=2020):
        input_data = np.array(self.input_data)
        output_label = np.array(self.output_label)

        mask_train = self.daily_averages.index.year < test_year
        mask_test = self.daily_averages.index.year == test_year

        X_train = input_data[mask_train]
        y_train = output_label[mask_train]

        X_test = input_data[mask_test]
        y_test = output_label[mask_test]

        mask_leap_year = self.daily_averages.index.dayofyear != 366
        X_train = X_train[mask_leap_year[mask_train]]
        y_train = y_train[mask_leap_year[mask_train]]
        X_test = X_test[mask_leap_year[mask_test]]
        y_test = y_test[mask_leap_year[mask_test]]

        return X_train, y_train, X_test, y_test

    def run_pipeline(self):
        self.filter_data()
        self.calculate_daily_averages()
        self.add_sunrise_sunset_times()
        self.process_input_output()
        return self.split_data()