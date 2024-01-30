<script setup lang="ts">
import { ref } from 'vue'
import { Streamlit } from '~/stcomponentlib'
import { DsfrInput } from '@gouvminint/vue-dsfr'

import { useStreamlit } from '../streamlit'
import type { ComponentProps } from '../types/ComponentProps.d.ts'

useStreamlit()

const props = defineProps<
	ComponentProps<{
		type?: string
		placeholder?: string
		disabled?: boolean
		// Props
		labelVisible?: boolean
		hint?: string
		modelValue?: string
		id?: string
		descriptionId?: string
		isInvalid?: boolean
		isValid?: boolean
		isTextarea?: boolean
		isWithWarning?: boolean
		labelClass?: string
		wrapperClass?: string
		// Slots
		label?: string
		requiredTip?: string
		// Custom
		height?: string
	}>
>()

// Bind the input value to `value`
const value = ref<string>(props.args.modelValue ?? '')
const lastValue = ref(value.value)

function setComponentValue()
{
	if (value.value !== lastValue.value)
	{
		lastValue.value = value.value

		if (value.value !== '' && props.args.type === 'number')
		{
			Streamlit.setComponentValue(Number(value.value))
		}
		else
		{
			Streamlit.setComponentValue(value.value)
		}
	}
}

// Update the Steamlit value when:
// - the input lose focus, if the value has changed
// - the user press enter, if the input is focused and the value has changed

function onInput(event: Event)
{
	const target = event.target as HTMLInputElement
	value.value = target.value
}

function onBlur()
{
	setComponentValue()
}

function onKeydown(event: KeyboardEvent)
{
	if (event.key === 'Enter')
	{
		setComponentValue()
	}
}
</script>

<template>
	<div
		class="component"
		:style="{
			'--dsfr-input-height': props.args.height ? `${props.args.height}px` : '5.75rem',
		}"
	>
		<DsfrInput
			v-bind="props.args"
			:disabled="props.disabled || props.args.disabled"
			v-model="value"
			@input="onInput"
			@blur="onBlur"
			@keydown="onKeydown"
		>
			<template #label v-if="props.args.label">
				{{ props.args.label }}
			</template>
			<template #required-tip v-if="props.args.requiredTip">
				{{ props.args.requiredTip }}
			</template>
		</DsfrInput>
	</div>
</template>

<style scoped>
.component {
	margin: 4px; /* Margin for the input outline on focus */
}

.component :deep(textarea.fr-input) {
	min-height: var(--dsfr-input-height);
	resize: none; /* While we don't send the new height to Streamlit */
}
</style>
