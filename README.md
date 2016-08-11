Django Dynamic Forms
====================

django_dynamic_forms is a library that allows you to generate django forms from a dynamic field structure.

Example
----------

```python
from dynamic_forms.forms import DynamicForm
class FieldContaier:
    """
    Super set of all your possible fields for this form.
    """
    user_name = ('user_name', {
        'type': 'CharField',
        'kwargs': {'label': 'User Name'}
    })

    github = ('github_account', {
        'type': 'CharField',
        'kwargs': {'label': 'Github Account', 'required': False}
    })

    gogs = ('gogs_account', {
        'type': 'CharField',
        'kwargs': {'label': 'Github Account', 'required': False}
    })

form_fields = ['user_name', 'password']

form = DynamicForm(form_fields, FieldContainer)
form.to_json() # JSON string representing form (for use in rendering)
```