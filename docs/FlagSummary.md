# FlagSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variations** | [**Dict[str, VariationSummary]**](VariationSummary.md) |  | 
**prerequisites** | **int** | The number of prerequisites for this flag | 

## Example

```python
from launchdarkly_api.models.flag_summary import FlagSummary

# TODO update the JSON string below
json = "{}"
# create an instance of FlagSummary from a JSON string
flag_summary_instance = FlagSummary.from_json(json)
# print the JSON string representation of the object
print(FlagSummary.to_json())

# convert the object into a dict
flag_summary_dict = flag_summary_instance.to_dict()
# create an instance of FlagSummary from a dict
flag_summary_from_dict = FlagSummary.from_dict(flag_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


