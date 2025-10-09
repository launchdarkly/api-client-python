# JudgeAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**judge_config_key** | **str** | Key of the judge AI config | 
**sampling_rate** | **float** | Sampling rate for this judge attachment (0.0 to 1.0) | 

## Example

```python
from launchdarkly_api.models.judge_attachment import JudgeAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of JudgeAttachment from a JSON string
judge_attachment_instance = JudgeAttachment.from_json(json)
# print the JSON string representation of the object
print(JudgeAttachment.to_json())

# convert the object into a dict
judge_attachment_dict = judge_attachment_instance.to_dict()
# create an instance of JudgeAttachment from a dict
judge_attachment_from_dict = JudgeAttachment.from_dict(judge_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


