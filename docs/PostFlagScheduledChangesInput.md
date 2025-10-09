# PostFlagScheduledChangesInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional comment describing the scheduled changes | [optional] 
**execution_date** | **int** |  | 
**instructions** | **List[Dict[str, object]]** |  | 

## Example

```python
from launchdarkly_api.models.post_flag_scheduled_changes_input import PostFlagScheduledChangesInput

# TODO update the JSON string below
json = "{}"
# create an instance of PostFlagScheduledChangesInput from a JSON string
post_flag_scheduled_changes_input_instance = PostFlagScheduledChangesInput.from_json(json)
# print the JSON string representation of the object
print(PostFlagScheduledChangesInput.to_json())

# convert the object into a dict
post_flag_scheduled_changes_input_dict = post_flag_scheduled_changes_input_instance.to_dict()
# create an instance of PostFlagScheduledChangesInput from a dict
post_flag_scheduled_changes_input_from_dict = PostFlagScheduledChangesInput.from_dict(post_flag_scheduled_changes_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


