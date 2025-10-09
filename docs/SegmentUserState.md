# SegmentUserState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**included** | [**SegmentUserList**](SegmentUserList.md) |  | [optional] 
**excluded** | [**SegmentUserList**](SegmentUserList.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.segment_user_state import SegmentUserState

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentUserState from a JSON string
segment_user_state_instance = SegmentUserState.from_json(json)
# print the JSON string representation of the object
print(SegmentUserState.to_json())

# convert the object into a dict
segment_user_state_dict = segment_user_state_instance.to_dict()
# create an instance of SegmentUserState from a dict
segment_user_state_from_dict = SegmentUserState.from_dict(segment_user_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


