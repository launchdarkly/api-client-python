# FlagsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**linked_flags** | [**ExpandedDirectlyLinkedFlags**](ExpandedDirectlyLinkedFlags.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.flags_summary import FlagsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of FlagsSummary from a JSON string
flags_summary_instance = FlagsSummary.from_json(json)
# print the JSON string representation of the object
print(FlagsSummary.to_json())

# convert the object into a dict
flags_summary_dict = flags_summary_instance.to_dict()
# create an instance of FlagsSummary from a dict
flags_summary_from_dict = FlagsSummary.from_dict(flags_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


