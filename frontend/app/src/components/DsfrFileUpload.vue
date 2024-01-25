<script setup lang="ts">
import { Streamlit } from '~/stcomponentlib'
import { DsfrFileUpload } from '@gouvminint/vue-dsfr'

import { useStreamlit } from '../streamlit'
import type { ComponentProps } from '../types/ComponentProps.d.ts'

useStreamlit()

const props = defineProps<
	ComponentProps<{
		// Props
		id?: string
		label?: string
		hint?: string
		error?: string
		validMessage?: string
		disabled?: boolean
		accept?: string[]
		modelValue?: string
		// Streamlit
		key?: string
	}>
>()

interface FileData
{
	name: string
	type: string
	data: string // bytes in base64
}

let value: FileData | undefined = undefined
let lastValue: FileData | undefined = value

function setComponentValue()
{
	if (value !== lastValue)
	{
		lastValue = value
		Streamlit.setComponentValue(value)
	}
}

function onChange(files: FileList | null)
{
	if (files && files.length > 0)
	{
		// Using File, FileReady, get the raw bytes
		// Then, encode in base64 and send to steamlit
		const file = files[0]!
		const reader = new FileReader()
		reader.addEventListener('load', () => {
			const dataUrl = reader.result as string
			const base64 = dataUrl.split(',')[1]!
			value = {
				'name':	file['name'],
				'type': file['type'],
				'data': base64,
			}
			setComponentValue()
		})
		reader.readAsDataURL(file)
	}
	else
	{
		value = undefined
		setComponentValue()
	}
}
</script>

<template>
	<div class="component">
		<DsfrFileUpload
			v-bind="props.args"
			:disabled="props.disabled || props.args.disabled"
			@change="onChange"
		/>
	</div>
</template>
