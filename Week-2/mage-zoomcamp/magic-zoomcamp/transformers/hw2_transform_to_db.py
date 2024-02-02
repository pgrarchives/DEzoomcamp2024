import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
def camel_to_snake(name):
    import re
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

@transformer
def transform(data, *args, **kwargs):
    # print("Rows with zero passengers: ",data['passenger_count'].isin([0]).sum() or )
    data=data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]
    data.lpep_pickup_datetime = pd.to_datetime(data.lpep_pickup_datetime)
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    new_columns = {old_name: camel_to_snake(old_name) for old_name in data.columns}
    data.rename(columns=new_columns, inplace=True)
    return data[data['passenger_count'] > 0]
    


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['vendor_id'].isin(output.columns).all
    assert (output['passenger_count'] > 0).all(), "There are rows with passenger_count <= 0."
    assert (output['trip_distance'] > 0).all(), "There are rows with trip_distance <= 0."