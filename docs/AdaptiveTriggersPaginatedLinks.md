# AdaptiveTriggersPaginatedLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | [**ExperimentationLink**](ExperimentationLink.md) |  | [optional] 
**last** | [**ExperimentationLink**](ExperimentationLink.md) |  | [optional] 
**next** | [**ExperimentationLink**](ExperimentationLink.md) |  | [optional] 
**prev** | [**ExperimentationLink**](ExperimentationLink.md) |  | [optional] 
**var_self** | [**ExperimentationLink**](ExperimentationLink.md) |  | 

## Example

```python
from launchdarkly_api.models.adaptive_triggers_paginated_links import AdaptiveTriggersPaginatedLinks

# TODO update the JSON string below
json = "{}"
# create an instance of AdaptiveTriggersPaginatedLinks from a JSON string
adaptive_triggers_paginated_links_instance = AdaptiveTriggersPaginatedLinks.from_json(json)
# print the JSON string representation of the object
print(AdaptiveTriggersPaginatedLinks.to_json())

# convert the object into a dict
adaptive_triggers_paginated_links_dict = adaptive_triggers_paginated_links_instance.to_dict()
# create an instance of AdaptiveTriggersPaginatedLinks from a dict
adaptive_triggers_paginated_links_from_dict = AdaptiveTriggersPaginatedLinks.from_dict(adaptive_triggers_paginated_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


