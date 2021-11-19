# launchdarkly_api.TeamsBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_team**](TeamsBetaApi.md#delete_team) | **DELETE** /api/v2/teams/{key} | Delete team
[**get_team**](TeamsBetaApi.md#get_team) | **GET** /api/v2/teams/{key} | Get team
[**get_teams**](TeamsBetaApi.md#get_teams) | **GET** /api/v2/teams | List teams
[**patch_team**](TeamsBetaApi.md#patch_team) | **PATCH** /api/v2/teams/{key} | Update team
[**post_team**](TeamsBetaApi.md#post_team) | **POST** /api/v2/teams | Create team


# **delete_team**
> delete_team(key)

Delete team

Delete a team by key

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import teams__beta_api
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
        # Delete team
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
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Action succeeded |  -  |
**401** | Invalid access token |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team**
> TeamRep get_team(key)

Get team

Fetch a team by key

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import teams__beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.team_rep import TeamRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.method_not_allowed_error_rep import MethodNotAllowedErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
        # Get team
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
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**405** | Method not allowed |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teams**
> TeamCollectionRep get_teams()

List teams

Return a list of teams.  By default, this returns the first 20 teams. Page through this list with the `limit` parameter and by following the `first`, `prev`, `next`, and `last` links in the returned `_links` field. These links are not present if the pages they refer to don't exist. For example, the `first` and `prev` links will be missing from the response on the first page.  ### Filtering teams  LaunchDarkly supports the `query` field for filtering. `query` is a string that matches against the teams' names and keys. It is not case sensitive. For example, the filter `query:abc` matches teams with the string `abc` in their name or key. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import teams__beta_api
from launchdarkly_api.model.method_not_allowed_error_rep import MethodNotAllowedErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
    limit = 1 # int | The number of teams to return in the response. Defaults to 20. (optional)
    offset = 1 # int | Where to start in the list. This is for use with pagination. For example, an offset of 10 would skip the first ten items and then return the next `limit` items. (optional)
    filter = "filter_example" # str | A comma-separated list of filters. Each filter is of the form `field:value`. Supported fields are explained above. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List teams
        api_response = api_instance.get_teams(limit=limit, offset=offset, filter=filter)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling TeamsBetaApi->get_teams: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of teams to return in the response. Defaults to 20. | [optional]
 **offset** | **int**| Where to start in the list. This is for use with pagination. For example, an offset of 10 would skip the first ten items and then return the next &#x60;limit&#x60; items. | [optional]
 **filter** | **str**| A comma-separated list of filters. Each filter is of the form &#x60;field:value&#x60;. Supported fields are explained above. | [optional]

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

Update team

Perform a partial update to a team.  The body of a semantic patch request takes the following three properties:  1. comment `string`: (Optional) A description of the update. 1. instructions `array`: (Required) The action or list of actions to be performed by the update. Each update action in the list must be an object/hash table with a `kind` property, although depending on the action, other properties may be necessary. Read below for more information on the specific supported semantic patch instructions.  If any instruction in the patch encounters an error, the error will be returned and the flag will not be changed. In general, instructions will silently do nothing if the flag is already in the state requested by the patch instruction. They will generally error if a parameter refers to something that does not exist. Other specific error conditions are noted in the instruction descriptions.  ### Instructions  #### `addCustomRoles`  Adds custom roles to the team. Team members will have these custom roles granted to them.  ##### Parameters  - `values`: list of custom role keys  #### `removeCustomRoles`  Removes the custom roles on the team. Team members will no longer have these custom roles granted to them.  ##### Parameters  - `values`: list of custom role keys  #### `addMembers`  Adds members to the team.  ##### Parameters  - `values`: list of member IDs  #### `removeMembers`  Removes members from the team.  ##### Parameters  - `values`: list of member IDs  #### `addPermissionGrants`  Adds permission grants to members for the team, allowing them to, for example, act as a team maintainer. A permission grant may have either an `actionSet` or a list of `actions` but not both at the same time. The members do not have to be team members to have a permission grant for the team.  ##### Parameters  - `actionSet`: name of the action set - `actions`: list of actions - `memberIDs`: list of member IDs  #### `removePermissionGrants`  Removes permission grants from members for the team. The `actionSet` and `actions` must match an existing permission grant.  ##### Parameters  - `actionSet`: name of the action set - `actions`: list of actions - `memberIDs`: list of member IDs  #### `updateDescription`  Updates the team's description.  ##### Parameters  - `value`: the team's new description  #### `updateName`  Updates the team's name.  ##### Parameters  - `value`: the team's new name 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import teams__beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.method_not_allowed_error_rep import MethodNotAllowedErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.team_patch_input import TeamPatchInput
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.team_collection_rep import TeamCollectionRep
from launchdarkly_api.model.status_conflict_error_rep import StatusConflictErrorRep
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
        # Update team
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
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**404** | Invalid resource identifier |  -  |
**405** | Method not allowed |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_team**
> TeamRep post_team(team_post_input)

Create team

Create a team

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import teams__beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.team_rep import TeamRep
from launchdarkly_api.model.method_not_allowed_error_rep import MethodNotAllowedErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**405** | Method not allowed |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

