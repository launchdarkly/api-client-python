# TargetResourceRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) |  | [optional] 
**name** | **str** | The name of the resource | [optional] 
**resources** | **List[str]** | The resource specifier | [optional] 

## Example

```python
from launchdarkly_api.models.target_resource_rep import TargetResourceRep

# TODO update the JSON string below
json = "{}"
# create an instance of TargetResourceRep from a JSON string
target_resource_rep_instance = TargetResourceRep.from_json(json)
# print the JSON string representation of the object
print(TargetResourceRep.to_json())

# convert the object into a dict
target_resource_rep_dict = target_resource_rep_instance.to_dict()
# create an instance of TargetResourceRep from a dict
target_resource_rep_from_dict = TargetResourceRep.from_dict(target_resource_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


