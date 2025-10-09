# FlagPrerequisitePost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Flag key of the prerequisite flag | 
**variation_id** | **str** | ID of a variation of the prerequisite flag | 

## Example

```python
from launchdarkly_api.models.flag_prerequisite_post import FlagPrerequisitePost

# TODO update the JSON string below
json = "{}"
# create an instance of FlagPrerequisitePost from a JSON string
flag_prerequisite_post_instance = FlagPrerequisitePost.from_json(json)
# print the JSON string representation of the object
print(FlagPrerequisitePost.to_json())

# convert the object into a dict
flag_prerequisite_post_dict = flag_prerequisite_post_instance.to_dict()
# create an instance of FlagPrerequisitePost from a dict
flag_prerequisite_post_from_dict = FlagPrerequisitePost.from_dict(flag_prerequisite_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


