# SdkKeyPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | (Optional)The human-readable name of the SDK key. | [optional] 
**description** | **str** | (Optional) The description of the SDK key. | [optional] 
**expiry** | **int** |  | [optional] 

## Example

```python
from launchdarkly_api.models.sdk_key_patch import SdkKeyPatch

# TODO update the JSON string below
json = "{}"
# create an instance of SdkKeyPatch from a JSON string
sdk_key_patch_instance = SdkKeyPatch.from_json(json)
# print the JSON string representation of the object
print(SdkKeyPatch.to_json())

# convert the object into a dict
sdk_key_patch_dict = sdk_key_patch_instance.to_dict()
# create an instance of SdkKeyPatch from a dict
sdk_key_patch_from_dict = SdkKeyPatch.from_dict(sdk_key_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


