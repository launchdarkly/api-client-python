# IntegrationStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from launchdarkly_api.models.integration_status import IntegrationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationStatus from a JSON string
integration_status_instance = IntegrationStatus.from_json(json)
# print the JSON string representation of the object
print(IntegrationStatus.to_json())

# convert the object into a dict
integration_status_dict = integration_status_instance.to_dict()
# create an instance of IntegrationStatus from a dict
integration_status_from_dict = IntegrationStatus.from_dict(integration_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


