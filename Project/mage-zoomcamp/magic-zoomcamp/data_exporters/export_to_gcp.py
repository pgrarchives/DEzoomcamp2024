from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

from datetime import datetime

# Generate an object key with the current date for a one-time batch process
date_str = datetime.now().strftime('%Y%m%d')
object_key = f'batch_processing/one_time_data_{date_str}.csv'


# @data_exporter
# def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:
#     """
#     Template for exporting data to a Google Cloud Storage bucket.
#     Specify your configuration settings in 'io_config.yaml'.

#     Docs: https://docs.mage.ai/design/data-loading#googlecloudstorage
#     """
#     config_path = path.join(get_repo_path(), 'io_config.yaml')
#     config_profile = 'default'

#     bucket_name = 'your_bucket_name'
#     object_key = 'your_object_key'

#     GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).export(
#         df,
#         bucket_name,
#         object_key,
#     )

@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    bucket_name = 'adtagroup1'  # Replace with your actual bucket name
    object_key = f'batch_processing/noise_complaints_{date_str}.csv'  # Use the dynamic date for the batch process

    GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).export(
        df,
        bucket_name,
        object_key,
    )

