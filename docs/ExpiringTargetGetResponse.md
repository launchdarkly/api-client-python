# ExpiringTargetGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ExpiringTarget]**](ExpiringTarget.md) | A list of expiring targets | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 

## Example

```python
from launchdarkly_api.models.expiring_target_get_response import ExpiringTargetGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExpiringTargetGetResponse from a JSON string
expiring_target_get_response_instance = ExpiringTargetGetResponse.from_json(json)
# print the JSON string representation of the object
print(ExpiringTargetGetResponse.to_json())

# convert the object into a dict
expiring_target_get_response_dict = expiring_target_get_response_instance.to_dict()
# create an instance of ExpiringTargetGetResponse from a dict
expiring_target_get_response_from_dict = ExpiringTargetGetResponse.from_dict(expiring_target_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


