# ExpiringUserTargetGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ExpiringUserTargetItem]**](ExpiringUserTargetItem.md) | An array of expiring user targets | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 

## Example

```python
from launchdarkly_api.models.expiring_user_target_get_response import ExpiringUserTargetGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExpiringUserTargetGetResponse from a JSON string
expiring_user_target_get_response_instance = ExpiringUserTargetGetResponse.from_json(json)
# print the JSON string representation of the object
print(ExpiringUserTargetGetResponse.to_json())

# convert the object into a dict
expiring_user_target_get_response_dict = expiring_user_target_get_response_instance.to_dict()
# create an instance of ExpiringUserTargetGetResponse from a dict
expiring_user_target_get_response_from_dict = ExpiringUserTargetGetResponse.from_dict(expiring_user_target_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


