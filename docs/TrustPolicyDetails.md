# TrustPolicyDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The version of the trust policy | [optional] 
**statement** | [**List[TrustPolicyStatement]**](TrustPolicyStatement.md) | The statements of the trust policy | [optional] 

## Example

```python
from launchdarkly_api.models.trust_policy_details import TrustPolicyDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TrustPolicyDetails from a JSON string
trust_policy_details_instance = TrustPolicyDetails.from_json(json)
# print the JSON string representation of the object
print(TrustPolicyDetails.to_json())

# convert the object into a dict
trust_policy_details_dict = trust_policy_details_instance.to_dict()
# create an instance of TrustPolicyDetails from a dict
trust_policy_details_from_dict = TrustPolicyDetails.from_dict(trust_policy_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


