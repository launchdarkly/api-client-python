# launchdarkly_api.TeamMembersApi

All URIs are relative to *https://app.launchdarkly.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_member**](TeamMembersApi.md#delete_member) | **DELETE** /members/{memberId} | Delete a team member by ID.
[**get_me**](TeamMembersApi.md#get_me) | **GET** /members/me | Get the current team member associated with the token
[**get_member**](TeamMembersApi.md#get_member) | **GET** /members/{memberId} | Get a single team member by ID.
[**get_members**](TeamMembersApi.md#get_members) | **GET** /members | Returns a list of all members in the account.
[**patch_member**](TeamMembersApi.md#patch_member) | **PATCH** /members/{memberId} | Modify a team member by ID.
[**post_members**](TeamMembersApi.md#post_members) | **POST** /members | Invite new members.


# **delete_member**
> delete_member(member_id)

Delete a team member by ID.

### Example
```python
from __future__ import print_function
import time
import launchdarkly_api
from launchdarkly_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = launchdarkly_api.TeamMembersApi(launchdarkly_api.ApiClient(configuration))
member_id = 'member_id_example' # str | The member ID.

try:
    # Delete a team member by ID.
    api_instance.delete_member(member_id)
except ApiException as e:
    print("Exception when calling TeamMembersApi->delete_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**| The member ID. | 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_me**
> Member get_me()

Get the current team member associated with the token

### Example
```python
from __future__ import print_function
import time
import launchdarkly_api
from launchdarkly_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = launchdarkly_api.TeamMembersApi(launchdarkly_api.ApiClient(configuration))

try:
    # Get the current team member associated with the token
    api_response = api_instance.get_me()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMembersApi->get_me: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Member**](Member.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_member**
> Member get_member(member_id)

Get a single team member by ID.

### Example
```python
from __future__ import print_function
import time
import launchdarkly_api
from launchdarkly_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = launchdarkly_api.TeamMembersApi(launchdarkly_api.ApiClient(configuration))
member_id = 'member_id_example' # str | The member ID.

try:
    # Get a single team member by ID.
    api_response = api_instance.get_member(member_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMembersApi->get_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**| The member ID. | 

### Return type

[**Member**](Member.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members**
> Members get_members(limit=limit, offset=offset, filter=filter, sort=sort)

Returns a list of all members in the account.

### Example
```python
from __future__ import print_function
import time
import launchdarkly_api
from launchdarkly_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = launchdarkly_api.TeamMembersApi(launchdarkly_api.ApiClient(configuration))
limit = 8.14 # float | The number of objects to return. Defaults to -1, which returns everything. (optional)
offset = 8.14 # float | Where to start in the list. This is for use with pagination. For example, an offset of 10 would skip the first 10 items and then return the next limit items. (optional)
filter = 'filter_example' # str | A comma-separated list of filters. Each filter is of the form field:value. (optional)
sort = 'sort_example' # str | A comma-separated list of fields to sort by. A field prefixed by a - will be sorted in descending order. (optional)

try:
    # Returns a list of all members in the account.
    api_response = api_instance.get_members(limit=limit, offset=offset, filter=filter, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMembersApi->get_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| The number of objects to return. Defaults to -1, which returns everything. | [optional] 
 **offset** | **float**| Where to start in the list. This is for use with pagination. For example, an offset of 10 would skip the first 10 items and then return the next limit items. | [optional] 
 **filter** | **str**| A comma-separated list of filters. Each filter is of the form field:value. | [optional] 
 **sort** | **str**| A comma-separated list of fields to sort by. A field prefixed by a - will be sorted in descending order. | [optional] 

### Return type

[**Members**](Members.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_member**
> Member patch_member(member_id, patch_delta)

Modify a team member by ID.

### Example
```python
from __future__ import print_function
import time
import launchdarkly_api
from launchdarkly_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = launchdarkly_api.TeamMembersApi(launchdarkly_api.ApiClient(configuration))
member_id = 'member_id_example' # str | The member ID.
patch_delta = [launchdarkly_api.PatchOperation()] # list[PatchOperation] | Requires a JSON Patch representation of the desired changes to the project. 'http://jsonpatch.com/'

try:
    # Modify a team member by ID.
    api_response = api_instance.patch_member(member_id, patch_delta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMembersApi->patch_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**| The member ID. | 
 **patch_delta** | [**list[PatchOperation]**](PatchOperation.md)| Requires a JSON Patch representation of the desired changes to the project. &#39;http://jsonpatch.com/&#39; | 

### Return type

[**Member**](Member.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_members**
> Members post_members(members_body)

Invite new members.

### Example
```python
from __future__ import print_function
import time
import launchdarkly_api
from launchdarkly_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = launchdarkly_api.TeamMembersApi(launchdarkly_api.ApiClient(configuration))
members_body = [launchdarkly_api.MembersBody()] # list[MembersBody] | New members to invite.

try:
    # Invite new members.
    api_response = api_instance.post_members(members_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMembersApi->post_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **members_body** | [**list[MembersBody]**](MembersBody.md)| New members to invite. | 

### Return type

[**Members**](Members.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

