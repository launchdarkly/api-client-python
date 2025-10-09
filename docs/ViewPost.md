# ViewPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Unique key for the view within the account/project | 
**name** | **str** | Human-readable name for the view | 
**description** | **str** | Optional detailed description of the view | [optional] [default to '']
**generate_sdk_keys** | **bool** | Whether to generate SDK keys for this view | [optional] [default to False]
**maintainer_id** | **str** | Member ID of the maintainer for this view. Only one of &#x60;maintainerId&#x60; or &#x60;maintainerTeamKey&#x60; can be specified. | [optional] 
**maintainer_team_key** | **str** | Key of the maintainer team for this view. Only one of &#x60;maintainerId&#x60; or &#x60;maintainerTeamKey&#x60; can be specified. | [optional] 
**tags** | **List[str]** | Tags associated with this view | [optional] 

## Example

```python
from launchdarkly_api.models.view_post import ViewPost

# TODO update the JSON string below
json = "{}"
# create an instance of ViewPost from a JSON string
view_post_instance = ViewPost.from_json(json)
# print the JSON string representation of the object
print(ViewPost.to_json())

# convert the object into a dict
view_post_dict = view_post_instance.to_dict()
# create an instance of ViewPost from a dict
view_post_from_dict = ViewPost.from_dict(view_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


