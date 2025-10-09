# PaginatedLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | [**AiConfigsLink**](AiConfigsLink.md) |  | [optional] 
**last** | [**AiConfigsLink**](AiConfigsLink.md) |  | [optional] 
**next** | [**AiConfigsLink**](AiConfigsLink.md) |  | [optional] 
**prev** | [**AiConfigsLink**](AiConfigsLink.md) |  | [optional] 
**var_self** | [**AiConfigsLink**](AiConfigsLink.md) |  | 

## Example

```python
from launchdarkly_api.models.paginated_links import PaginatedLinks

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedLinks from a JSON string
paginated_links_instance = PaginatedLinks.from_json(json)
# print the JSON string representation of the object
print(PaginatedLinks.to_json())

# convert the object into a dict
paginated_links_dict = paginated_links_instance.to_dict()
# create an instance of PaginatedLinks from a dict
paginated_links_from_dict = PaginatedLinks.from_dict(paginated_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


