# ReleasePoliciesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ReleasePolicy]**](ReleasePolicy.md) | List of release policies | 
**total_count** | **int** | Total number of release policies | 

## Example

```python
from launchdarkly_api.models.release_policies_response import ReleasePoliciesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReleasePoliciesResponse from a JSON string
release_policies_response_instance = ReleasePoliciesResponse.from_json(json)
# print the JSON string representation of the object
print(ReleasePoliciesResponse.to_json())

# convert the object into a dict
release_policies_response_dict = release_policies_response_instance.to_dict()
# create an instance of ReleasePoliciesResponse from a dict
release_policies_response_from_dict = ReleasePoliciesResponse.from_dict(release_policies_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


