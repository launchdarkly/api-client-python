# AssignedToRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members_count** | **int** | The number of individual members this role is assigned to | [optional] 
**teams_count** | **int** | The number of teams this role is assigned to | [optional] 

## Example

```python
from launchdarkly_api.models.assigned_to_rep import AssignedToRep

# TODO update the JSON string below
json = "{}"
# create an instance of AssignedToRep from a JSON string
assigned_to_rep_instance = AssignedToRep.from_json(json)
# print the JSON string representation of the object
print(AssignedToRep.to_json())

# convert the object into a dict
assigned_to_rep_dict = assigned_to_rep_instance.to_dict()
# create an instance of AssignedToRep from a dict
assigned_to_rep_from_dict = AssignedToRep.from_dict(assigned_to_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


