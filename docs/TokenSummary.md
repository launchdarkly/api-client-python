# TokenSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** | The name of the token | [optional] 
**ending** | **str** | The last few characters of the token | [optional] 
**service_token** | **bool** | Whether this is a service token | [optional] 

## Example

```python
from launchdarkly_api.models.token_summary import TokenSummary

# TODO update the JSON string below
json = "{}"
# create an instance of TokenSummary from a JSON string
token_summary_instance = TokenSummary.from_json(json)
# print the JSON string representation of the object
print(TokenSummary.to_json())

# convert the object into a dict
token_summary_dict = token_summary_instance.to_dict()
# create an instance of TokenSummary from a dict
token_summary_from_dict = TokenSummary.from_dict(token_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


