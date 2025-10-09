# FlagCopyConfigPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**FlagCopyConfigEnvironment**](FlagCopyConfigEnvironment.md) |  | 
**target** | [**FlagCopyConfigEnvironment**](FlagCopyConfigEnvironment.md) |  | 
**comment** | **str** | Optional comment | [optional] 
**included_actions** | **List[str]** | Optional list of the flag changes to copy from the source environment to the target environment. You may include either &lt;code&gt;includedActions&lt;/code&gt; or &lt;code&gt;excludedActions&lt;/code&gt;, but not both. If you include neither, then all flag changes will be copied. | [optional] 
**excluded_actions** | **List[str]** | Optional list of the flag changes NOT to copy from the source environment to the target environment. You may include either  &lt;code&gt;includedActions&lt;/code&gt; or &lt;code&gt;excludedActions&lt;/code&gt;, but not both. If you include neither, then all flag changes will be copied. | [optional] 

## Example

```python
from launchdarkly_api.models.flag_copy_config_post import FlagCopyConfigPost

# TODO update the JSON string below
json = "{}"
# create an instance of FlagCopyConfigPost from a JSON string
flag_copy_config_post_instance = FlagCopyConfigPost.from_json(json)
# print the JSON string representation of the object
print(FlagCopyConfigPost.to_json())

# convert the object into a dict
flag_copy_config_post_dict = flag_copy_config_post_instance.to_dict()
# create an instance of FlagCopyConfigPost from a dict
flag_copy_config_post_from_dict = FlagCopyConfigPost.from_dict(flag_copy_config_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


