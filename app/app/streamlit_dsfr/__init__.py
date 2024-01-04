import os
import streamlit.components.v1 as components

# Release flag constant. Set to True when releasing the component.
_RELEASE = False

supported_components = {
    'dsfr_alert': 'st_dsfr_alert',
    'dsfr_badge': 'st_dsfr_badge',
    'dsfr_breadcrumb': 'st_dsfr_breadcrumb',
    'dsfr_button': 'st_dsfr_button',
    'dsfr_input': 'st_dsfr_input',
}

if not _RELEASE:
    # When components are in development, we use `url` to tell Streamlit
    # that the component will be served by a local dev server.
    components_url = 'http://localhost:8000'
    for component in supported_components:
        globals()[f'_{component}_func'] = \
            components.declare_component(
                component,
                url = f'{components_url}/{supported_components[component]}',
            )
else:
    # When we are distributing a production version of the component, we
    # use `path` instead of `url`. This tells Streamlit to load the component
    # from the component build directory directly.
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, 'frontend')
    for component in supported_components:
        globals()[f'_{component}_func'] = \
            components.declare_component(
                component,
                path = os.path.join(build_dir, supported_components[component]),
            )


# Components wrapper functions for users

def dsfr_alert(label, key = None):
	component_value = _dsfr_alert_func(label = label, key = key, default = False)
	return component_value

def dsfr_badge(label, key = None):
	component_value = _dsfr_badge_func(label = label, key = key, default = False)
	return component_value

def dsfr_breadcrumb(label, items = None, key = None):
	component_value = _dsfr_breadcrumb_func(label = label, items = items, key = key, default = False)
	return component_value

def dsfr_button(label, key = None):
	component_value = _dsfr_button_func(label = label, key = key, default = False)
	return component_value

def dsfr_checkbox(label, value = None, key = None):
	component_value = _dsfr_checkbox_func(label = label, modelValue = value, key = key, default = False)
	return component_value

def dsfr_input(key = None):
	component_value = _dsfr_input_func(key = key, default = False)
	return component_value
