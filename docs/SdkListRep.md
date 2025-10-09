# SdkListRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | **Dict[str, object]** | The location and content type of related resources | 
**sdks** | **List[str]** | The list of SDK names | 

## Example

```python
from launchdarkly_api.models.sdk_list_rep import SdkListRep

# TODO update the JSON string below
json = "{}"
# create an instance of SdkListRep from a JSON string
sdk_list_rep_instance = SdkListRep.from_json(json)
# print the JSON string representation of the object
print(SdkListRep.to_json())

# convert the object into a dict
sdk_list_rep_dict = sdk_list_rep_instance.to_dict()
# create an instance of SdkListRep from a dict
sdk_list_rep_from_dict = SdkListRep.from_dict(sdk_list_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


