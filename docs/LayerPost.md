# LayerPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Unique identifier for the layer | 
**name** | **str** | Layer name | 
**description** | **str** | The checkout flow for the application | 

## Example

```python
from launchdarkly_api.models.layer_post import LayerPost

# TODO update the JSON string below
json = "{}"
# create an instance of LayerPost from a JSON string
layer_post_instance = LayerPost.from_json(json)
# print the JSON string representation of the object
print(LayerPost.to_json())

# convert the object into a dict
layer_post_dict = layer_post_instance.to_dict()
# create an instance of LayerPost from a dict
layer_post_from_dict = LayerPost.from_dict(layer_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


