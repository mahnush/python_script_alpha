import numpy as np
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.basemap import shiftgrid
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.colors

nlon=4001
nlat=1501
rd=287
g=9.8
nlev=25

qnc_dw_di=np.zeros((nlev,nlat,nlon))
qnc_wg_di=np.zeros((nlev,nlat,nlon))
qnc_al1_di=np.zeros((nlev,nlat,nlon))
qnc_al07_di=np.zeros((nlev,nlat,nlon))
qnc_al03_di=np.zeros((nlev,nlat,nlon))
qnc_al02_di=np.zeros((nlev,nlat,nlon))
qnc_al01_di=np.zeros((nlev,nlat,nlon))
den_dw=np.zeros((nlev,nlat,nlon))

ncout = Dataset('/work/bb1093/b380900/holouraun_nccn/alpha_values/nc_file/qnc_w_mean_test_nccn.nc',mode="w",format='NETCDF4_CLASSIC')

ipath_wg ='/work/bb1093/b380900/holouraun_nccn/output_cosp_rad_w/output_uns/remap_data'
ipath_al1 ='/work/bb1093/b380900/holouraun_nccn/alpha_values/alpha_1.33'
ipath_al07='/work/bb1093/b380900/holouraun_nccn/alpha_values/alpha_0.7'
ipath_al03='/work/bb1093/b380900/holouraun_nccn/alpha_values/alpha_0.3'
#ipath_al01='/work/bb1093/b380900/holouraun_nccn/alpha_values/alpha_0.1'
#ifile_dw  = '/work/bb1093/b380900/holouraun_nccn/output_cosp_rad/output_uns/remap_data/NWP_LAM_DOM01_20140901T050000Z_0005.nc'
ifile_dw  = '/work/bb1093/b380900/holouraun_nccn/output_cosp_rad_mic/output_un/remap_data_final/NWP_LAM_DOM01_20140901T050000Z_0005.nc'
ifile_wg  ='/work/bb1093/b380900/holouraun_nccn/output_cosp_rad_w/output_uns/remap_data/NWP_LAM_DOM01_20140901T050000Z_0005.nc'
#ifile_al1='/work/bb1093/b380900/holouraun_nccn/alpha_values/alpha_1.33/remap_NWP_LAM_DOM01_20140901T050000Z_0005.nc'
ifile_al1 ='/work/bb1093/b380900/holouraun_nccn/output_nccn_alpha/alpha_1.33/remap_NWP_LAM_DOM01_20140901T050000Z_0005.nc'
#ifile_al07 ='/work/bb1093/b380900/holouraun_nccn/alpha_values/alpha_0.7/remap_NWP_LAM_DOM01_20140901T050000Z_0005.nc'
ifile_al07 = '/work/bb1093/b380900/holouraun_nccn/output_nccn_alpha/alpha_0.7/remap_NWP_LAM_DOM01_20140901T050000Z_0005.nc'
#ifile_al03='/work/bb1093/b380900/holouraun_nccn/alpha_values/alpha_0.3/remap_NWP_LAM_DOM01_20140901T050000Z_0005.nc'
ifile_al03 ='/work/bb1093/b380900/holouraun_nccn/output_nccn_alpha/alpha_0.3/remap_NWP_LAM_DOM01_20140901T050000Z_0005.nc'
ifile_al02 ='/work/bb1093/b380900/holouraun_nccn/alpha_values/alpha_0.2/remap_NWP_LAM_DOM01_20140901T050000Z_0005.nc'
#ifile_al01 ='/work/bb1093/b380900/holouraun_nccn/alpha_values/alpha_0.1/remap_NWP_LAM_DOM01_20140901T050000Z_0005.nc'
ifile_al01 ='/work/bb1093/b380900/holouraun_nccn/output_nccn_alpha/alpha_0.1/remap_NWP_LAM_DOM01_20140901T050000Z_0005.nc'
#ifile_al01 ='/work/bb1093/b380900/holouraun_nccn/output_nccn_alpha/remap_NWP_LAM_DOM01_20140901T000000Z_0001.nc'
#ifile_al01= ipath_al01+'NWP_LAM_DOM01_20140901T050000Z_0005.nc'
nc_dw =  Dataset(ifile_dw,'r')
nc_wg =  Dataset(ifile_wg,'r')
nc_al1 = Dataset(ifile_al1,'r')
nc_al07= Dataset(ifile_al07,'r')
nc_al03= Dataset(ifile_al03,'r')
nc_al02= Dataset(ifile_al02,'r')
nc_al01= Dataset(ifile_al01,'r')
#nc_al01= Dataset(ifile_al01,'r')
lon=nc_wg.variables['lon'][:]
lat=nc_wg.variables['lat'][:]

qnc_dw  = nc_dw.variables['qnc'][0,:,:,:]
temp_dw = nc_dw.variables['temp'][0,:,:,:]
pres_dw = nc_dw.variables['pres'][0,:,:,:]
geo_dw  = nc_dw.variables['geopot'][0,:,:,:]


qnc_wg  = nc_wg.variables['qnc'][0,:,:,:]
temp_wg = nc_wg.variables['temp'][0,:,:,:]
pres_wg = nc_wg.variables['pres'][0,:,:,:]
geo_wg  = nc_wg.variables['geopot'][0,:,:,:]

qnc_al1 = nc_al1.variables['qnc'][0,:,:,:]
temp_al1 = nc_al1.variables['temp'][0,:,:,:]
pres_al1 = nc_al1.variables['pres'][0,:,:,:]
geo_al1  = nc_al1.variables['geopot'][0,:,:,:]

