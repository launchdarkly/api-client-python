# GenerateTrustPolicyPostRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_trust_policy** | [**TrustPolicyDetails**](TrustPolicyDetails.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.generate_trust_policy_post_rep import GenerateTrustPolicyPostRep

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateTrustPolicyPostRep from a JSON string
generate_trust_policy_post_rep_instance = GenerateTrustPolicyPostRep.from_json(json)
# print the JSON string representation of the object
print(GenerateTrustPolicyPostRep.to_json())

# convert the object into a dict
generate_trust_policy_post_rep_dict = generate_trust_policy_post_rep_instance.to_dict()
# create an instance of GenerateTrustPolicyPostRep from a dict
generate_trust_policy_post_rep_from_dict = GenerateTrustPolicyPostRep.from_dict(generate_trust_policy_post_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


