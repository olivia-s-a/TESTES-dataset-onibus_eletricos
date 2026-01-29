import os
import geopandas as gpd
from config import data_folder

def save_shp(gdf: gpd.GeoDataFrame, file_name: str = "data.shp"):
    """
    Salva um GeoDataFrame como .shp diretamente na data_folder.

    Args:
        gdf: GeoDataFrame a ser salvo
        file_name: nome do arquivo .shp a ser salvo (default: "data.shp")
    """
    
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    file_path = os.path.join(data_folder, file_name)

    gdf.to_file(file_path)

    print(f"Shapefile salvo em {file_path}")


def save_shp_custom(
    gdf: gpd.GeoDataFrame,
    data_path: str = os.path.join(data_folder, 'data.shp')
):
    """
    Salva um GeoDataFrame como .shp sem pasta especificada.

    Args:
        gdf: GeoDataFrame a ser salvo
        file_name: nome do arquivo .shp a ser salvo (default: "data.shp")
    """

    folder_path = os.path.dirname(data_path)
    file_name= os.path.basename(data_path)
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    gdf.to_file(data_path)

    print(f"Shapefile salvo em {data_path}")