qnc_al07 = nc_al07.variables['qnc'][0,:,:,:]
temp_al07 = nc_al07.variables['temp'][0,:,:,:]
pres_al07 = nc_al07.variables['pres'][0,:,:,:]
geo_al07  = nc_al07.variables['geopot'][0,:,:,:]

qnc_al03 = nc_al03.variables['qnc'][0,:,:,:]
temp_al03 = nc_al03.variables['temp'][0,:,:,:]
pres_al03 = nc_al03.variables['pres'][0,:,:,:]
geo_al03  = nc_al03.variables['geopot'][0,:,:,:]

qnc_al02 = nc_al02.variables['qnc'][0,:,:,:]
temp_al02 = nc_al02.variables['temp'][0,:,:,:]
pres_al02 = nc_al02.variables['pres'][0,:,:,:]
geo_al02  = nc_al02.variables['geopot'][0,:,:,:]

qnc_al01 = nc_al01.variables['qnc'][0,:,:,:]
temp_al01 = nc_al01.variables['temp'][0,:,:,:]
pres_al01 = nc_al01.variables['pres'][0,:,:,:]
geo_al01  = nc_al01.variables['geopot'][0,:,:,:]


for ihh in range(25):
    ih=ihh+50
    print(ihh)
    print(ih)
    den_dw[ihh,:,:]=pres_dw[ih,:,:]/(rd*temp_dw[ih,:,:])
    qnc_dw_di[ihh,:,:]=(pres_dw[ih,:,:]/(rd*temp_dw[ih,:,:]))*qnc_dw[ih,:,:]
    qnc_wg_di[ihh,:,:]=(pres_wg[ih,:,:]/(rd*temp_wg[ih,:,:]))*qnc_wg[ih,:,:]
    qnc_al1_di[ihh,:,:]=(pres_al1[ih,:,:]/(rd*temp_al1[ih,:,:]))*qnc_al1[ih,:,:]
    qnc_al07_di[ihh,:,:]=(pres_al07[ih,:,:]/(rd*temp_al07[ih,:,:]))*qnc_al07[ih,:,:]
    qnc_al03_di[ihh,:,:]=(pres_al03[ih,:,:]/(rd*temp_al03[ih,:,:]))*qnc_al03[ih,:,:]
    qnc_al02_di[ihh,:,:]=(pres_al02[ih,:,:]/(rd*temp_al02[ih,:,:]))*qnc_al02[ih,:,:]
    qnc_al01_di[ihh,:,:]=(pres_al01[ih,:,:]/(rd*temp_al01[ih,:,:]))*qnc_al01[ih,:,:]

print(np.amax(qnc_dw_di))
print(np.amax(qnc_wg_di))
print(np.amax(qnc_al1_di))
print(np.amax(qnc_al07_di))
print(np.amax(qnc_al03_di))
print(np.amax(qnc_al02_di))
print(np.amax(qnc_al01_di))
print(np.amax(den_dw))
 
avg_qnc_dw_di=(np.mean(qnc_dw_di,axis=0))/1e6   
avg_qnc_wg_di=(np.mean(qnc_wg_di,axis=0))/1e6
avg_qnc_al1_di=(np.mean(qnc_al1_di,axis=0))/1e6
avg_qnc_al07_di=(np.mean(qnc_al07_di,axis=0))/1e6
avg_qnc_al03_di=(np.mean(qnc_al03_di,axis=0))/1e6
avg_qnc_al02_di=(np.mean(qnc_al02_di,axis=0))/1e6
avg_qnc_al01_di=(np.mean(qnc_al01_di,axis=0))/1e6

lon=nc_wg.variables['lon'][:]
lat=nc_wg.variables['lat'][:]
print(np.amax(avg_qnc_dw_di))
print(np.amax(avg_qnc_wg_di))
print(np.amax(avg_qnc_al1_di))
print(np.amax(avg_qnc_al07_di))
print(np.amax(avg_qnc_al03_di))
print(np.amax(avg_qnc_al02_di))
print(np.amax(avg_qnc_al01_di))

ncout.createDimension('lev',nlev)
ncout.createDimension('lon',nlon)
ncout.createDimension('lat',nlat)
lon_o = ncout.createVariable('lon',np.float32,('lon',))
lat_o= ncout.createVariable('lat',np.float32,('lat',))
qnc_dw_mean = ncout.createVariable('qnc_dw',np.float32,('lat','lon'))
qnc_wg_mean = ncout.createVariable('qnc_wg',np.float32,('lat','lon'))
qnc_al1_mean = ncout.createVariable('qnc_al1',np.float32,('lat','lon'))
qnc_al07_mean = ncout.createVariable('qnc_al07',np.float32,('lat','lon'))
qnc_al03_mean = ncout.createVariable('qnc_al03',np.float32,('lat','lon'))
qnc_al02_mean = ncout.createVariable('qnc_al02',np.float32,('lat','lon'))
qnc_al01_mean = ncout.createVariable('qnc_al01',np.float32,('lat','lon'))
den_dw_o=ncout.createVariable('den',np.float32,('lev','lat','lon'))
lon_o[:]=lon[:]
lat_o[:]=lat[:]
qnc_dw_mean[:]=avg_qnc_dw_di[:]
qnc_wg_mean[:]=avg_qnc_wg_di[:]
qnc_al1_mean[:]=avg_qnc_al1_di[:]
qnc_al07_mean[:]=avg_qnc_al07_di[:]
qnc_al03_mean[:]=avg_qnc_al03_di[:]
qnc_al02_mean[:]=avg_qnc_al02_di[:]
qnc_al01_mean[:]=avg_qnc_al01_di[:]
den_dw_o[:]=den_dw[:]
