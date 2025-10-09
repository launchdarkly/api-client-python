# IntegrationDeliveryConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**IntegrationDeliveryConfigurationLinks**](IntegrationDeliveryConfigurationLinks.md) |  | 
**id** | **str** | The integration ID | 
**integration_key** | **str** | The integration key | 
**project_key** | **str** | The project key | 
**environment_key** | **str** | The environment key | 
**config** | **Dict[str, object]** |  | 
**on** | **bool** | Whether the configuration is turned on | 
**tags** | **List[str]** | List of tags for this configuration | 
**name** | **str** | Name of the configuration | 
**version** | **int** | Version of the current configuration | 
**access** | [**Access**](Access.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.integration_delivery_configuration import IntegrationDeliveryConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationDeliveryConfiguration from a JSON string
integration_delivery_configuration_instance = IntegrationDeliveryConfiguration.from_json(json)
# print the JSON string representation of the object
print(IntegrationDeliveryConfiguration.to_json())

# convert the object into a dict
integration_delivery_configuration_dict = integration_delivery_configuration_instance.to_dict()
# create an instance of IntegrationDeliveryConfiguration from a dict
integration_delivery_configuration_from_dict = IntegrationDeliveryConfiguration.from_dict(integration_delivery_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


