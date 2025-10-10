# launchdarkly_api.AuditLogApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audit_log_entries**](AuditLogApi.md#get_audit_log_entries) | **GET** /api/v2/auditlog | List audit log entries
[**get_audit_log_entry**](AuditLogApi.md#get_audit_log_entry) | **GET** /api/v2/auditlog/{id} | Get audit log entry
[**post_audit_log_entries**](AuditLogApi.md#post_audit_log_entries) | **POST** /api/v2/auditlog | Search audit log entries


# **get_audit_log_entries**
> AuditLogEntryListingRepCollection get_audit_log_entries(before=before, after=after, q=q, limit=limit, spec=spec)

List audit log entries

Get a list of all audit log entries. The query parameters let you restrict the results that return by date ranges, resource specifiers, or a full-text search query.

LaunchDarkly uses a resource specifier syntax to name resources or collections of resources. To learn more, read [About the resource specifier syntax](https://launchdarkly.com/docs/home/account/role-resources#about-the-resource-specifier-syntax).


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.audit_log_entry_listing_rep_collection import AuditLogEntryListingRepCollection
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
    api_instance = launchdarkly_api.AuditLogApi(api_client)
    before = 56 # int | A timestamp filter, expressed as a Unix epoch time in milliseconds.  All entries this returns occurred before the timestamp. (optional)
    after = 56 # int | A timestamp filter, expressed as a Unix epoch time in milliseconds. All entries this returns occurred after the timestamp. (optional)
    q = 'q_example' # str | Text to search for. You can search for the full or partial name of the resource. (optional)
    limit = 56 # int | A limit on the number of audit log entries that return. Set between 1 and 20. The default is 10. (optional)
    spec = 'spec_example' # str | A resource specifier that lets you filter audit log listings by resource (optional)

    try:
        # List audit log entries
        api_response = api_instance.get_audit_log_entries(before=before, after=after, q=q, limit=limit, spec=spec)
        print("The response of AuditLogApi->get_audit_log_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogApi->get_audit_log_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **before** | **int**| A timestamp filter, expressed as a Unix epoch time in milliseconds.  All entries this returns occurred before the timestamp. | [optional] 
 **after** | **int**| A timestamp filter, expressed as a Unix epoch time in milliseconds. All entries this returns occurred after the timestamp. | [optional] 
 **q** | **str**| Text to search for. You can search for the full or partial name of the resource. | [optional] 
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

Fetch a detailed audit log entry representation. The detailed representation includes several fields that are not present in the summary representation, including:

- `previousVersion`: a JSON representation of the previous version of the entity.
- `currentVersion`: a JSON representation of the current version of the entity.
- `delta`: the JSON patch body that was used in the request to update the entity. This is only included if the update was made through a [JSON patch](https://launchdarkly.com/docs/api#updates-using-json-patch). It is null when the update was made using [semantic patch](https://launchdarkly.com/docs/api#updates-using-semantic-patch). Because most [flag updates](https://launchdarkly.com/docs/api/feature-flags/patch-feature-flag) are made using semantic patch, this field is rarely returned.


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.audit_log_entry_rep import AuditLogEntryRep
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
    api_instance = launchdarkly_api.AuditLogApi(api_client)
    id = 'id_example' # str | The ID of the audit log entry

    try:
        # Get audit log entry
        api_response = api_instance.get_audit_log_entry(id)
        print("The response of AuditLogApi->get_audit_log_entry:\n")
        pprint(api_response)
    except Exception as e:
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

# **post_audit_log_entries**
> AuditLogEntryListingRepCollection post_audit_log_entries(before=before, after=after, q=q, limit=limit, statement_post=statement_post)

Search audit log entries

Search your audit log entries. The query parameters let you restrict the results that return by date ranges, or a full-text search query. The request body lets you restrict the results that return by resource specifiers.

LaunchDarkly uses a resource specifier syntax to name resources or collections of resources. To learn more, read [About the resource specifier syntax](https://launchdarkly.com/docs/home/account/role-resources#about-the-resource-specifier-syntax).


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.audit_log_entry_listing_rep_collection import AuditLogEntryListingRepCollection
from launchdarkly_api.models.statement_post import StatementPost
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
    api_instance = launchdarkly_api.AuditLogApi(api_client)
    before = 56 # int | A timestamp filter, expressed as a Unix epoch time in milliseconds.  All entries returned occurred before the timestamp. (optional)
    after = 56 # int | A timestamp filter, expressed as a Unix epoch time in milliseconds. All entries returned occurred after the timestamp. (optional)
    q = 'q_example' # str | Text to search for. You can search for the full or partial name of the resource. (optional)
    limit = 56 # int | A limit on the number of audit log entries that return. Set between 1 and 20. The default is 10. (optional)
    statement_post = [launchdarkly_api.StatementPost()] # List[StatementPost] |  (optional)

    try:
        # Search audit log entries
        api_response = api_instance.post_audit_log_entries(before=before, after=after, q=q, limit=limit, statement_post=statement_post)
        print("The response of AuditLogApi->post_audit_log_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogApi->post_audit_log_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **before** | **int**| A timestamp filter, expressed as a Unix epoch time in milliseconds.  All entries returned occurred before the timestamp. | [optional] 
 **after** | **int**| A timestamp filter, expressed as a Unix epoch time in milliseconds. All entries returned occurred after the timestamp. | [optional] 
 **q** | **str**| Text to search for. You can search for the full or partial name of the resource. | [optional] 
 **limit** | **int**| A limit on the number of audit log entries that return. Set between 1 and 20. The default is 10. | [optional] 
 **statement_post** | [**List[StatementPost]**](StatementPost.md)|  | [optional] 

### Return type

[**AuditLogEntryListingRepCollection**](AuditLogEntryListingRepCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
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

