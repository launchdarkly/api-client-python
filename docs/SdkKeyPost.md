# SdkKeyPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | The kind of SDK key. Can be either \&quot;sdk\&quot; (server-side) or \&quot;mobile\&quot; (mobile). Defaults to \&quot;sdk\&quot; when not explicitly defined. | [optional] [default to 'sdk']
**key** | **str** | The user-defined key of the SDK key. | 
**name** | **str** | The human-readable name of the SDK key. | 
**description** | **str** | The optional description of the SDK key. | [optional] 
**expiry** | **int** |  | [optional] 

## Example

```python
from launchdarkly_api.models.sdk_key_post import SdkKeyPost

# TODO update the JSON string below
json = "{}"
# create an instance of SdkKeyPost from a JSON string
sdk_key_post_instance = SdkKeyPost.from_json(json)
# print the JSON string representation of the object
print(SdkKeyPost.to_json())

# convert the object into a dict
sdk_key_post_dict = sdk_key_post_instance.to_dict()
# create an instance of SdkKeyPost from a dict
sdk_key_post_from_dict = SdkKeyPost.from_dict(sdk_key_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


