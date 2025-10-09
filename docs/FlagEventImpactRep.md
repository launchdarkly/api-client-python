# FlagEventImpactRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **str** | The size of the flag event impact. Sizes are defined as: none (0%), small (0-20%), medium (20-80%), large (&gt;80%) | [optional] 
**percentage** | **float** | The percentage of the flag event impact | [optional] 
**reason** | **str** |  | [optional] 
**evaluations_summary** | [**EvaluationsSummary**](EvaluationsSummary.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.flag_event_impact_rep import FlagEventImpactRep

# TODO update the JSON string below
json = "{}"
# create an instance of FlagEventImpactRep from a JSON string
flag_event_impact_rep_instance = FlagEventImpactRep.from_json(json)
# print the JSON string representation of the object
print(FlagEventImpactRep.to_json())

# convert the object into a dict
flag_event_impact_rep_dict = flag_event_impact_rep_instance.to_dict()
# create an instance of FlagEventImpactRep from a dict
flag_event_impact_rep_from_dict = FlagEventImpactRep.from_dict(flag_event_impact_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


