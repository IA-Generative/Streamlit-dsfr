import os
from typing import Optional, Union, Iterable, Callable
import json
import base64
import hashlib
from io import BytesIO

import streamlit.components.v1 as components
from streamlit.runtime.uploaded_file_manager import UploadedFile, UploadedFileRec
from streamlit.proto.Common_pb2 import FileURLs as FileURLsProto

# Release flag constant. Set to True when releasing the component.
_RELEASE = False

supported_components = {
    'dsfr_default': 'st_dsfr_default',
    'dsfr_alert': 'st_dsfr_alert',
    'dsfr_badge': 'st_dsfr_badge',
    'dsfr_breadcrumb': 'st_dsfr_breadcrumb',
    'dsfr_button': 'st_dsfr_button',
    'dsfr_buttons_group': 'st_dsfr_buttons_group',
	'dsfr_checkbox': 'st_dsfr_checkbox',
	'dsfr_file_upload': 'st_dsfr_file_upload',
    'dsfr_input': 'st_dsfr_input',
	'dsfr_picture': 'st_dsfr_picture',
    'dsfr_radio': 'st_dsfr_radio',
	'dsfr_range': 'st_dsfr_range',
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

def alert(
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

dsfr_alert = alert

def badge(
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

dsfr_badge = badge

def breadcrumb(
	links: Optional[Union[str, list[str], list[tuple[str, str]], list[dict[str, str]]]] = None,
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

dsfr_breadcrumb = breadcrumb

def button(
	label: str, # Standard
	key: Optional[Union[str, int]] = None, # Standard
	# help: Optional[str] = None, # Standard
	size: Optional[str] = None,
	# on_click: Optional[Callable] = None, # Standard
	# args: Optional[tuple] = None, # Standard
	# kwargs: Optional[dict] = None, # Standard
	*,
	type: Optional[str] = None, # Standard
	disabled: Optional[bool] = None, # Standard
	# use_container_width: Optional[bool] = None, # Standard
	secondary: Optional[bool] = None,
	tertiary: Optional[bool] = None,
	icon: Optional[str] = None,
	iconOnly: Optional[bool] = None,
	iconRight: Optional[bool] = None,
	noOutline: Optional[bool] = None,
	**kwargs,
):
	"""
	Streamlit DSFR Button component

	Streamlit standard component equivalent:
	https://docs.streamlit.io/library/api-reference/widgets/st.button
	"""
	kwargs['label'] = label

	if size is not None:
		kwargs['size'] = size

	if disabled is not None:
		kwargs['disabled'] = disabled

	if type is not None:
		if type == 'secondary':
			kwargs['secondary'] = True
		elif type == 'tertiary':
			kwargs['tertiary'] = True
	else:
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

	return _dsfr_button_func(**kwargs, key = key, default = False)

dsfr_button = button

def link_button(
	label: str, # Standard
	url: str, # Standard
	*,
	key: Optional[Union[str, int]] = None,
	help: Optional[str] = None, # Standard
	type: Optional[str] = None, # Standard # 'primary' | 'secondary'
	disabled: Optional[bool] = None, # Standard
	use_container_width: Optional[bool] = None, # Standard
):
	"""
	Streamlit DSFR Link Button component

	Streamlit standard component equivalent:
	https://docs.streamlit.io/library/api-reference/widgets/st.link_button
	"""
	return button(
		label = label,
		key = key,
		help = help,
		type = type,
		disabled = disabled,
		use_container_width = use_container_width,
		link = url,
	)

dsfr_link_button = link_button

def copy_button(
	label: str,
	content: str,
	*,
	key: Optional[Union[str, int]] = None,
	help: Optional[str] = None,
	type: Optional[str] = None, # 'primary' | 'secondary'
	disabled: Optional[bool] = None,
	use_container_width: Optional[bool] = None,
):
	"""
	Streamlit DSFR Copy Button component
	"""
	return button(
		label = label,
		key = key,
		help = help,
		type = type,
		disabled = disabled,
		use_container_width = use_container_width,
		copy = content,
	)

dsfr_copy_button = copy_button

def buttons_group(
	labels: Iterable[str],
	key: Optional[Union[str, int]] = None,
	inline: Optional[bool] = None,
	size: Optional[str] = None,
	*,
	disabled: Union[Optional[bool], list[Optional[bool]]] = None,
	# Buttons
	type: Union[Optional[str], list[Optional[str]]] = None,
	secondary: Union[Optional[bool], list[Optional[bool]]] = None,
	tertiary: Union[Optional[bool], list[Optional[bool]]] = None,
	icon: Union[Optional[str], list[Optional[str]]] = None,
	iconOnly: Union[Optional[bool], list[Optional[bool]]] = None,
	noOutline: Union[Optional[bool], list[Optional[bool]]] = None,
	link: Union[Optional[str], list[Optional[str]]] = None,
	copy: Union[Optional[str], list[Optional[str]]] = None,
	# Group
	align: Optional[str] = None,
	reverse: Optional[bool] = None,
	iconRight: Optional[bool] = None,
	equisized: Optional[bool] = None,
	**kwargs,
):
	"""
	Streamlit DSFR Button component

	Streamlit standard component equivalent:
	https://docs.streamlit.io/library/api-reference/widgets/st.button
	"""

	buttons = []

	if isinstance(labels, str):
		labels = [labels]
	for label in labels:
		buttons.append({
			'label': label,
		})

	if type is not None:
		if isinstance(type, list):
			for i, each in enumerate(type):
				if each == 'secondary':
					kwargs['secondary'] = True
				elif each == 'tertiary':
					kwargs['tertiary'] = True
		else:
			for button in buttons:
				if type == 'secondary':
					kwargs['secondary'] = True
				elif type == 'tertiary':
					kwargs['tertiary'] = True
	else:
		if secondary is not None:
			if isinstance(secondary, list):
				for i, each in enumerate(secondary):
					if each is not None:
						buttons[i]['secondary'] = each
			else:
				for button in buttons:
					button['secondary'] = secondary
		if tertiary is not None:
			if isinstance(tertiary, list):
				for i, each in enumerate(tertiary):
					if each is not None:
						buttons[i]['tertiary'] = each
			else:
				for button in buttons:
					button['tertiary'] = tertiary

	if disabled is not None:
		if isinstance(disabled, list):
			for i, each in enumerate(disabled):
				if each is not None:
					buttons[i]['disabled'] = each
		else:
			for button in buttons:
				button['disabled'] = disabled

	if icon is not None:
		if isinstance(icon, list):
			for i, each in enumerate(icon):
				if each is not None:
					buttons[i]['icon'] = each
		else:
			for button in buttons:
				button['icon'] = icon

	if iconOnly is not None:
		if isinstance(iconOnly, list):
			for i, each in enumerate(iconOnly):
				if each is not None:
					buttons[i]['iconOnly'] = each
		else:
			for button in buttons:
				button['iconOnly'] = iconOnly

	if noOutline is not None:
		if isinstance(noOutline, list):
			for i, each in enumerate(noOutline):
				if each is not None:
					buttons[i]['noOutline'] = each
		else:
			for button in buttons:
				button['noOutline'] = noOutline

	if link is not None:
		if isinstance(link, list):
			for i, each in enumerate(link):
				if each is not None:
					buttons[i]['link'] = each
		else:
			for button in buttons:
				button['link'] = link

	if copy is not None:
		if isinstance(copy, list):
			for i, each in enumerate(copy):
				if each is not None:
					buttons[i]['copy'] = each
		else:
			for button in buttons:
				button['copy'] = copy

	kwargs['buttons'] = buttons

	if align is not None:
		kwargs['align'] = align
	if inline is not None:
		kwargs['inlineLayoutWhen'] = 'always' if inline else 'never'
	if reverse is not None:
		kwargs['reverse'] = reverse
	if iconRight is not None:
		kwargs['iconRight'] = iconRight
	if size is not None:
		kwargs['size'] = size
	if equisized is not None:
		kwargs['equisized'] = equisized

	return _dsfr_buttons_group_func(**kwargs, key = key, default = [False for _ in buttons])

dsfr_buttons_group = buttons_group

def checkbox(
	label: str, # Standard
	value: Optional[bool] = None, # Standard
	key: Optional[Union[str, int]] = None, # Standard
	help: Optional[str] = None, # Standard
	small: Optional[bool] = None,
	required: Optional[bool] = None,
	name: Optional[str] = None,
	# on_change: Optional[Callable] = None, # Standard
	# args: Optional[tuple] = None, # Standard
	# kwargs: Optional[dict] = None, # Standard
	*,
	disabled: Optional[bool] = None, # Standard
	# label_visibility: Optional[str] = None, # Standard
	id: Optional[str] = None,
	inline: Optional[bool] = None,
	errorMessage: Optional[str] = None,
	validMessage: Optional[str] = None,
	**kwargs,
):
	"""
	Streamlit DSFR Checkbox component

	Streamlit standard component equivalent:
	https://docs.streamlit.io/library/api-reference/widgets/st.checkbox
	"""
	kwargs['label'] = label

	if value is not None:
		kwargs['modelValue'] = value
	else:
		kwargs['modelValue'] = False

	if help is not None:
		kwargs['hint'] = help

	if small is not None:
		kwargs['small'] = small
	if required is not None:
		kwargs['required'] = required
	if name is not None:
		kwargs['name'] = name

	if disabled is not None:
		kwargs['disabled'] = disabled

	if id is not None:
		kwargs['id'] = id
	if inline is not None:
		kwargs['inline'] = inline
	if errorMessage is not None:
		kwargs['errorMessage'] = errorMessage
	if validMessage is not None:
		kwargs['validMessage'] = validMessage

	return _dsfr_checkbox_func(**kwargs, key = key, default = kwargs['modelValue'])

dsfr_checkbox = checkbox

_ext2mimeTypes = None

def ext2mimeTypes():
	global _ext2mimeTypes
	if _ext2mimeTypes is None:
		with open(os.path.join(os.path.dirname(__file__), 'mimeTypes.json'), 'r') as f:
			_ext2mimeTypes = json.load(f)
	return _ext2mimeTypes

def file_uploader(
	label: str, # Standard
	type: Optional[Union[str, list[str]]] = None, # Standard # extensions, e.g. ['png', 'jpg']
	# accept_multiple_files: Optional[bool] = None, # Standard
	key: Optional[Union[str, int]] = None, # Standard
	help: Optional[str] = None, # Standard
	# on_change: Optional[Callable] = None, # Standard
	# args: Optional[tuple] = None, # Standard
	# kwargs: Optional[dict] = None, # Standard
	*,
	disabled: Optional[bool] = None, # Standard
	# label_visibility: Optional[str] = None, # Standard
	id: Optional[str] = None,
	hint: Optional[str] = None, # Alias for 'help'
	error: Optional[str] = None,
	validMessage: Optional[str] = None,
	# modelValue: Optional[str] = None,
	**kwargs,
):
	"""
	Streamlit DSFR Checkbox component

	Streamlit standard component equivalent:
	https://docs.streamlit.io/library/api-reference/widgets/st.checkbox
	"""
	kwargs['label'] = label

	if help is not None:
		kwargs['hint'] = help
	elif hint is not None:
		kwargs['hint'] = hint

	# Convert type to list of MimeTypes
	if type is not None:
		if isinstance(type, str):
			type = [type]
		_ext2mimeTypesDict = ext2mimeTypes()
		accept = [
			_ext2mimeTypesDict[f'.{ext}']
			for ext in type
		]
		kwargs['accept'] = accept

	if disabled is not None:
		kwargs['disabled'] = disabled

	if id is not None:
		kwargs['id'] = id
	if error is not None:
		kwargs['error'] = error
	if validMessage is not None:
		kwargs['validMessage'] = validMessage

	file = _dsfr_file_upload_func(**kwargs, key = key, default = None)

	if not file:
		return None

	id = hashlib.sha256(file['data'].encode('utf-8')).hexdigest()

	return UploadedFile(
		UploadedFileRec(
			file_id = id,
			name = file['name'],
			type = file['type'],
			data = base64.b64decode(file['data']), # Decode bytes
		),
		FileURLsProto(
			file_id = id,
			delete_url = None, # ?
			upload_url = None, # ?
		),
	)

dsfr_file_upload = file_uploader
dsfr_file_uploader = file_uploader

def input(
	label: str, # Standard
	value: Optional[str] = None, # Standard
	# max_chars: Optional[int] = None, # Standard
	key: Optional[Union[str, int]] = None, # Standard
	type: Optional[str] = None, # Semi-standard
	help: Optional[str] = None, # Standard
	# autocomplete: Optional[str] = None, # Standard
	# on_change: Optional[Callable] = None, # Standard
	# args: Optional[tuple] = None, # Standard
	# kwargs: Optional[dict] = None, # Standard
	*,
	placeholder: Optional[str] = None, # Standard
	disabled: Optional[bool] = None, # Standard
	# label_visibility: Optional[str] = None, # 'visible' (default), 'hidden', 'collapse' # Standard
	hint: Optional[str] = None, # Alias for 'help'
	labelVisible: Optional[bool] = None,
	id: Optional[str] = None,
	descriptionId: Optional[str] = None,
	isInvalid: Optional[bool] = None,
	isValid: Optional[bool] = None,
	isTextarea: Optional[bool] = None,
	isWithWarning: Optional[bool] = None,
	labelClass: Optional[str] = None,
	wrapperClass: Optional[str] = None,
	requiredTip: Optional[str] = None,
	height: Optional[int] = None,
	**kwargs,
):
	"""
	Streamlit DSFR Input component
	"""
	kwargs['label'] = label

	if value is not None:
		kwargs['modelValue'] = value
	else:
		kwargs['modelValue'] = ''

	if help is not None:
		kwargs['hint'] = help
	elif hint is not None:
		kwargs['hint'] = hint

	if placeholder is not None:
		kwargs['placeholder'] = placeholder

	if disabled is not None:
		kwargs['disabled'] = disabled

	if type is not None:
		if type == 'default':
			kwargs['type'] = 'text'
		kwargs['type'] = type

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
	if isTextarea is not None:
		kwargs['isTextarea'] = isTextarea
	if isWithWarning is not None:
		kwargs['isWithWarning'] = isWithWarning
	if labelClass is not None:
		kwargs['labelClass'] = labelClass
	if wrapperClass is not None:
		kwargs['wrapperClass'] = wrapperClass
	if requiredTip is not None:
		kwargs['requiredTip'] = requiredTip
	if height is not None:
		kwargs['height'] = height

	return _dsfr_input_func(**kwargs, key = key, default = kwargs['modelValue'])

dsfr_input = input

def text_input(
	label: str, # Standard
	value: Optional[str] = None, # Standard
	# max_chars: Optional[int] = None, # Standard
	key: Optional[Union[str, int]] = None, # Standard
	type: Optional[str] = None, # 'default' | 'password' # Standard
	help: Optional[str] = None, # Standard
	# autocomplete: Optional[str] = None, # Standard
	# on_change: Optional[Callable] = None, # Standard
	# args: Optional[tuple] = None, # Standard
	# kwargs: Optional[dict] = None, # Standard
	*,
	placeholder: Optional[str] = None, # Standard
	disabled: Optional[bool] = None, # Standard
	# label_visibility: Optional[str] = None, # 'visible' (default), 'hidden', 'collapse' # Standard
	hint: Optional[str] = None, # Alias for 'help'
	labelVisible: Optional[bool] = None,
	id: Optional[str] = None,
	descriptionId: Optional[str] = None,
	isInvalid: Optional[bool] = None,
	isValid: Optional[bool] = None,
	isWithWarning: Optional[bool] = None,
	labelClass: Optional[str] = None,
	wrapperClass: Optional[str] = None,
	requiredTip: Optional[str] = None,
	**kwargs,
):
	"""
	Streamlit DSFR Text Input component

	Streamlit standard component equivalent:
	https://docs.streamlit.io/library/api-reference/widgets/st.text_input
	"""
	if value is None:
		value = ''

	return dsfr_input(
		label = label,
		value = value,
		key = key,
		type = type,
		help = help,
		placeholder = placeholder,
		disabled = disabled,
		hint = hint,
		labelVisible = labelVisible,
		id = id,
		descriptionId = descriptionId,
		isInvalid = isInvalid,
		isValid = isValid,
		isTextarea = False,
		isWithWarning = isWithWarning,
		labelClass = labelClass,
		wrapperClass = wrapperClass,
		requiredTip = requiredTip,
		**kwargs,
	)

dsfr_text_input = text_input

def number_input(
	label: str, # Standard
	min_value: Optional[Union[int, float]] = None, # Standard
	max_value: Optional[Union[int, float]] = None, # Standard
	value: Optional[Union[int, float]] = None, # Standard
	step: Optional[Union[int, float]] = None, # Standard
	# format: Optional[str] = None, # Standard
	key: Optional[Union[str, int]] = None, # Standard
	help: Optional[str] = None, # Standard
	# on_change: Optional[Callable] = None, # Standard
	# args: Optional[tuple] = None, # Standard
	# kwargs: Optional[dict] = None, # Standard
	*,
	placeholder: Optional[str] = None, # Standard
	disabled: Optional[bool] = None, # Standard
	# label_visibility: Optional[str] = None, # 'visible' (default), 'hidden', 'collapse' # Standard
	hint: Optional[str] = None, # Alias for 'help'
	labelVisible: Optional[bool] = None,
	id: Optional[str] = None,
	descriptionId: Optional[str] = None,
	isInvalid: Optional[bool] = None,
	isValid: Optional[bool] = None,
	isWithWarning: Optional[bool] = None,
	labelClass: Optional[str] = None,
	wrapperClass: Optional[str] = None,
	requiredTip: Optional[str] = None,
	**kwargs,
):
	"""
	Streamlit DSFR Number Input component

	Streamlit standard component equivalent:
	https://docs.streamlit.io/library/api-reference/widgets/st.number_input
	"""
	if value is None:
		if min_value is not None:
			value = min_value
		else:
			value = 0.0

	if step is None:
		if isinstance(step, int):
			step = 1
		else:
			step = 0.01

	return dsfr_input(
		label = label,
		value = value,
		key = key,
		type = 'number',
		help = help,
		placeholder = placeholder,
		disabled = disabled,
		hint = hint,
		labelVisible = labelVisible,
		id = id,
		descriptionId = descriptionId,
		isInvalid = isInvalid,
		isValid = isValid,
		isTextarea = False,
		isWithWarning = isWithWarning,
		labelClass = labelClass,
		wrapperClass = wrapperClass,
		requiredTip = requiredTip,
		min = min_value,
		max = max_value,
		step = step,
		**kwargs,
	)

dsfr_number_input = number_input

def text_area(
	label: str, # Standard
	value: Optional[str] = None, # Standard
	height: Optional[int] = None, # Standard
	# max_chars: Optional[int] = None, # Standard
	key: Optional[Union[str, int]] = None, # Standard
	help: Optional[str] = None, # Standard
	# on_change: Optional[Callable] = None, # Standard
	# args: Optional[tuple] = None, # Standard
	# kwargs: Optional[dict] = None, # Standard
	*,
	placeholder: Optional[str] = None, # Standard
	disabled: Optional[bool] = None, # Standard
	# label_visibility: Optional[str] = None, # 'visible' (default), 'hidden', 'collapse' # Standard
	hint: Optional[str] = None, # Alias for 'help'
	labelVisible: Optional[bool] = None,
	id: Optional[str] = None,
	descriptionId: Optional[str] = None,
	isInvalid: Optional[bool] = None,
	isValid: Optional[bool] = None,
	isWithWarning: Optional[bool] = None,
	labelClass: Optional[str] = None,
	wrapperClass: Optional[str] = None,
	requiredTip: Optional[str] = None,
	**kwargs,
):
	"""
	Streamlit DSFR Text Area component

	Streamlit standard component equivalent:
	https://docs.streamlit.io/library/api-reference/widgets/st.text_area
	"""
	if value is None:
		value = ''

	return dsfr_input(
		label = label,
		value = value,
		height = height,
		key = key,
		help = help,
		placeholder = placeholder,
		disabled = disabled,
		hint = hint,
		labelVisible = labelVisible,
		id = id,
		descriptionId = descriptionId,
		isInvalid = isInvalid,
		isValid = isValid,
		isTextarea = True,
		isWithWarning = isWithWarning,
		labelClass = labelClass,
		wrapperClass = wrapperClass,
		requiredTip = requiredTip,
		**kwargs,
	)

dsfr_text_area = text_area

def date_input(
	label: str, # Standard
	# value: Optional[Union[datetime, str]] = None, # Standard
	value: Optional[str] = None, # Semi-standard
	# min_value: Optional[Union[datetime]] = None, # Standard
	min_value: Optional[str] = None, # Semi-standard
	# max_value: Optional[Union[datetime]] = None, # Standard
	max_value: Optional[str] = None, # Semi-standard
	key: Optional[Union[str, int]] = None, # Standard
	help: Optional[str] = None, # Standard
	# on_change: Optional[Callable] = None, # Standard
	# args: Optional[tuple] = None, # Standard
	# kwargs: Optional[dict] = None, # Standard
	*,
	# format: Optional[str] = None, # Standard
	disabled: Optional[bool] = None, # Standard
	# label_visibility: Optional[str] = None, # 'visible' (default), 'hidden', 'collapse' # Standard
	hint: Optional[str] = None, # Alias for 'help'
	labelVisible: Optional[bool] = None,
	id: Optional[str] = None,
	descriptionId: Optional[str] = None,
	isInvalid: Optional[bool] = None,
	isValid: Optional[bool] = None,
	isWithWarning: Optional[bool] = None,
	labelClass: Optional[str] = None,
	wrapperClass: Optional[str] = None,
	requiredTip: Optional[str] = None,
	**kwargs,
):
	"""
	Streamlit DSFR Text Area component

	Streamlit standard component equivalent:
	https://docs.streamlit.io/library/api-reference/widgets/st.date_input
	"""
	if value is None:
		value = ''

	return dsfr_input(
		label = label,
		value = value,
		key = key,
		help = help,
		disabled = disabled,
		hint = hint,
		labelVisible = labelVisible,
		id = id,
		descriptionId = descriptionId,
		isInvalid = isInvalid,
		isValid = isValid,
		isTextarea = False,
		isWithWarning = isWithWarning,
		labelClass = labelClass,
		wrapperClass = wrapperClass,
		requiredTip = requiredTip,
		min = min_value,
		max = max_value,
		**kwargs,
	)

dsfr_date_input = date_input

def time_input(
	label: str, # Standard
	# value: Optional[Union[datetime, str]] = None, # Standard
	value: Optional[str] = None, # Semi-standard
	key: Optional[Union[str, int]] = None, # Standard
	help: Optional[str] = None, # Standard
	# on_change: Optional[Callable] = None, # Standard
	# args: Optional[tuple] = None, # Standard
	# kwargs: Optional[dict] = None, # Standard
	*,
	disabled: Optional[bool] = None, # Standard
	# label_visibility: Optional[str] = None, # 'visible' (default), 'hidden', 'collapse' # Standard
	# step: Optional[Union[int, timedelta]] = None, # Standard
	step: Optional[int] = None, # Semi-standard
	hint: Optional[str] = None, # Alias for 'help'
	labelVisible: Optional[bool] = None,
	id: Optional[str] = None,
	descriptionId: Optional[str] = None,
	isInvalid: Optional[bool] = None,
	isValid: Optional[bool] = None,
	isWithWarning: Optional[bool] = None,
	labelClass: Optional[str] = None,
	wrapperClass: Optional[str] = None,
	requiredTip: Optional[str] = None,
	**kwargs,
):
	"""
	Streamlit DSFR Text Area component

	Streamlit standard component equivalent:
	https://docs.streamlit.io/library/api-reference/widgets/st.time_input
	"""
	if value is None:
		value = ''

	return dsfr_input(
		label = label,
		value = value,
		key = key,
		help = help,
		disabled = disabled,
		hint = hint,
		labelVisible = labelVisible,
		id = id,
		descriptionId = descriptionId,
		isInvalid = isInvalid,
		isValid = isValid,
		isTextarea = False,
		isWithWarning = isWithWarning,
		labelClass = labelClass,
		wrapperClass = wrapperClass,
		requiredTip = requiredTip,
		step = step,
		**kwargs,
	)

dsfr_time_input = time_input

def picture(
	# image: Union[np.ndarray, List[np.ndarray], BytesIO, str, List[str]], # Standard
	image: [BytesIO, str], # Semi-standard
	# caption: Optional[Union[str, List[str]]] = None, # Standard
	caption: Optional[str] = None, # Semi-standard
	size: Optional[str] = None, # 'small' | 'medium' | 'large'
	# width: Optional[int] = None, # Standard
	# use_column_width: Optional[Union[str, bool]] = None, # 'auto' | 'always' | 'never' | bool # Standard
	# clamp: Optional[bool] = None, # Standard
	# channels: Optional[str] = None, # 'RGB' | 'BGR' # Standard
	# output_format: Optional[str] = None, # 'JPEG' | 'PNG' | 'auto' # Standard
	*,
	legend: Optional[str] = None, # Alias for 'caption'
	alt: Optional[str] = None,
	title: Optional[str] = None,
	ratio: Optional[str] = None, # '32x9' | '16x9' | '3x2' | '4x3' | '1x1' | '3x4' | '2x3'
	key: Optional[Union[str, int]] = None,
	**kwargs,
):
	"""
	Streamlit DSFR Picture component

	Streamlit standard component equivalent:
	https://docs.streamlit.io/library/api-reference/media/st.image
	"""
	if isinstance(image, BytesIO):
		# Convert BytesIO to base64
		image_data = base64.b64encode(image.getvalue()).decode('utf-8')
		# Get image type (if possible, in child class of BytesIO like streamlit's UploadedFile)
		image_type = image.type if hasattr(image, 'type') else 'image/png'
		kwargs['src'] = f'data:{image_type};base64,{image_data}'
	elif isinstance(image, str):
		kwargs['src'] = image

	if caption is not None:
		kwargs['legend'] = caption
	elif legend is not None:
		kwargs['legend'] = legend

	if size is not None:
		kwargs['size'] = size
	if alt is not None:
		kwargs['alt'] = alt
	if title is not None:
		kwargs['title'] = title
	if ratio is not None:
		kwargs['ratio'] = ratio

	return _dsfr_picture_func(**kwargs, key = key, default = None)

image = picture
dsfr_picture = picture
dsfr_image = picture

def radio(
	label: str, # Standard
	options: Iterable[str], # Standard
	index: Optional[int] = None, # Standard
	format_func: Optional[Callable] = None, # Standard
	key: Optional[Union[str, int]] = None, # Standard
	# help: Optional[str] = None, # Supported in DSFR but missing in VueDsfr? # Standard
	# on_change: Optional[Callable] = None, # Standard
	# args: Optional[tuple] = None, # Standard
	# kwargs: Optional[dict] = None, # Standard
	*,
	disabled: Optional[Union[bool, list[bool]]] = None, # Standard
	horizontal: Optional[bool] = None, # Standard
	captions: Optional[list[str]] = None, # Standard
	# label_visibility: Optional[str] = None, # 'visible' (default), 'hidden', 'collapse' # Standard
	inline: Optional[bool] = None, # Alias for 'horizontal'
	hints: Optional[list[str]] = None, # Alias for 'captions'
	small: Optional[bool] = None,
	titleId: Optional[str] = None,
	required: Optional[bool] = None,
	name: Optional[str] = None,
	errorMessage: Optional[str] = None,
	validMessage: Optional[str] = None,
	requiredTip: Optional[str] = None,
	default: Optional[int] = None,
	**kwargs,
):
	"""
	Streamlit DSFR Radio component

	Streamlit standard component equivalent:
	https://docs.streamlit.io/library/api-reference/widgets/st.radio
	"""
	kwargs['legend'] = label

	if format_func is None:
		format_func = lambda x: x

	kwargs['options'] = [
		{
			'label': format_func(option),
			'value': option,
		}
		for option in options
	]

	lenoptions = len(kwargs['options'])

	if index is None:
		index = 0
	if lenoptions > 0:
		if index < lenoptions:
			kwargs['modelValue'] = kwargs['options'][index]['value']
		else:
			kwargs['modelValue'] = kwargs['options'][0]['value']
	else:
		kwargs['modelValue'] = None

	if disabled is not None:
		if isinstance(disabled, bool):
			kwargs['disabled'] = disabled
		elif isinstance(disabled, Iterable):
			if len(disabled) > lenoptions:
				raise ValueError('disabled as a list cannot be longer than options')
			for index, value in enumerate(disabled):
				kwargs['options'][index]['disabled'] = value
		else:
			raise ValueError('disabled must be a bool or a list of bools')

	if horizontal is not None:
		kwargs['inline'] = small
	elif inline is not None:
		kwargs['inline'] = small

	if captions is None:
		captions = hints
	if captions is not None:
		if len(captions) > lenoptions:
			raise ValueError('captions cannot be longer than options')
		for index, value in enumerate(captions):
			kwargs['options'][index]['hint'] = value

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
	if requiredTip is not None:
		kwargs['requiredTip'] = requiredTip
	if default is not None:
		kwargs['value'] = default

	return _dsfr_radio_func(**kwargs, key = key, default = kwargs['modelValue'])

dsfr_radio = radio

def range(
	label: str, # Standard
	# min_value: Optional[Union[int, float, datetime, timedelta]] = None, # Standard
	min_value: Optional[Union[int, float]] = None, # Semi-standard
	# max_value: Optional[Union[int, float, datetime, timedelta]] = None, # Standard
	max_value: Optional[Union[int, float]] = None, # Semi-standard
	# value: Optional[Union[int, float, tuple[int, int], tuple[float, float], tuple[datetime, datetime], Tuple[timedelta, timedelta]]] = None, # Standard
	value: Optional[Union[int, float, tuple[int, int], tuple[float, float]]] = None, # Semi-standard
	# step: Optional[Union[int, float, datetime, timedelta]] = None, # Standard
	step: Optional[Union[int, float]] = None, # Semi-standard
	# format: Optional[str] = None, # Standard
	key: Optional[Union[str, int]] = None, # Standard
	help: Optional[str] = None, # Standard
	# on_change: Optional[Callable] = None, # Standard
	# args: Optional[tuple] = None, # Standard
	# kwargs: Optional[dict] = None, # Standard
	*,
	disabled: Optional[bool] = None, # Standard
	# label_visibility: Optional[str] = None, # 'visible' (default), 'hidden', 'collapse' # Standard
	hint: Optional[str] = None, # Alias for 'help'
	messages: Optional[dict] = None,
	id: Optional[str] = None,
	lowerValue: Optional[Union[int, float]] = None,
	message: Optional[str] = None,
	prefix: Optional[str] = None,
	suffix: Optional[str] = None,
	small: Optional[bool] = None,
	hideIndicators: Optional[bool] = None,
	**kwargs,
):
	"""
	Streamlit DSFR Radio component

	Streamlit standard component equivalent:
	https://docs.streamlit.io/library/api-reference/widgets/st.slider
	"""
	kwargs['label'] = label

	if help is not None:
		kwargs['hint'] = help
	elif hint is not None:
		kwargs['hint'] = hint

	if messages is not None:
		kwargs['messages'] = messages

	if min_value is None:
		min_value = 0
	kwargs['min'] = min_value
	if value is None:
		value = min_value

	if max_value is not None:
		kwargs['max'] = max_value

	if value is not None:
		kwargs['modelValue'] = value
		if min_value is None:
			if isinstance(value, int):
				kwargs['min'] = 0
			elif isinstance(value, float):
				kwargs['min'] = 0.0
		if max_value is None:
			if isinstance(value, int):
				kwargs['max'] = 100
			elif isinstance(value, float):
				kwargs['max'] = 1.0
		if step is None:
			if isinstance(value, int):
				kwargs['step'] = 1
			elif isinstance(value, float):
				kwargs['step'] = 0.01

	if id is not None:
		kwargs['id'] = id
	if lowerValue is not None:
		kwargs['lowerValue'] = lowerValue
	if message is not None:
		kwargs['message'] = message
	if prefix is not None:
		kwargs['prefix'] = prefix
	if suffix is not None:
		kwargs['suffix'] = suffix
	if small is not None:
		kwargs['small'] = small
	if hideIndicators is not None:
		kwargs['hideIndicators'] = hideIndicators

	if step is not None:
		kwargs['step'] = step

	if disabled is not None:
		kwargs['disabled'] = disabled

	return _dsfr_range_func(**kwargs, key = key, default = kwargs['modelValue'])

slider = range
dsfr_range = range
dsfr_slider = range

# Util functions for users

from .override_font_family import override_font_family
