# ExperimentationLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.experimentation_link import ExperimentationLink

# TODO update the JSON string below
json = "{}"
# create an instance of ExperimentationLink from a JSON string
experimentation_link_instance = ExperimentationLink.from_json(json)
# print the JSON string representation of the object
print(ExperimentationLink.to_json())

# convert the object into a dict
experimentation_link_dict = experimentation_link_instance.to_dict()
# create an instance of ExperimentationLink from a dict
experimentation_link_from_dict = ExperimentationLink.from_dict(experimentation_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


