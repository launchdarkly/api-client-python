# ParentResourceRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) |  | [optional] 
**name** | **str** | The name of the parent resource | [optional] 
**resource** | **str** | The parent&#39;s resource specifier | [optional] 

## Example

```python
from launchdarkly_api.models.parent_resource_rep import ParentResourceRep

# TODO update the JSON string below
json = "{}"
# create an instance of ParentResourceRep from a JSON string
parent_resource_rep_instance = ParentResourceRep.from_json(json)
# print the JSON string representation of the object
print(ParentResourceRep.to_json())

# convert the object into a dict
parent_resource_rep_dict = parent_resource_rep_instance.to_dict()
# create an instance of ParentResourceRep from a dict
parent_resource_rep_from_dict = ParentResourceRep.from_dict(parent_resource_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


