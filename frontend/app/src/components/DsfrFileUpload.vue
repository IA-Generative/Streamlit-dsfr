<script setup lang="ts">
import { ref } from 'vue'
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

// Bind the input value to `value`
const value = ref<string | undefined>(undefined)
const lastValue = ref(value.value)

function setComponentValue()
{
	if (value.value !== lastValue.value)
	{
		lastValue.value = value.value
		Streamlit.setComponentValue(value.value)
	}
}

function onChange(files: FileList | null)
{
	if (files && files.length > 0)
	{
		// Using File, FileReady, get the raw bytes
		// Then, encode in base64 and send to steamlit
		const file = files[0]
		const reader = new FileReader()
		reader.addEventListener('load', () => {
			const base64 = reader.result as string
			const base64WithoutPrefix = base64.split(',')[1]
			value.value = base64WithoutPrefix
			setComponentValue()
		})
		reader.readAsDataURL(file)
	}
	else
	{
		value.value = undefined
	}
}
</script>

<template>
	<div class="component">
		<DsfrFileUpload
			v-bind="props.args"
			:disabled="props.disabled || props.args.disabled"
			v-model="value"
			@change="onChange"
		/>
	</div>
</template>
