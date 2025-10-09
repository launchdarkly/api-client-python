# DestinationPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-readable name for your Data Export destination | [optional] 
**kind** | **str** | The type of Data Export destination | [optional] 
**config** | **object** | An object with the configuration parameters required for the destination type | [optional] 
**on** | **bool** | Whether the export is on. Displayed as the integration status in the LaunchDarkly UI. | [optional] 

## Example

```python
from launchdarkly_api.models.destination_post import DestinationPost

# TODO update the JSON string below
json = "{}"
# create an instance of DestinationPost from a JSON string
destination_post_instance = DestinationPost.from_json(json)
# print the JSON string representation of the object
print(DestinationPost.to_json())

# convert the object into a dict
destination_post_dict = destination_post_instance.to_dict()
# create an instance of DestinationPost from a dict
destination_post_from_dict = DestinationPost.from_dict(destination_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


