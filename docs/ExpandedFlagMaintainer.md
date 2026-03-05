# ExpandedFlagMaintainer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The ID of the maintainer member, or the key of the maintainer team | 
**kind** | **str** | The type of the maintainer | 
**member** | [**ViewsMemberSummary**](ViewsMemberSummary.md) |  | [optional] 
**team** | [**ViewsMemberTeamSummaryRep**](ViewsMemberTeamSummaryRep.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.expanded_flag_maintainer import ExpandedFlagMaintainer

# TODO update the JSON string below
json = "{}"
# create an instance of ExpandedFlagMaintainer from a JSON string
expanded_flag_maintainer_instance = ExpandedFlagMaintainer.from_json(json)
# print the JSON string representation of the object
print(ExpandedFlagMaintainer.to_json())

# convert the object into a dict
expanded_flag_maintainer_dict = expanded_flag_maintainer_instance.to_dict()
# create an instance of ExpandedFlagMaintainer from a dict
expanded_flag_maintainer_from_dict = ExpandedFlagMaintainer.from_dict(expanded_flag_maintainer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


