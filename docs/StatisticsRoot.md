# StatisticsRoot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**projects** | [**List[Link]**](Link.md) | The location and content type of all projects that have code references | [optional] 
**var_self** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.statistics_root import StatisticsRoot

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticsRoot from a JSON string
statistics_root_instance = StatisticsRoot.from_json(json)
# print the JSON string representation of the object
print(StatisticsRoot.to_json())

# convert the object into a dict
statistics_root_dict = statistics_root_instance.to_dict()
# create an instance of StatisticsRoot from a dict
statistics_root_from_dict = StatisticsRoot.from_dict(statistics_root_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


