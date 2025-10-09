# FlagConfigEvaluation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_kinds** | **List[str]** |  | [optional] 

## Example

```python
from launchdarkly_api.models.flag_config_evaluation import FlagConfigEvaluation

# TODO update the JSON string below
json = "{}"
# create an instance of FlagConfigEvaluation from a JSON string
flag_config_evaluation_instance = FlagConfigEvaluation.from_json(json)
# print the JSON string representation of the object
print(FlagConfigEvaluation.to_json())

# convert the object into a dict
flag_config_evaluation_dict = flag_config_evaluation_instance.to_dict()
# create an instance of FlagConfigEvaluation from a dict
flag_config_evaluation_from_dict = FlagConfigEvaluation.from_dict(flag_config_evaluation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


