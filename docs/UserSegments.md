# UserSegments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[UserSegment]**](UserSegment.md) | An array of segments | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**total_count** | **int** | The total number of segments | [optional] 

## Example

```python
from launchdarkly_api.models.user_segments import UserSegments

# TODO update the JSON string below
json = "{}"
# create an instance of UserSegments from a JSON string
user_segments_instance = UserSegments.from_json(json)
# print the JSON string representation of the object
print(UserSegments.to_json())

# convert the object into a dict
user_segments_dict = user_segments_instance.to_dict()
# create an instance of UserSegments from a dict
user_segments_from_dict = UserSegments.from_dict(user_segments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


