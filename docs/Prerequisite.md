# Prerequisite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**variation** | **int** |  | 

## Example

```python
from launchdarkly_api.models.prerequisite import Prerequisite

# TODO update the JSON string below
json = "{}"
# create an instance of Prerequisite from a JSON string
prerequisite_instance = Prerequisite.from_json(json)
# print the JSON string representation of the object
print(Prerequisite.to_json())

# convert the object into a dict
prerequisite_dict = prerequisite_instance.to_dict()
# create an instance of Prerequisite from a dict
prerequisite_from_dict = Prerequisite.from_dict(prerequisite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


