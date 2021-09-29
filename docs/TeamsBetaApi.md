# launchdarkly_api.TeamsBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_team**](TeamsBetaApi.md#delete_team) | **DELETE** /api/v2/teams/{key} | Delete team by key
[**get_team**](TeamsBetaApi.md#get_team) | **GET** /api/v2/teams/{key} | Get team by key
[**get_teams**](TeamsBetaApi.md#get_teams) | **GET** /api/v2/teams | Get all teams
[**patch_team**](TeamsBetaApi.md#patch_team) | **PATCH** /api/v2/teams/{key} | Patch team by key
[**post_team**](TeamsBetaApi.md#post_team) | **POST** /api/v2/teams | Create team


# **delete_team**
> delete_team(key)

Delete team by key

Delete a team by key.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import teams__beta_api
from pprint import pprint
# Defining the host is optional and defaults to https://app.launchdarkly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = launchdarkly_api.Configuration(
    host = "https://app.launchdarkly.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = teams__beta_api.TeamsBetaApi(api_client)
    key = "key_example" # str | The team key

    # example passing only required values which don't have defaults set
    try:
        # Delete team by key
        api_instance.delete_team(key)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling TeamsBetaApi->delete_team: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The team key |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Action completed successfully |  -  |
**401** | Invalid access token |  -  |
**404** | Unknown team key |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team**
> TeamRep get_team(key)

Get team by key

Fetch a team by key.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import teams__beta_api
from launchdarkly_api.model.team_rep import TeamRep
from pprint import pprint
# Defining the host is optional and defaults to https://app.launchdarkly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = launchdarkly_api.Configuration(
    host = "https://app.launchdarkly.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = teams__beta_api.TeamsBetaApi(api_client)
    key = "key_example" # str | The team key

    # example passing only required values which don't have defaults set
    try:
        # Get team by key
        api_response = api_instance.get_team(key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling TeamsBetaApi->get_team: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The team key |

### Return type

[**TeamRep**](TeamRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Team response JSON |  -  |
**400** | Invalid request body |  -  |
**401** | Invalid access token |  -  |
**404** | Unknown team key |  -  |
**405** | Method not allowed |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teams**
> TeamCollectionRep get_teams()

Get all teams

Fetch all teams.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import teams__beta_api
from launchdarkly_api.model.team_collection_rep import TeamCollectionRep
from pprint import pprint
# Defining the host is optional and defaults to https://app.launchdarkly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = launchdarkly_api.Configuration(
    host = "https://app.launchdarkly.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = teams__beta_api.TeamsBetaApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all teams
        api_response = api_instance.get_teams()
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling TeamsBetaApi->get_teams: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TeamCollectionRep**](TeamCollectionRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Teams collection response JSON |  -  |
**401** | Invalid access token |  -  |
**405** | Method not allowed |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_team**
> TeamCollectionRep patch_team(key, team_patch_input)

Patch team by key

Perform a partial update to a team.  The body of a semantic patch request takes the following three properties:  1. comment `string`: (Optional) A description of the update. 1. environmentKey `string`: (Required) The key of the LaunchDarkly environment. 1. instructions `array`: (Required) The action or list of actions to be performed by the update. Each update action in the list must be an object/hash table with a `kind` property, although depending on the action, other properties may be necessary. Read below for more information on the specific supported semantic patch instructions.  If any instruction in the patch encounters an error, the error will be returned and the flag will not be changed. In general, instructions will silently do nothing if the flag is already in the state requested by the patch instruction. They will generally error if a parameter refers to something that does not exist. Other specific error conditions are noted in the instruction descriptions.  ### Instructions  #### `addCustomRoles`  Adds custom roles to the team. Team members will have these custom roles granted to them.  ##### Parameters  - `values`: list of custom role keys  #### `removeCustomRoles`  Removes the custom roles on the team. Team members will no longer have these custom roles granted to them.  ##### Parameters  - `values`: list of custom role keys  #### `addMembers`  Adds members to the team.  ##### Parameters  - `values`: list of member IDs  #### `removeMembers`  Removes members from the team.  ##### Parameters  - `values`: list of member IDs  #### `addPermissionGrants`  Adds permission grants to members for the team, allowing them to, for example, act as a team maintainer. A permission grant may have either an `actionSet` or a list of `actions` but not both at the same time. The members do not have to be team members to have a permission grant for the team.  ##### Parameters  - `actionSet`: name of the action set - `actions`: list of actions - `memberIDs`: list of member IDs  #### `removePermissionGrants`  Removes permission grants from members for the team. The `actionSet` and `actions` must match an existing permission grant.  ##### Parameters  - `actionSet`: name of the action set - `actions`: list of actions - `memberIDs`: list of member IDs  #### `updateDescription`  Updates the team's description.  ##### Parameters  - `value`: the team's new description  #### `updateName`  Updates the team's name.  ##### Parameters  - `value`: the team's new name 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import teams__beta_api
from launchdarkly_api.model.team_patch_input import TeamPatchInput
from launchdarkly_api.model.team_collection_rep import TeamCollectionRep
from pprint import pprint
# Defining the host is optional and defaults to https://app.launchdarkly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = launchdarkly_api.Configuration(
    host = "https://app.launchdarkly.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = teams__beta_api.TeamsBetaApi(api_client)
    key = "key_example" # str | The team key
    team_patch_input = TeamPatchInput(
        comment="comment_example",
        instructions=Instructions([
            Instruction(
                key=None,
            ),
        ]),
    ) # TeamPatchInput | 

    # example passing only required values which don't have defaults set
    try:
        # Patch team by key
        api_response = api_instance.patch_team(key, team_patch_input)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling TeamsBetaApi->patch_team: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The team key |
 **team_patch_input** | [**TeamPatchInput**](TeamPatchInput.md)|  |

### Return type

[**TeamCollectionRep**](TeamCollectionRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Teams collection response JSON |  -  |
**400** | Invalid request body |  -  |
**401** | Invalid access token |  -  |
**404** | Unknown team key |  -  |
**405** | Method not allowed |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_team**
> TeamRep post_team(team_post_input)

Create team

Create a team.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import teams__beta_api
from launchdarkly_api.model.team_rep import TeamRep
from launchdarkly_api.model.team_post_input import TeamPostInput
from pprint import pprint
# Defining the host is optional and defaults to https://app.launchdarkly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = launchdarkly_api.Configuration(
    host = "https://app.launchdarkly.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = teams__beta_api.TeamsBetaApi(api_client)
    team_post_input = TeamPostInput(
        custom_role_keys=[
            "custom_role_keys_example",
        ],
        description="description_example",
        key="key_example",
        member_ids=[
            "member_ids_example",
        ],
        name="name_example",
        permission_grants=[
            PermissionGrantInput(
                member_ids=[
                    "member_ids_example",
                ],
                actions=[
                    "actions_example",
                ],
                action_set="action_set_example",
            ),
        ],
    ) # TeamPostInput | 

    # example passing only required values which don't have defaults set
    try:
        # Create team
        api_response = api_instance.post_team(team_post_input)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling TeamsBetaApi->post_team: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_post_input** | [**TeamPostInput**](TeamPostInput.md)|  |

### Return type

[**TeamRep**](TeamRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful teams response |  -  |
**400** | Invalid request body |  -  |
**401** | Invalid access token |  -  |
**405** | Method not allowed |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

