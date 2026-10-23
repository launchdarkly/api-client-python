# ModelConfigPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human readable name of the model | 
**key** | **str** | Unique key for the model config in the project, in the format &#x60;Provider.model-id&#x60;. Config variations reject other formats. Keys of global catalog models are reserved. | 
**id** | **str** | Model ID that the provider&#39;s API uses. Cannot be changed after creation. | 
**maintainer_id** | **str** | The member ID of the maintainer. Not applied on create. To set the maintainer, update the model config after you create it. | [optional] 
**maintainer_team_key** | **str** | The key of the team that maintains the model config. Not applied on create. To set the maintainer, update the model config after you create it. | [optional] 
**icon** | **str** | Icon for the model | [optional] 
**provider** | **str** | Provider for the model. Use the provider prefix of &#x60;key&#x60;. Cannot be changed after creation. | [optional] 
**params** | **object** | Freeform JSON object. LaunchDarkly does not validate the keys. In a model config, &#x60;params&#x60; and &#x60;customParams&#x60; hold parameters that the provider&#39;s API accepts, for example &#x60;{\&quot;temperature\&quot;: 0.7, \&quot;maxTokens\&quot;: 4096}&#x60;. | [optional] 
**custom_params** | **object** | Freeform JSON object. LaunchDarkly does not validate the keys. In a model config, &#x60;params&#x60; and &#x60;customParams&#x60; hold parameters that the provider&#39;s API accepts, for example &#x60;{\&quot;temperature\&quot;: 0.7, \&quot;maxTokens\&quot;: 4096}&#x60;. | [optional] 
**tags** | **List[str]** | Tags for the model config | [optional] 
**cost_per_input_token** | **float** | Cost per input token in USD | [optional] 
**cost_per_output_token** | **float** | Cost per output token in USD | [optional] 
**cost_per_cached_input_token** | **float** | Cost per cached input token in USD | [optional] 

## Example

```python
from launchdarkly_api.models.model_config_post import ModelConfigPost

# TODO update the JSON string below
json = "{}"
# create an instance of ModelConfigPost from a JSON string
model_config_post_instance = ModelConfigPost.from_json(json)
# print the JSON string representation of the object
print(ModelConfigPost.to_json())

# convert the object into a dict
model_config_post_dict = model_config_post_instance.to_dict()
# create an instance of ModelConfigPost from a dict
model_config_post_from_dict = ModelConfigPost.from_dict(model_config_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


