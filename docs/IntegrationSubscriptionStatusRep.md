# IntegrationSubscriptionStatusRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success_count** | **int** |  | [optional] 
**last_success** | **int** |  | [optional] 
**last_error** | **int** |  | [optional] 
**error_count** | **int** |  | [optional] 
**errors** | [**List[IntegrationStatusRep]**](IntegrationStatusRep.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.integration_subscription_status_rep import IntegrationSubscriptionStatusRep

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationSubscriptionStatusRep from a JSON string
integration_subscription_status_rep_instance = IntegrationSubscriptionStatusRep.from_json(json)
# print the JSON string representation of the object
print(IntegrationSubscriptionStatusRep.to_json())

# convert the object into a dict
integration_subscription_status_rep_dict = integration_subscription_status_rep_instance.to_dict()
# create an instance of IntegrationSubscriptionStatusRep from a dict
integration_subscription_status_rep_from_dict = IntegrationSubscriptionStatusRep.from_dict(integration_subscription_status_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


