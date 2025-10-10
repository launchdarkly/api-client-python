# launchdarkly_api.AccountMembersApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_member**](AccountMembersApi.md#delete_member) | **DELETE** /api/v2/members/{id} | Delete account member
[**get_member**](AccountMembersApi.md#get_member) | **GET** /api/v2/members/{id} | Get account member
[**get_members**](AccountMembersApi.md#get_members) | **GET** /api/v2/members | List account members
[**patch_member**](AccountMembersApi.md#patch_member) | **PATCH** /api/v2/members/{id} | Modify an account member
[**post_member_teams**](AccountMembersApi.md#post_member_teams) | **POST** /api/v2/members/{id}/teams | Add a member to teams
[**post_members**](AccountMembersApi.md#post_members) | **POST** /api/v2/members | Invite new members


# **delete_member**
> delete_member(id)

Delete account member

Delete a single account member by ID. Requests to delete account members will not work if SCIM is enabled for the account.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.rest import ApiException
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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = launchdarkly_api.AccountMembersApi(api_client)
    id = 'id_example' # str | The member ID

    try:
        # Delete account member
        api_instance.delete_member(id)
    except Exception as e:
        print("Exception when calling AccountMembersApi->delete_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The member ID | 

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
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_member**
> Member get_member(id, expand=expand)

Get account member

Get a single account member by member ID.

`me` is a reserved value for the `id` parameter that returns the caller's member information.

### Expanding the member response
LaunchDarkly supports one field for expanding the "Get member" response. By default, this field is **not** included in the response.

To expand the response, append the `expand` query parameter and add a comma-separated list with any of the following fields:

* `roleAttributes` includes a list of the role attributes that you have assigned to the member.

For example, `expand=roleAttributes` includes `roleAttributes` field in the response.


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.member import Member
from launchdarkly_api.rest import ApiException
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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = launchdarkly_api.AccountMembersApi(api_client)
    id = 'id_example' # str | The member ID
    expand = 'expand_example' # str | A comma-separated list of properties that can reveal additional information in the response. (optional)

    try:
        # Get account member
        api_response = api_instance.get_member(id, expand=expand)
        print("The response of AccountMembersApi->get_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountMembersApi->get_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The member ID | 
 **expand** | **str**| A comma-separated list of properties that can reveal additional information in the response. | [optional] 

### Return type

[**Member**](Member.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Member response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members**
> Members get_members(limit=limit, offset=offset, filter=filter, expand=expand, sort=sort)

List account members

Return a list of account members.

By default, this returns the first 20 members. Page through this list with the `limit` parameter and by following the `first`, `prev`, `next`, and `last` links in the returned `_links` field. These links are not present if the pages they refer to don't exist. For example, the `first` and `prev` links will be missing from the response on the first page.

### Filtering members

LaunchDarkly supports the following fields for filters:

- `query` is a string that matches against the members' emails and names. It is not case sensitive.
- `role` is a `|` separated list of roles and custom roles. It filters the list to members who have any of the roles in the list. For the purposes of this filtering, `Owner` counts as `Admin`.
- `id` is a `|` separated list of member IDs. It filters the list to members who match any of the IDs in the list.
- `email` is a `|` separated list of member emails. It filters the list to members who match any of the emails in the list.
- `team` is a string that matches against the key of the teams the members belong to. It is not case sensitive.
- `noteam` is a boolean that filters the list of members who are not on a team if true and members on a team if false.
- `lastSeen` is a JSON object in one of the following formats:
  - `{"never": true}` - Members that have never been active, such as those who have not accepted their invitation to LaunchDarkly, or have not logged in after being provisioned via SCIM.
  - `{"noData": true}` - Members that have not been active since LaunchDarkly began recording last seen timestamps.
  - `{"before": 1608672063611}` - Members that have not been active since the provided value, which should be a timestamp in Unix epoch milliseconds.
- `accessCheck` is a string that represents a specific action on a specific resource and is in the format `<ActionSpecifier>:<ResourceSpecifier>`. It filters the list to members who have the ability to perform that action on that resource. Note: `accessCheck` is only supported in API version `20220603` and earlier. To learn more, read [Versioning](https://launchdarkly.com/docs/api#versioning).
  - For example, the filter `accessCheck:createApprovalRequest:proj/default:env/test:flag/alternate-page` matches members with the ability to create an approval request for the `alternate-page` flag in the `test` environment of the `default` project.
  - Wildcard and tag filters are not supported when filtering for access.

For example, the filter `query:abc,role:admin|customrole` matches members with the string `abc` in their email or name, ignoring case, who also are either an `Owner` or `Admin` or have the custom role `customrole`.

### Sorting members

LaunchDarkly supports two fields for sorting: `displayName` and `lastSeen`:

- `displayName` sorts by first + last name, using the member's email if no name is set.
- `lastSeen` sorts by the `_lastSeen` property. LaunchDarkly considers members that have never been seen or have no data the oldest.

### Expanding the members response
LaunchDarkly supports two fields for expanding the "List members" response. By default, these fields are **not** included in the response.

To expand the response, append the `expand` query parameter and add a comma-separated list with any of the following fields:

* `customRoles` includes a list of the roles that you have assigned to the member.
* `roleAttributes` includes a list of the role attributes that you have assigned to the member.

For example, `expand=roleAttributes` includes `roleAttributes` field in the response.


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.members import Members
from launchdarkly_api.rest import ApiException
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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = launchdarkly_api.AccountMembersApi(api_client)
    limit = 56 # int | The number of members to return in the response. Defaults to 20. (optional)
    offset = 56 # int | Where to start in the list. This is for use with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)
    filter = 'filter_example' # str | A comma-separated list of filters. Each filter is of the form `field:value`. Supported fields are explained above. (optional)
    expand = 'expand_example' # str | A comma-separated list of properties that can reveal additional information in the response. (optional)
    sort = 'sort_example' # str | A comma-separated list of fields to sort by. Fields prefixed by a dash ( - ) sort in descending order. (optional)

    try:
        # List account members
        api_response = api_instance.get_members(limit=limit, offset=offset, filter=filter, expand=expand, sort=sort)
        print("The response of AccountMembersApi->get_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountMembersApi->get_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of members to return in the response. Defaults to 20. | [optional] 
 **offset** | **int**| Where to start in the list. This is for use with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 
 **filter** | **str**| A comma-separated list of filters. Each filter is of the form &#x60;field:value&#x60;. Supported fields are explained above. | [optional] 
 **expand** | **str**| A comma-separated list of properties that can reveal additional information in the response. | [optional] 
 **sort** | **str**| A comma-separated list of fields to sort by. Fields prefixed by a dash ( - ) sort in descending order. | [optional] 

### Return type

[**Members**](Members.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Members collection response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_member**
> Member patch_member(id, patch_operation)

Modify an account member


Update a single account member. Updating a member uses a [JSON patch](https://datatracker.ietf.org/doc/html/rfc6902) representation of the desired changes. To learn more, read [Updates](https://launchdarkly.com/docs/api#updates).

To update fields in the account member object that are arrays, set the `path` to the name of the field and then append `/<array index>`. Use `/0` to add to the beginning of the array. Use `/-` to add to the end of the array. For example, to add a new custom role to a member, use the following request body:

```
  [
    {
      "op": "add",
      "path": "/customRoles/0",
      "value": "some-role-id"
    }
  ]
```

You can update only an account member's role or custom role using a JSON patch. Members can update their own names and email addresses though the LaunchDarkly UI.

When SAML SSO or SCIM is enabled for the account, account members are managed in the Identity Provider (IdP). Requests to update account members will succeed, but the IdP will override the update shortly afterwards.


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.member import Member
from launchdarkly_api.models.patch_operation import PatchOperation
from launchdarkly_api.rest import ApiException
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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = launchdarkly_api.AccountMembersApi(api_client)
    id = 'id_example' # str | The member ID
    patch_operation = [{"op":"add","path":"/role","value":"writer"}] # List[PatchOperation] | 

    try:
        # Modify an account member
        api_response = api_instance.patch_member(id, patch_operation)
        print("The response of AccountMembersApi->patch_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountMembersApi->patch_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The member ID | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)|  | 

### Return type

[**Member**](Member.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Member response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_member_teams**
> Member post_member_teams(id, member_teams_post_input)

Add a member to teams

Add one member to one or more teams.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.member import Member
from launchdarkly_api.models.member_teams_post_input import MemberTeamsPostInput
from launchdarkly_api.rest import ApiException
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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = launchdarkly_api.AccountMembersApi(api_client)
    id = 'id_example' # str | The member ID
    member_teams_post_input = launchdarkly_api.MemberTeamsPostInput() # MemberTeamsPostInput | 

    try:
        # Add a member to teams
        api_response = api_instance.post_member_teams(id, member_teams_post_input)
        print("The response of AccountMembersApi->post_member_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountMembersApi->post_member_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The member ID | 
 **member_teams_post_input** | [**MemberTeamsPostInput**](MemberTeamsPostInput.md)|  | 

### Return type

[**Member**](Member.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Member response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Member not found |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_members**
> Members post_members(new_member_form)

Invite new members

Invite one or more new members to join an account. Each member is sent an invitation. Members with Admin or Owner roles may create new members, as well as anyone with a `createMember` permission for "member/\*". If a member cannot be invited, the entire request is rejected and no members are invited from that request.

Each member _must_ have an `email` field and either a `role` or a `customRoles` field. If any of the fields are not populated correctly, the request is rejected with the reason specified in the "message" field of the response.

Valid base role names that you can provide for the `role` field include `reader`, `writer`, `admin`, `owner/admin`, and `no_access`. To learn more about base roles, read [Organization roles](https://launchdarkly.com/docs/home/account/roles/organization-roles).

If you are using the `customRoles` field instead, you can provide the key for any role that you have created, or for any preset [organization role](https://launchdarkly.com/docs/home/account/roles/organization-roles) or [project role](https://launchdarkly.com/docs/home/account/roles/project-roles) provided by LaunchDarkly. Some preset roles additionally require that you specify `roleAttributes`. To learn more, read [Using role scope](https://launchdarkly.com/docs/home/account/roles/role-scope).

Requests to create account members will not work if SCIM is enabled for the account.

_No more than 50 members may be created per request._

A request may also fail because of conflicts with existing members. These conflicts are reported using the additional `code` and `invalid_emails` response fields with the following possible values for `code`:

- **email_already_exists_in_account**: A member with this email address already exists in this account.
- **email_taken_in_different_account**: A member with this email address exists in another account.
- **duplicate_email**s: This request contains two or more members with the same email address.

A request that fails for one of the above reasons returns an HTTP response code of 400 (Bad Request).


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.members import Members
from launchdarkly_api.models.new_member_form import NewMemberForm
from launchdarkly_api.rest import ApiException
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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = launchdarkly_api.AccountMembersApi(api_client)
    new_member_form = [launchdarkly_api.NewMemberForm()] # List[NewMemberForm] | 

    try:
        # Invite new members
        api_response = api_instance.post_members(new_member_form)
        print("The response of AccountMembersApi->post_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountMembersApi->post_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_member_form** | [**List[NewMemberForm]**](NewMemberForm.md)|  | 

### Return type

[**Members**](Members.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Member collection response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

