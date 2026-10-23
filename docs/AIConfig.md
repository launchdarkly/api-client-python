# AIConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**AiConfigsAccess**](AiConfigsAccess.md) |  | [optional] 
**links** | [**ParentAndSelfLinks**](ParentAndSelfLinks.md) |  | [optional] 
**site** | [**CoreLink**](CoreLink.md) |  | [optional] 
**description** | **str** | A description of the AI Config | 
**key** | **str** | The AI Config key | 
**maintainer** | [**AIConfigMaintainer**](AIConfigMaintainer.md) |  | [optional] 
**mode** | **str** | The AI Config mode | [optional] [default to 'completion']
**name** | **str** | The AI Config name | 
**tags** | **List[str]** | Tags for this resource | 
**version** | **int** | The version number of this resource | 
**variations** | [**List[AIConfigVariation]**](AIConfigVariation.md) | The variations of this AI Config | 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 
**evaluation_metric_key** | **str** | Evaluation metric key for this config | [optional] 
**evaluation_metric_keys** | **List[str]** | List of evaluation metric keys for this config | [optional] 
**is_inverted** | **bool** | Whether the evaluation metric is inverted, meaning a lower value is better if set as true | [optional] 
**dependencies** | [**List[AIConfigDependency]**](AIConfigDependency.md) | Resources that depend on this config, grouped by type | [optional] 

## Example

```python
from launchdarkly_api.models.ai_config import AIConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AIConfig from a JSON string
ai_config_instance = AIConfig.from_json(json)
# print the JSON string representation of the object
print(AIConfig.to_json())

# convert the object into a dict
ai_config_dict = ai_config_instance.to_dict()
# create an instance of AIConfig from a dict
ai_config_from_dict = AIConfig.from_dict(ai_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


