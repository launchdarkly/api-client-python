# Clause


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attribute** | **str** |  | 
**op** | **str** |  | 
**values** | **List[object]** |  | 
**context_kind** | **str** |  | [optional] 
**negate** | **bool** |  | 

## Example

```python
from launchdarkly_api.models.clause import Clause

# TODO update the JSON string below
json = "{}"
# create an instance of Clause from a JSON string
clause_instance = Clause.from_json(json)
# print the JSON string representation of the object
print(Clause.to_json())

# convert the object into a dict
clause_dict = clause_instance.to_dict()
# create an instance of Clause from a dict
clause_from_dict = Clause.from_dict(clause_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


