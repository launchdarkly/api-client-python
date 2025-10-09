# DeploymentRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The deployment ID | 
**application_key** | **str** | The application key | 
**application_version** | **str** | The application version | 
**started_at** | **int** |  | 
**ended_at** | **int** |  | [optional] 
**duration_ms** | **int** | The duration of the deployment in milliseconds | [optional] 
**status** | **str** |  | 
**kind** | **str** |  | 
**active** | **bool** | Whether the deployment is active | 
**metadata** | **Dict[str, object]** | The metadata associated with the deployment | [optional] 
**archived** | **bool** | Whether the deployment is archived | 
**environment_key** | **str** | The environment key | 
**number_of_contributors** | **int** | The number of contributors | 
**number_of_pull_requests** | **int** | The number of pull requests | 
**lines_added** | **int** | The number of lines added | 
**lines_deleted** | **int** | The number of lines deleted | 
**lead_time** | **int** | The total lead time from first commit to deployment end in milliseconds | 
**pull_requests** | [**PullRequestCollectionRep**](PullRequestCollectionRep.md) |  | [optional] 
**flag_references** | [**FlagReferenceCollectionRep**](FlagReferenceCollectionRep.md) |  | [optional] 
**lead_time_stages** | [**LeadTimeStagesRep**](LeadTimeStagesRep.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.deployment_rep import DeploymentRep

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentRep from a JSON string
deployment_rep_instance = DeploymentRep.from_json(json)
# print the JSON string representation of the object
print(DeploymentRep.to_json())

# convert the object into a dict
deployment_rep_dict = deployment_rep_instance.to_dict()
# create an instance of DeploymentRep from a dict
deployment_rep_from_dict = DeploymentRep.from_dict(deployment_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


