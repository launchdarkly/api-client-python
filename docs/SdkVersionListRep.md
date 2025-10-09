# SdkVersionListRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | **Dict[str, object]** | The location and content type of related resources | 
**sdk_versions** | [**List[SdkVersionRep]**](SdkVersionRep.md) | The list of SDK names and versions | 

## Example

```python
from launchdarkly_api.models.sdk_version_list_rep import SdkVersionListRep

# TODO update the JSON string below
json = "{}"
# create an instance of SdkVersionListRep from a JSON string
sdk_version_list_rep_instance = SdkVersionListRep.from_json(json)
# print the JSON string representation of the object
print(SdkVersionListRep.to_json())

# convert the object into a dict
sdk_version_list_rep_dict = sdk_version_list_rep_instance.to_dict()
# create an instance of SdkVersionListRep from a dict
sdk_version_list_rep_from_dict = SdkVersionListRep.from_dict(sdk_version_list_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


