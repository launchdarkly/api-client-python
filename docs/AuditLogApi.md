# launchdarkly_api.AuditLogApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audit_log_entries**](AuditLogApi.md#get_audit_log_entries) | **GET** /api/v2/auditlog | List audit log entries
[**get_audit_log_entry**](AuditLogApi.md#get_audit_log_entry) | **GET** /api/v2/auditlog/{id} | Get audit log entry


# **get_audit_log_entries**
> AuditLogEntryListingRepCollection get_audit_log_entries()

List audit log entries

Get a list of all audit log entries. The query parameters let you restrict the results that return by date ranges, resource specifiers, or a full-text search query.  LaunchDarkly uses a resource specifier syntax to name resources or collections of resources. To learn more, read [Understanding the resource specifier syntax](https://docs.launchdarkly.com/home/members/role-resources#understanding-the-resource-specifier-syntax). 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import audit_log_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.audit_log_entry_listing_rep_collection import AuditLogEntryListingRepCollection
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
    api_instance = audit_log_api.AuditLogApi(api_client)
    before = 1 # int | A timestamp filter, expressed as a Unix epoch time in milliseconds.  All entries this returns occurred before the timestamp. (optional)
    after = 1 # int | A timestamp filter, expressed as a Unix epoch time in milliseconds. All entries this returns occurred after the timestamp. (optional)
    q = "q_example" # str | Text to search for. You can search for the full or partial name of the resource, or full or partial email address of the member who made a change. (optional)
    limit = 1 # int | A limit on the number of audit log entries that return. Set between 1 and 20. The default is 10. (optional)
    spec = "spec_example" # str | A resource specifier that lets you filter audit log listings by resource (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List audit log entries
        api_response = api_instance.get_audit_log_entries(before=before, after=after, q=q, limit=limit, spec=spec)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AuditLogApi->get_audit_log_entries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **before** | **int**| A timestamp filter, expressed as a Unix epoch time in milliseconds.  All entries this returns occurred before the timestamp. | [optional]
 **after** | **int**| A timestamp filter, expressed as a Unix epoch time in milliseconds. All entries this returns occurred after the timestamp. | [optional]
 **q** | **str**| Text to search for. You can search for the full or partial name of the resource, or full or partial email address of the member who made a change. | [optional]
 **limit** | **int**| A limit on the number of audit log entries that return. Set between 1 and 20. The default is 10. | [optional]
 **spec** | **str**| A resource specifier that lets you filter audit log listings by resource | [optional]

### Return type

[**AuditLogEntryListingRepCollection**](AuditLogEntryListingRepCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audit log entries response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_log_entry**
> AuditLogEntryRep get_audit_log_entry(id)

Get audit log entry

Fetch a detailed audit log entry representation. The detailed representation includes several fields that are not present in the summary representation, including:  - `delta`: the JSON patch body that was used in the request to update the entity - `previousVersion`: a JSON representation of the previous version of the entity - `currentVersion`: a JSON representation of the current version of the entity 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import audit_log_api
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.audit_log_entry_rep import AuditLogEntryRep
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
    api_instance = audit_log_api.AuditLogApi(api_client)
    id = "id_example" # str | The ID of the audit log entry

    # example passing only required values which don't have defaults set
    try:
        # Get audit log entry
        api_response = api_instance.get_audit_log_entry(id)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AuditLogApi->get_audit_log_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the audit log entry |

### Return type

[**AuditLogEntryRep**](AuditLogEntryRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audit log entry response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

