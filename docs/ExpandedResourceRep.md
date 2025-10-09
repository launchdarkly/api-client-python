# ExpandedResourceRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | The type of resource | 
**ai_config** | [**AIConfigRep**](AIConfigRep.md) |  | [optional] 
**flag** | [**ExpandedFlagRep**](ExpandedFlagRep.md) |  | [optional] 
**segment** | [**UserSegment**](UserSegment.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.expanded_resource_rep import ExpandedResourceRep

# TODO update the JSON string below
json = "{}"
# create an instance of ExpandedResourceRep from a JSON string
expanded_resource_rep_instance = ExpandedResourceRep.from_json(json)
# print the JSON string representation of the object
print(ExpandedResourceRep.to_json())

# convert the object into a dict
expanded_resource_rep_dict = expanded_resource_rep_instance.to_dict()
# create an instance of ExpandedResourceRep from a dict
expanded_resource_rep_from_dict = ExpandedResourceRep.from_dict(expanded_resource_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


