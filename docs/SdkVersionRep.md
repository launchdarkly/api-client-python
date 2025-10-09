# SdkVersionRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sdk** | **str** | The SDK name, or \&quot;Unknown\&quot; | 
**version** | **str** | The version number, or \&quot;Unknown\&quot; | 

## Example

```python
from launchdarkly_api.models.sdk_version_rep import SdkVersionRep

# TODO update the JSON string below
json = "{}"
# create an instance of SdkVersionRep from a JSON string
sdk_version_rep_instance = SdkVersionRep.from_json(json)
# print the JSON string representation of the object
print(SdkVersionRep.to_json())

# convert the object into a dict
sdk_version_rep_dict = sdk_version_rep_instance.to_dict()
# create an instance of SdkVersionRep from a dict
sdk_version_rep_from_dict = SdkVersionRep.from_dict(sdk_version_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


