# StaleFlagData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ready_for_code_removal** | **bool** | Whether the flag is ready for code removal | [optional] 
**ready_to_archive** | **bool** | Whether the flag is ready to be archived | [optional] 
**cleanup_id** | **str** | If a third-party system helps clean up the flag, the ID from that system | [optional] 

## Example

```python
from launchdarkly_api.models.stale_flag_data import StaleFlagData

# TODO update the JSON string below
json = "{}"
# create an instance of StaleFlagData from a JSON string
stale_flag_data_instance = StaleFlagData.from_json(json)
# print the JSON string representation of the object
print(StaleFlagData.to_json())

# convert the object into a dict
stale_flag_data_dict = stale_flag_data_instance.to_dict()
# create an instance of StaleFlagData from a dict
stale_flag_data_from_dict = StaleFlagData.from_dict(stale_flag_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


