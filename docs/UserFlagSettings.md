# UserFlagSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**Dict[str, UserFlagSetting]**](UserFlagSetting.md) | An array of flag settings for the user | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 

## Example

```python
from launchdarkly_api.models.user_flag_settings import UserFlagSettings

# TODO update the JSON string below
json = "{}"
# create an instance of UserFlagSettings from a JSON string
user_flag_settings_instance = UserFlagSettings.from_json(json)
# print the JSON string representation of the object
print(UserFlagSettings.to_json())

# convert the object into a dict
user_flag_settings_dict = user_flag_settings_instance.to_dict()
# create an instance of UserFlagSettings from a dict
user_flag_settings_from_dict = UserFlagSettings.from_dict(user_flag_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


