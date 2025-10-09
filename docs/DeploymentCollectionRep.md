# DeploymentCollectionRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of deployments | 
**items** | [**List[DeploymentRep]**](DeploymentRep.md) | A list of deployments | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 

## Example

```python
from launchdarkly_api.models.deployment_collection_rep import DeploymentCollectionRep

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentCollectionRep from a JSON string
deployment_collection_rep_instance = DeploymentCollectionRep.from_json(json)
# print the JSON string representation of the object
print(DeploymentCollectionRep.to_json())

# convert the object into a dict
deployment_collection_rep_dict = deployment_collection_rep_instance.to_dict()
# create an instance of DeploymentCollectionRep from a dict
deployment_collection_rep_from_dict = DeploymentCollectionRep.from_dict(deployment_collection_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


