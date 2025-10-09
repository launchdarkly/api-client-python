# HMACSignature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header_name** | **str** |  | [optional] 
**hmac_secret_form_variable_key** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.hmac_signature import HMACSignature

# TODO update the JSON string below
json = "{}"
# create an instance of HMACSignature from a JSON string
hmac_signature_instance = HMACSignature.from_json(json)
# print the JSON string representation of the object
print(HMACSignature.to_json())

# convert the object into a dict
hmac_signature_dict = hmac_signature_instance.to_dict()
# create an instance of HMACSignature from a dict
hmac_signature_from_dict = HMACSignature.from_dict(hmac_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


