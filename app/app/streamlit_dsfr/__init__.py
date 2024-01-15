import os
from typing import Optional, Union

import streamlit.components.v1 as components

# Release flag constant. Set to True when releasing the component.
_RELEASE = False

supported_components = {
    'dsfr_default': 'st_dsfr_default',
    'dsfr_alert': 'st_dsfr_alert',
    'dsfr_badge': 'st_dsfr_badge',
    'dsfr_breadcrumb': 'st_dsfr_breadcrumb',
    'dsfr_button': 'st_dsfr_button',
	'dsfr_checkbox': 'st_dsfr_checkbox',
    'dsfr_input': 'st_dsfr_input',
	'dsfr_picture': 'st_dsfr_picture',
    'dsfr_radio': 'st_dsfr_radio',
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

def dsfr_alert(
	title: str,
	description: Optional[str] = None,
	type: Optional[str] = None,
	small: Optional[bool] = None,
	*,
	closed: Optional[bool] = None,
	closeable: Optional[bool] = None,
	titleTag: Optional[str] = None,
	id: Optional[str] = None,
	key: Optional[str] = None,
	**kwargs,
):
	if description is not None:
		kwargs['description'] = description
	if type is not None:
		kwargs['type'] = type
	if small is not None:
		kwargs['small'] = small
		if small and description is None:
			kwargs['description'] = title
			title = None
	if closed is not None:
		kwargs['closed'] = closed
	if closeable is not None:
		kwargs['closeable'] = closeable
	if titleTag is not None:
		kwargs['titleTag'] = titleTag
	if id is not None:
		kwargs['id'] = id

	return _dsfr_alert_func(title = title, **kwargs, key = key, default = None)

def dsfr_badge(
	label: str,
	type: Optional[str] = None,
	small: Optional[bool] = None,
	*,
	noIcon: Optional[bool] = None,
	ellipsis: Optional[bool] = None,
	key: Optional[str] = None,
	**kwargs,
):
	if type is not None:
		kwargs['type'] = type
	if small is not None:
		kwargs['small'] = small
	if noIcon is not None:
		kwargs['noIcon'] = noIcon
	if ellipsis is not None:
		kwargs['ellipsis'] = ellipsis

	return _dsfr_badge_func(label = label, **kwargs, key = key, default = None)

def dsfr_breadcrumb(
	links: str | list[str] | list[(str, str)] | list[dict[str, str]] | None = None,
	*,
	id: Optional[str] = None,
	key: Optional[str] = None,
	**kwargs,
):
	if links is not None:
		if isinstance(links, str):
			kwargs['links'] = [{'to': links, 'text': links}]
		elif isinstance(links, list):
			def item_to_dict(item):
				if isinstance(item, str):
					return {'to': item, 'text': item}
				elif isinstance(item, tuple):
					return {'to': item[0], 'text': item[1]}
				elif isinstance(item, dict):
					return item
				else:
					raise ValueError('links must be a list of strings, tuples or dicts')
			kwargs['links'] = [item_to_dict(item) for item in links]
		else:
			raise ValueError('links must be a list of strings, tuples or dicts')

	if id is not None:
		kwargs['breadcrumbId'] = id

	return _dsfr_breadcrumb_func(**kwargs, key = key, default = False)

def dsfr_button(
	label: str,
	size: Optional[str] = None,
	disabled: Optional[bool] = None,
	*,
	secondary: Optional[bool] = None,
	tertiary: Optional[bool] = None,
	icon: Optional[str] = None,
	iconOnly: Optional[bool] = None,
	iconRight: Optional[bool] = None,
	noOutline: Optional[bool] = None,
	key: Optional[str] = None,
	**kwargs,
):
	if size is not None:
		kwargs['size'] = size
	if disabled is not None:
		kwargs['disabled'] = disabled
	if secondary is not None:
		kwargs['secondary'] = secondary
	if tertiary is not None:
		kwargs['tertiary'] = tertiary
	if icon is not None:
		kwargs['icon'] = icon
	if iconOnly is not None:
		kwargs['iconOnly'] = iconOnly
	if iconRight is not None:
		kwargs['iconRight'] = iconRight
	if noOutline is not None:
		kwargs['noOutline'] = noOutline

	return _dsfr_button_func(label = label, **kwargs, key = key, default = False)

def dsfr_checkbox(
	hint: Optional[str] = None,
	small: Optional[bool] = None,
	required: Optional[bool] = None,
	name: Optional[str] = None,
	value: Optional[bool] = None,
	*,
	id: Optional[str] = None,
	inline: Optional[bool] = None,
	errorMessage: Optional[str] = None,
	validMessage: Optional[str] = None,
	key: Optional[str] = None,
	**kwargs,
):
	if hint is not None:
		kwargs['hint'] = hint
	if small is not None:
		kwargs['small'] = small
	if required is not None:
		kwargs['required'] = required
	if name is not None:
		kwargs['name'] = name
	if value is not None:
		kwargs['modelValue'] = value
	if id is not None:
		kwargs['id'] = id
	if inline is not None:
		kwargs['inline'] = inline
	if errorMessage is not None:
		kwargs['errorMessage'] = errorMessage
	if validMessage is not None:
		kwargs['validMessage'] = validMessage

	return _dsfr_checkbox_func(**kwargs, key = key, default = False)

def dsfr_input(
	label: str,
	hint: Optional[str] = None,
	value: Optional[str] = None,
	*,
	labelVisible: Optional[bool] = None,
	id: Optional[str] = None,
	descriptionId: Optional[str] = None,
	isInvalid: Optional[bool] = None,
	isValid: Optional[bool] = None,
	isWithWarning: Optional[bool] = None,
	labelClass: Optional[str] = None,
	wrapperClass: Optional[str] = None,
	requiredTip: Optional[str] = None,
	key: Optional[str] = None,
	**kwargs,
):
	if hint is not None:
		kwargs['hint'] = hint
	if value is not None:
		kwargs['modelValue'] = value
	if labelVisible is not None:
		kwargs['labelVisible'] = labelVisible
	else:
		kwargs['labelVisible'] = not not label
	if id is not None:
		kwargs['id'] = id
	if descriptionId is not None:
		kwargs['descriptionId'] = descriptionId
	if isInvalid is not None:
		kwargs['isInvalid'] = isInvalid
	if isValid is not None:
		kwargs['isValid'] = isValid
	if isWithWarning is not None:
		kwargs['isWithWarning'] = isWithWarning
	if labelClass is not None:
		kwargs['labelClass'] = labelClass
	if wrapperClass is not None:
		kwargs['wrapperClass'] = wrapperClass
	if requiredTip is not None:
		kwargs['requiredTip'] = requiredTip

	return _dsfr_input_func(label = label, **kwargs, key = key, default = value)

def dsfr_picture(
	src: str,
	size: Optional[str] = None,
	*,
	alt: Optional[str] = None,
	title: Optional[str] = None,
	legend: Optional[str] = None,
	ratio: Optional[str] = None,
	key: Optional[str] = None,
	**kwargs,
):
	if size is not None:
		kwargs['size'] = size
	if alt is not None:
		kwargs['alt'] = alt
	if title is not None:
		kwargs['title'] = title
	if legend is not None:
		kwargs['legend'] = legend
	if ratio is not None:
		kwargs['ratio'] = ratio

	return _dsfr_picture_func(src = src, **kwargs, key = key, default = None)

def dsfr_radio(
	options: Union[list[str], list[dict[str, str]]],
	index: Optional[int] = None,
	*,
	inline: Optional[bool] = None,
	small: Optional[bool] = None,
	titleId: Optional[str] = None,
	disabled: Optional[Union[bool, list[bool]]] = None,
	required: Optional[bool] = None,
	name: Optional[str] = None,
	errorMessage: Optional[str] = None,
	validMessage: Optional[str] = None,
	legend: Optional[str] = None,
	requiredTip: Optional[str] = None,
	default: Optional[int] = None,
	hints: Optional[list[str]] = None,
	key: Optional[str] = None,
	**kwargs,
):
	if inline is not None:
		kwargs['inline'] = inline
	if small is not None:
		kwargs['small'] = small
	if titleId is not None:
		kwargs['titleId'] = titleId
	if required is not None:
		kwargs['required'] = required
	if name is not None:
		kwargs['name'] = name
	if errorMessage is not None:
		kwargs['errorMessage'] = errorMessage
	if validMessage is not None:
		kwargs['validMessage'] = validMessage
	if legend is not None:
		kwargs['legend'] = legend
	if requiredTip is not None:
		kwargs['requiredTip'] = requiredTip
	if default is not None:
		kwargs['value'] = default

	if not isinstance(options, list):
		options = [options]

	lenoptions = len(options)
	if lenoptions <= 0:
		kwargs['options'] = []
	elif isinstance(options[0], dict):
		kwargs['options'] = options
	elif isinstance(options[0], str):
		kwargs['options'] = [
			{
				'label': option,
				'value': str(index),
			}
			for index, option in enumerate(options)
		]
	else:
		raise ValueError('options must be a list of strings or dicts')

	if disabled is not None:
		if isinstance(disabled, bool):
			kwargs['disabled'] = disabled
		elif isinstance(disabled, list):
			if len(disabled) > len(kwargs['options']):
				raise ValueError('disabled as a list cannot be longer than options')
			for index, value in enumerate(disabled):
				kwargs['options'][index]['disabled'] = value
		else:
			raise ValueError('disabled must be a bool or a list of bools')

	if hints is not None:
		if len(hints) > len(kwargs['options']):
			raise ValueError('hints cannot be longer than options')
		for index, value in enumerate(hints):
			kwargs['options'][index]['hint'] = value

	if index is not None:
		kwargs['modelValue'] = str(index)
		default = index
	elif lenoptions > 0:
		kwargs['modelValue'] = '0'
		default = 0
	else:
		default = None

	return _dsfr_radio_func(**kwargs, key = key, default = default)
