# IntegrationDeliveryConfigurationPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on** | **bool** | Whether the integration configuration is active. Default value is false. | [optional] 
**config** | **Dict[str, object]** |  | 
**tags** | **List[str]** | Tags to associate with the integration | [optional] 
**name** | **str** | Name to identify the integration | [optional] 

## Example

```python
from launchdarkly_api.models.integration_delivery_configuration_post import IntegrationDeliveryConfigurationPost

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationDeliveryConfigurationPost from a JSON string
integration_delivery_configuration_post_instance = IntegrationDeliveryConfigurationPost.from_json(json)
# print the JSON string representation of the object
print(IntegrationDeliveryConfigurationPost.to_json())

# convert the object into a dict
integration_delivery_configuration_post_dict = integration_delivery_configuration_post_instance.to_dict()
# create an instance of IntegrationDeliveryConfigurationPost from a dict
integration_delivery_configuration_post_from_dict = IntegrationDeliveryConfigurationPost.from_dict(integration_delivery_configuration_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


