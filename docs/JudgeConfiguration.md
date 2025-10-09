# JudgeConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**judges** | [**List[JudgeAttachment]**](JudgeAttachment.md) | List of judges for this variation. When updating, this replaces all existing judge attachments, and if empty, removes all judge attachments.  | [optional] 

## Example

```python
from launchdarkly_api.models.judge_configuration import JudgeConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of JudgeConfiguration from a JSON string
judge_configuration_instance = JudgeConfiguration.from_json(json)
# print the JSON string representation of the object
print(JudgeConfiguration.to_json())

# convert the object into a dict
judge_configuration_dict = judge_configuration_instance.to_dict()
# create an instance of JudgeConfiguration from a dict
judge_configuration_from_dict = JudgeConfiguration.from_dict(judge_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


