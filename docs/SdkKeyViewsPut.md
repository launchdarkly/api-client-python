# SdkKeyViewsPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_keys** | **List[str]** | The complete target list of view keys to associate with this SDK key. An empty array removes all views from the SDK key. | 

## Example

```python
from launchdarkly_api.models.sdk_key_views_put import SdkKeyViewsPut

# TODO update the JSON string below
json = "{}"
# create an instance of SdkKeyViewsPut from a JSON string
sdk_key_views_put_instance = SdkKeyViewsPut.from_json(json)
# print the JSON string representation of the object
print(SdkKeyViewsPut.to_json())

# convert the object into a dict
sdk_key_views_put_dict = sdk_key_views_put_instance.to_dict()
# create an instance of SdkKeyViewsPut from a dict
sdk_key_views_put_from_dict = SdkKeyViewsPut.from_dict(sdk_key_views_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


