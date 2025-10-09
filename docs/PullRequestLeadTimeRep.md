# PullRequestLeadTimeRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coding_duration_ms** | **int** | The coding duration in milliseconds | 
**review_duration_ms** | **int** | The review duration in milliseconds | [optional] 
**max_wait_duration_ms** | **int** | The max wait duration between merge time and deploy start time in milliseconds | [optional] 
**avg_wait_duration_ms** | **int** | The average wait duration between merge time and deploy start time in milliseconds | [optional] 
**max_deploy_duration_ms** | **int** | The max deploy duration in milliseconds | [optional] 
**avg_deploy_duration_ms** | **int** | The average deploy duration in milliseconds | [optional] 
**max_total_lead_time_ms** | **int** | The max total lead time in milliseconds | [optional] 
**avg_total_lead_time_ms** | **int** | The average total lead time in milliseconds | [optional] 

## Example

```python
from launchdarkly_api.models.pull_request_lead_time_rep import PullRequestLeadTimeRep

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequestLeadTimeRep from a JSON string
pull_request_lead_time_rep_instance = PullRequestLeadTimeRep.from_json(json)
# print the JSON string representation of the object
print(PullRequestLeadTimeRep.to_json())

# convert the object into a dict
pull_request_lead_time_rep_dict = pull_request_lead_time_rep_instance.to_dict()
# create an instance of PullRequestLeadTimeRep from a dict
pull_request_lead_time_rep_from_dict = PullRequestLeadTimeRep.from_dict(pull_request_lead_time_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


