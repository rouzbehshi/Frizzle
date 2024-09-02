# Temporal-disaggregation of Regional Climate Models (RCM) with Artificial Neural Networks (ANNs)
# Background
The energy system's growing sensitivity to weather not only amplifies its vulnerability to current climate fluctuations but also suggests that human-induced climate change could alter the patterns and spatial-temporal variability of meteorological factors, thereby influencing both energy supply and demand [1].
As a result, the use of long-term climate data in the planning and operation of power systems is rapidly increasing. Several climate models with fine spatial resolution are available as outputs from Regional Climate Models (RCMs), which provide downscaled data derived from Global Climate Models (GCMs). These models can be incorporated into power system studies to simulate possible future conditions that the systems might encounter. However, these climate models are mainly available with daily resolution due to the limited space of data servers [2]. A higher level of temporal resolution is needed to properly plan and operate power systems by accounting for the intermittent nature of renewable energy sources.


This repository aims to develop a tool for temporal disaggregation of regional climate models.
![Mrs. Frizzle](plots/Mrs._Frizzle.webp)


# Data Acquisition
The hourly bias-corrected reconstruction of near-surface meteorological variables derived from the fifth generation of the European Centre for Medium-Range Weather Forecasts (ECMWF) atmospheric reanalyses (ERA5)
is used as the input to the model <a href="https://cds.climate.copernicus.eu/cdsapp#!/dataset/derived-near-surface-meteorological-variables?tab=overview" target="_blank">[3]</a>.
# ANN Model
![ANN Model](plots/ANN2.pdf)

# References
[1] H. C. Bloomfield et al., ”The Importance of Weather and Climate to Energy Systems: A Workshop on Next Generation Challenges in Energy–Climate Modeling”, Bulletin of the American Meteorological Society, vol. 102, no. 1, pp. E159–E167, 2021.

[2] M. Juckes et al., "The CMIP6 Data Request (DREQ, version 01.00.31)", Geoscientific Model Development, vol. 13, no. 1, pp. 201–224, 2020.

[3] https://cds.climate.copernicus.eu/cdsapp#!/dataset/derived-near-surface-meteorological-variables?tab=overview