from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:
    
    now = kwargs.get('execution_date')
    print(now) # Output: '2024-01-25 18:42:18.783257' (example output)

    now_fpath = now.strftime('%Y/%m/%d')
    print(now_fpath) # Output: '2024/01/25' (example output)

    bucket_name = 'mage-zoomcamp-jonah-oliver'
    object_key = f'{now_fpath}/daily-trips.parquet'
    print(object_key) # Output: 2024/01/25/daily-trips.parquet (example output)

    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    # GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).export(
    #     df,
    #     bucket_name,
    #     object_key,
    # )


