# AudiencePost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_key** | **str** | A project-unique key for the environment. | 
**name** | **str** | The audience name | 
**segment_keys** | **List[str]** | Segments targeted by this audience. | [optional] 
**configuration** | [**AudienceConfiguration**](AudienceConfiguration.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.audience_post import AudiencePost

# TODO update the JSON string below
json = "{}"
# create an instance of AudiencePost from a JSON string
audience_post_instance = AudiencePost.from_json(json)
# print the JSON string representation of the object
print(AudiencePost.to_json())

# convert the object into a dict
audience_post_dict = audience_post_instance.to_dict()
# create an instance of AudiencePost from a dict
audience_post_from_dict = AudiencePost.from_dict(audience_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


