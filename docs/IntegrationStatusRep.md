# IntegrationStatusRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** |  | [optional] 
**response_body** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 

## Example

```python
from launchdarkly_api.models.integration_status_rep import IntegrationStatusRep

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationStatusRep from a JSON string
integration_status_rep_instance = IntegrationStatusRep.from_json(json)
# print the JSON string representation of the object
print(IntegrationStatusRep.to_json())

# convert the object into a dict
integration_status_rep_dict = integration_status_rep_instance.to_dict()
# create an instance of IntegrationStatusRep from a dict
integration_status_rep_from_dict = IntegrationStatusRep.from_dict(integration_status_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


