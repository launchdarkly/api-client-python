# ConflictOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stage_id** | **str** | The stage ID | 
**message** | **str** | Message about the conflict | 

## Example

```python
from launchdarkly_api.models.conflict_output import ConflictOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ConflictOutput from a JSON string
conflict_output_instance = ConflictOutput.from_json(json)
# print the JSON string representation of the object
print(ConflictOutput.to_json())

# convert the object into a dict
conflict_output_dict = conflict_output_instance.to_dict()
# create an instance of ConflictOutput from a dict
conflict_output_from_dict = ConflictOutput.from_dict(conflict_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


