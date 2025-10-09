# HoldoutPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name for the holdout | [optional] 
**key** | **str** | A key that identifies the holdout | [optional] 
**description** | **str** | Description of the holdout | [optional] 
**randomizationunit** | **str** | The chosen randomization unit for the holdout base experiment | [optional] 
**attributes** | **List[str]** | The attributes that the holdout iteration&#39;s results can be sliced by | [optional] 
**holdoutamount** | **str** | Audience allocation for the holdout | [optional] 
**primarymetrickey** | **str** | The key of the primary metric for this holdout | [optional] 
**metrics** | [**List[MetricInput]**](MetricInput.md) | Details on the metrics for this experiment | [optional] 
**prerequisiteflagkey** | **str** | The key of the flag that the holdout is dependent on | [optional] 
**maintainer_id** | **str** | Maintainer id | [optional] 

## Example

```python
from launchdarkly_api.models.holdout_post_request import HoldoutPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HoldoutPostRequest from a JSON string
holdout_post_request_instance = HoldoutPostRequest.from_json(json)
# print the JSON string representation of the object
print(HoldoutPostRequest.to_json())

# convert the object into a dict
holdout_post_request_dict = holdout_post_request_instance.to_dict()
# create an instance of HoldoutPostRequest from a dict
holdout_post_request_from_dict = HoldoutPostRequest.from_dict(holdout_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


