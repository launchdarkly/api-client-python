# HunkRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**starting_line_number** | **int** | Line number of beginning of code reference hunk | 
**lines** | **str** | Contextual lines of code that include the referenced feature flag | [optional] 
**proj_key** | **str** | The project key | [optional] 
**flag_key** | **str** | The feature flag key | [optional] 
**aliases** | **List[str]** | An array of flag key aliases | [optional] 

## Example

```python
from launchdarkly_api.models.hunk_rep import HunkRep

# TODO update the JSON string below
json = "{}"
# create an instance of HunkRep from a JSON string
hunk_rep_instance = HunkRep.from_json(json)
# print the JSON string representation of the object
print(HunkRep.to_json())

# convert the object into a dict
hunk_rep_dict = hunk_rep_instance.to_dict()
# create an instance of HunkRep from a dict
hunk_rep_from_dict = HunkRep.from_dict(hunk_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


