# UserFlagSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources. | 
**value** | **object** | The value of the flag variation that the user receives. If there is no defined default rule, this is null. | 
**setting** | **object** | Whether the user is explicitly targeted to receive a particular variation. The setting is false if you have turned off a feature flag for a user. It is null if you haven&#39;t assigned that user to a specific variation. | 
**reason** | [**EvaluationReason**](EvaluationReason.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.user_flag_setting import UserFlagSetting

# TODO update the JSON string below
json = "{}"
# create an instance of UserFlagSetting from a JSON string
user_flag_setting_instance = UserFlagSetting.from_json(json)
# print the JSON string representation of the object
print(UserFlagSetting.to_json())

# convert the object into a dict
user_flag_setting_dict = user_flag_setting_instance.to_dict()
# create an instance of UserFlagSetting from a dict
user_flag_setting_from_dict = UserFlagSetting.from_dict(user_flag_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


