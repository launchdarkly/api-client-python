# PostInsightGroupParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the insight group | 
**key** | **str** | The key of the insight group | 
**project_key** | **str** | The projectKey to be associated with the insight group | 
**environment_key** | **str** | The environmentKey to be associated with the insight group | 
**application_keys** | **List[str]** | The application keys to associate with the insight group. If not provided, the insight group will include data from all applications. | [optional] 

## Example

```python
from launchdarkly_api.models.post_insight_group_params import PostInsightGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of PostInsightGroupParams from a JSON string
post_insight_group_params_instance = PostInsightGroupParams.from_json(json)
# print the JSON string representation of the object
print(PostInsightGroupParams.to_json())

# convert the object into a dict
post_insight_group_params_dict = post_insight_group_params_instance.to_dict()
# create an instance of PostInsightGroupParams from a dict
post_insight_group_params_from_dict = PostInsightGroupParams.from_dict(post_insight_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


