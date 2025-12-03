# TrustPolicyStatement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effect** | **str** | The effect of trust policy statement | [optional] 
**action** | **List[str]** | The action of trust policy statement | [optional] 
**principal** | **object** | The principal of trust policy statement | [optional] 
**condition** | **object** | The condition of trust policy statement | [optional] 

## Example

```python
from launchdarkly_api.models.trust_policy_statement import TrustPolicyStatement

# TODO update the JSON string below
json = "{}"
# create an instance of TrustPolicyStatement from a JSON string
trust_policy_statement_instance = TrustPolicyStatement.from_json(json)
# print the JSON string representation of the object
print(TrustPolicyStatement.to_json())

# convert the object into a dict
trust_policy_statement_dict = trust_policy_statement_instance.to_dict()
# create an instance of TrustPolicyStatement from a dict
trust_policy_statement_from_dict = TrustPolicyStatement.from_dict(trust_policy_statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


