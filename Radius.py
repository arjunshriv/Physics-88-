# %%
import lightkurve as lk
%matplotlib inline
import numpy as np
# Search for Kepler observations of Kepler objects
search_result_1 = lk.search_lightcurve('Kepler-4', author='Kepler', cadence='long')
lc_collection_1 = search_result_1.download_all()
lc_1 = lc_collection_1.stitch().flatten(window_length=901).remove_outliers()

search_result_2 = lk.search_lightcurve('Kepler-5', author='Kepler', cadence='long')
lc_collection_2 = search_result_2.download_all()
lc_2 = lc_collection_2.stitch().flatten(window_length=901).remove_outliers()

search_result_3 = lk.search_lightcurve('Kepler-6', author='Kepler', cadence='long')
lc_collection_3 = search_result_3.download_all()
lc_3 = lc_collection_3.stitch().flatten(window_length=901).remove_outliers()

search_result_4 = lk.search_lightcurve('Kepler-7', author='Kepler', cadence='long')
lc_collection_4 = search_result_4.download_all()
lc_4 = lc_collection_4.stitch().flatten(window_length=901).remove_outliers()

search_result_5 = lk.search_lightcurve('Kepler-8', author='Kepler', cadence='long')
lc_collection_5 = search_result_5.download_all()
lc_5 = lc_collection_5.stitch().flatten(window_length=901).remove_outliers()

search_result_6 = lk.search_lightcurve('Kepler-66', author='Kepler', cadence='long')
lc_collection_6 = search_result_6.download_all()
lc_6 = lc_collection_6.stitch().flatten(window_length=901).remove_outliers()

search_result_7 = lk.search_lightcurve('Kepler-59', author='Kepler', cadence='long')
lc_collection_7 = search_result_7.download_all()
lc_7 = lc_collection_7.stitch().flatten(window_length=901).remove_outliers()

search_result_8 = lk.search_lightcurve('Kepler-13', author='Kepler', cadence='long')
lc_collection_8 = search_result_8.download_all()
lc_8 = lc_collection_8.stitch().flatten(window_length=901).remove_outliers()

search_result_9 = lk.search_lightcurve('Kepler-14', author='Kepler', cadence='long')
lc_collection_9 = search_result_9.download_all()
lc_9 = lc_collection_9.stitch().flatten(window_length=901).remove_outliers()

search_result_10 = lk.search_lightcurve('Kepler-15', author='Kepler', cadence='long')
lc_collection_10 = search_result_10.download_all()
lc_10 = lc_collection_10.stitch().flatten(window_length=901).remove_outliers()

radii = [1.555, 1.793, 1.391, 1.843, 1.486, 0.966, 1.386, 1.71, 2.048, 0.992]
star_radii = np.array(radii)*(6.957*10**8)
def getRadius(lc_array, star_radius):
    period = np.linspace(1, 80, 10000)
    bls_array = lc_array.to_periodogram(method='bls', period = period)
    planet_b_period = bls_array.period_at_max_power
    planet_b_t0 = bls_array.transit_time_at_max_power
    # Check the value for period
    planet_b_period
    ax = lc_array.fold(period=planet_b_period, epoch_time=planet_b_t0).scatter()
    ax.set_xlim(-5, 5);
    #Finding the radius
    depth = bls_array.depth_at_max_power
    radius = np.power(depth*np.power(star_radius,2),0.5)
    return radius

radius_1 = getRadius(lc_1, star_radii[0])
radius_2 = getRadius(lc_2, star_radii[1])
radius_3 = getRadius(lc_3, star_radii[2])
radius_4 = getRadius(lc_4, star_radii[3])
radius_5 = getRadius(lc_5, star_radii[4])
radius_6 = getRadius(lc_6, star_radii[5])
radius_7 = getRadius(lc_7, star_radii[6])
radius_8 = getRadius(lc_8, star_radii[7])
radius_9 = getRadius(lc_9, star_radii[8])
radius_10 = getRadius(lc_10, star_radii[9])
