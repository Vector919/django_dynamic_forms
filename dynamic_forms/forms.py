from django import forms
import json

class DynamicForm(forms.Form):

    def __init__(self, field_list, field_container, *args, **kwargs):
        """
        Creates the form given the field list and container
        """
        super(DynamicForm, self).__init__(*args, **kwargs)

        self.field_structure = []

        for field_name in field_list:
            field_data = getattr(field_container, field_name)[1]

            field_object = getattr(forms.fields, field_data['type'])(**field_data['kwargs'])
            self.fields[field_name] = field_object

            field_data['field_name'] = field_name
            self.field_structure.append(field_data)
    
    def to_json(self):
        """
        Dumps a JSON string representation of the form
        """
        return json.dumps(self.field_structure)
