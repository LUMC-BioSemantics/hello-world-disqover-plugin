plugin_interface_version = 2

def meta_data():
    return {
        'id': 'hello-world-disqover-plugin',
        'name': 'Hello world',
        'description': 'Example plugin for DISQOVER',
        'type-id': 'instance-processor'
    }

def process_instances(log, **kwargs):
    log('Hello world')
    return {'result': 'Hello world'}
