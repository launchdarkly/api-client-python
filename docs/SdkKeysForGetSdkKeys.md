# SdkKeysForGetSdkKeys


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**SdkKeysSelfLink**](SdkKeysSelfLink.md) |  | [optional] 
**items** | [**List[SdkKey]**](SdkKey.md) |  | 
**total_count** | **int** | The total number of SDK keys matching the query, before pagination. | 

## Example

```python
from launchdarkly_api.models.sdk_keys_for_get_sdk_keys import SdkKeysForGetSdkKeys

# TODO update the JSON string below
json = "{}"
# create an instance of SdkKeysForGetSdkKeys from a JSON string
sdk_keys_for_get_sdk_keys_instance = SdkKeysForGetSdkKeys.from_json(json)
# print the JSON string representation of the object
print(SdkKeysForGetSdkKeys.to_json())

# convert the object into a dict
sdk_keys_for_get_sdk_keys_dict = sdk_keys_for_get_sdk_keys_instance.to_dict()
# create an instance of SdkKeysForGetSdkKeys from a dict
sdk_keys_for_get_sdk_keys_from_dict = SdkKeysForGetSdkKeys.from_dict(sdk_keys_for_get_sdk_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


