# SegmentUserList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add** | **List[str]** |  | [optional] 
**remove** | **List[str]** |  | [optional] 

## Example

```python
from launchdarkly_api.models.segment_user_list import SegmentUserList

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentUserList from a JSON string
segment_user_list_instance = SegmentUserList.from_json(json)
# print the JSON string representation of the object
print(SegmentUserList.to_json())

# convert the object into a dict
segment_user_list_dict = segment_user_list_instance.to_dict()
# create an instance of SegmentUserList from a dict
segment_user_list_from_dict = SegmentUserList.from_dict(segment_user_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


