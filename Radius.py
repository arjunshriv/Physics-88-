# %%
import lightkurve as lk
%matplotlib inline
# Search for Kepler observations of Kepler-11
search_result = lk.search_lightcurve('Kepler-11', author='Kepler', cadence='long')
# Download all available Kepler light curves
lc_collection = search_result.download_all()
lc = lc_collection.stitch().flatten(window_length=901).remove_outliers()
import numpy as np
# Create array of periods to search
period = np.linspace(1, 80, 10000)
# Create a BLSPeriodogram
bls = lc.to_periodogram(method='bls', period=period);
planet_b_period = bls.period_at_max_power
planet_b_t0 = bls.transit_time_at_max_power
planet_b_dur = bls.duration_at_max_power

# Check the value for period
planet_b_period
ax = lc.fold(period=planet_b_period, epoch_time=planet_b_t0).scatter()
ax.set_xlim(-6.5, 6.5);

#Finding the radius
depth = bls.depth_at_max_power
radius = np.power(depth*np.power(7.096*(10**8),2),0.5)
print("\nThe radius of the planet with period of ~13 days is " + str(radius*(10**-7)) + "⋅10^7 meters")


