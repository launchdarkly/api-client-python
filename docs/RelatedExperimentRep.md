# RelatedExperimentRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**environment** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.related_experiment_rep import RelatedExperimentRep

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedExperimentRep from a JSON string
related_experiment_rep_instance = RelatedExperimentRep.from_json(json)
# print the JSON string representation of the object
print(RelatedExperimentRep.to_json())

# convert the object into a dict
related_experiment_rep_dict = related_experiment_rep_instance.to_dict()
# create an instance of RelatedExperimentRep from a dict
related_experiment_rep_from_dict = RelatedExperimentRep.from_dict(related_experiment_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


