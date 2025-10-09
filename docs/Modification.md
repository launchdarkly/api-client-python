# Modification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** |  | [optional] 

## Example

```python
from launchdarkly_api.models.modification import Modification

# TODO update the JSON string below
json = "{}"
# create an instance of Modification from a JSON string
modification_instance = Modification.from_json(json)
# print the JSON string representation of the object
print(Modification.to_json())

# convert the object into a dict
modification_dict = modification_instance.to_dict()
# create an instance of Modification from a dict
modification_from_dict = Modification.from_dict(modification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


