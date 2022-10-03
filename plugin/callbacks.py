plugin_interface_version = 2

def meta_data():
    return {
        'id': 'hello-world-disqover-plugin',
        'name': 'Hello world',
        'description': 'Example plugin for DISQOVER',
        'type-id': 'instance-processor'
    }

def global_options_definition():
    return [{
        'content_type': 'text',
        'id': 'global_text_value',
        'name': 'Value',
        'description': 'Enter a value'
    }]

def session_options_definition():
    return [{
        'content_type': 'text',
        'id': 'hello_text',
        'name': 'Name',
        'description': 'Enter your name here'

    }, {
        'content_type': 'bool',
        'id': 'hello_bool',
        'name': 'Export',
        'description': 'Would you like to export?'

    }, {
        'content_type': 'url',
        'id': 'hello_url',
        'name': 'Hello website',
        'description': 'Enter your url here.'
    }]

def process_instances(log, options_values, **kwargs):
    log('Hello world')
    return {'message': f'Hello {options_values["hello_text"]}: {options_values["global_text_value"]}'}
