import hiblooms_core as hb
import numpy as np

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--shp_path', action='store', type=int, required=True, dest='shp_path')


args = arg_parser.parse_args()
print(args)

id = args.id

shp_path = args.shp_path



for v in ["res","dates","df_media","df_points","df_distribution",
          "df_media_comb","gdf","aoi"]:
    if v in globals():
        del globals()[v]

gdf = hb.load_reservoir_shapefile("VAL", shp_path)  # name must match the shapefile
aoi = hb.gdf_to_ee_geometry(gdf)

dates = hb.get_available_dates(aoi, "2024-06-01", "2024-06-15", max_cloud_percentage=60)

res = hb.run_batch_processing(
    aoi=aoi,
    available_dates=dates,
    selected_indices=("MCI","NDCI_ind","PC_Val_cal","Chla_Val_cal"),  # calibrated indices for VAL
    max_cloud_percentage=60,
    points_of_interest={"VAL": {"Probe": (41.8761, -1.7883)}},  # probe point of interest
    reservoir_name_for_pois="VAL",
    compute_distributions=True,
    distribution_bins_by_index={
        "PC_Val_cal": np.linspace(0,10,6),
        "MCI": np.linspace(-0.1,0.4,6)
    }
)

print("Processed dates:", res.processed_dates[:10])
print("Example GeoTIFF URL:", res.urls_exportacion[:1])
print("First data_time records:", res.data_time[:5])

file_res = open("/tmp/res_" + id + ".json", "w")
file_res.write(json.dumps(res))
file_res.close()
