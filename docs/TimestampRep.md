# TimestampRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**milliseconds** | **int** |  | [optional] 
**seconds** | **int** |  | [optional] 
**rfc3339** | **str** |  | [optional] 
**simple** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.timestamp_rep import TimestampRep

# TODO update the JSON string below
json = "{}"
# create an instance of TimestampRep from a JSON string
timestamp_rep_instance = TimestampRep.from_json(json)
# print the JSON string representation of the object
print(TimestampRep.to_json())

# convert the object into a dict
timestamp_rep_dict = timestamp_rep_instance.to_dict()
# create an instance of TimestampRep from a dict
timestamp_rep_from_dict = TimestampRep.from_dict(timestamp_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


