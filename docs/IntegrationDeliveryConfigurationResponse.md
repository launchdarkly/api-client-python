# IntegrationDeliveryConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** | The status code returned by the validation | [optional] 
**error** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 
**response_body** | **str** | JSON response to the validation request | [optional] 

## Example

```python
from launchdarkly_api.models.integration_delivery_configuration_response import IntegrationDeliveryConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationDeliveryConfigurationResponse from a JSON string
integration_delivery_configuration_response_instance = IntegrationDeliveryConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(IntegrationDeliveryConfigurationResponse.to_json())

# convert the object into a dict
integration_delivery_configuration_response_dict = integration_delivery_configuration_response_instance.to_dict()
# create an instance of IntegrationDeliveryConfigurationResponse from a dict
integration_delivery_configuration_response_from_dict = IntegrationDeliveryConfigurationResponse.from_dict(integration_delivery_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


