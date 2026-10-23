# CallerIdentityRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**environment_id** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**environment_name** | **str** |  | [optional] 
**project_name** | **str** |  | [optional] 
**auth_kind** | **str** |  | [optional] 
**token_kind** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_name** | **str** | The registered name of the OAuth client the access token was issued to. Only present for OAuth access tokens, and omitted when the client&#39;s name can&#39;t be resolved. | [optional] 
**audience** | **List[str]** | The resources (RFC 8707) the OAuth access token was issued for. Only present for OAuth access tokens issued for a specific resource. | [optional] 
**expires_at** | **int** |  | [optional] 
**token_name** | **str** |  | [optional] 
**token_id** | **str** |  | [optional] 
**member_id** | **str** |  | [optional] 
**service_token** | **bool** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 

## Example

```python
from launchdarkly_api.models.caller_identity_rep import CallerIdentityRep

# TODO update the JSON string below
json = "{}"
# create an instance of CallerIdentityRep from a JSON string
caller_identity_rep_instance = CallerIdentityRep.from_json(json)
# print the JSON string representation of the object
print(CallerIdentityRep.to_json())

# convert the object into a dict
caller_identity_rep_dict = caller_identity_rep_instance.to_dict()
# create an instance of CallerIdentityRep from a dict
caller_identity_rep_from_dict = CallerIdentityRep.from_dict(caller_identity_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


