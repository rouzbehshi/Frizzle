from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LeakyReLU
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.regularizers import l2
from tensorflow.keras.optimizers.legacy import Adam

from DataProcessing import DataProcessingPipeline
from DataCleaning import DataCleaningPipeline

# DataCleaningPipeline Parameters
path = ('data/data.csv')

# DataProcessingPipeline Parameters
variable = 'Gd(i)'
latitude = 40.5112  # Latitude of the specific location
longitude = 16.3723  # Longitude of the specific location

# Data Cleaning Pipeline
pipeline_cleaning = DataCleaningPipeline(path)
df = pipeline_cleaning.run_pipeline()

# Data Processing Pipeline
pipeline_processing = DataProcessingPipeline(df, variable, latitude, longitude)
X_train, y_train, X_test, y_test = pipeline_processing.run_pipeline()

# Parameters
window_size = 365  # Number of samples in each training window
step_size = 180  # Number of samples to move the window by each iteration

# Total number of windows
total_windows = (len(X_train) - window_size) // step_size + 1


# ANN Model
def build_model(input_shape):
    model = Sequential([
        Dense(60, activation=LeakyReLU(), input_shape=(input_shape,),
              kernel_regularizer=l2(0.01)),
        Dense(24)
    ])
    model.compile(optimizer=Adam(), loss='mae')
    return model


# Rolling window
for window_start in range(0, total_windows * step_size, step_size):
    train_end = window_start + window_size
    if train_end > len(X_train):
        break

    # Split the dataset for this window
    X_train_window, y_train_window = X_train[window_start:train_end], y_train[window_start:train_end]

    # Build the model
    model = build_model(X_train_window.shape[1])
    early_stopping = EarlyStopping(monitor='val_loss', patience=40, restore_best_weights=True, mode='min')
    # Fit the model
    model.fit(X_train_window, y_train_window, batch_size=10, epochs=3000, verbose=1, validation_split=0.1,
              callbacks=[early_stopping])

print(f"Training of {variable} model is finished.")

model.save('Windf')

#%%
