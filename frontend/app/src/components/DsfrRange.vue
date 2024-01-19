<script setup lang="ts">
import { ref } from 'vue'
import { Streamlit } from '~/stcomponentlib'
import { DsfrRange } from '@gouvminint/vue-dsfr'

import { useStreamlit } from '../streamlit'
import type { ComponentProps } from '../types/ComponentProps.d.ts'

useStreamlit()

const props = defineProps<
	ComponentProps<{
		// Slots
		label?: string
		hint?: string
		messages?: object
		// Props
		min?: number
		max?: number
		modelValue?: number
		id?: string
		lowerValue?: number
		message?: string
		prefix?: string
		suffix?: string
		small?: boolean
		hideIndicators?: boolean
		step?: number
		disabled?: boolean
	}>
>()

const lastValue = ref('')
const value = ref('')

// Bind the input value to `value`
// Update the Steamlit value when:
// - the input lose focus, if the value has changed
// - the user press enter, if the input is focused and the value has changed

function onUpdateModelValue()
{
	console.log('onUpdateModelValue', value.value)
	Streamlit.setComponentValue(value.value)
}

const onBlur = () =>
	{
		console.log('onBlur', value.value, '!==', lastValue.value)
		if (value.value !== lastValue.value)
		{
			lastValue.value = value.value
			Streamlit.setComponentValue(value.value)
		}
	}
</script>

<template>
	<div class="component">
		<DsfrRange
			v-bind="props.args"
			:disabled="props.disabled || props.args.disabled"
			v-model="value"
			@update:modelValue="onUpdateModelValue"
			@blur="onBlur"
		>
			<template #label v-if="props.args.label">
				{{ props.args.label }}
			</template>
			<template #required-tip v-if="props.args.requiredTip">
				{{ props.args.requiredTip }}
			</template>
		</DsfrRange>
	</div>
</template>

<!-- <style scoped>
.component {
	margin: 4px; /* Margin for the input outline on focus */
}
</style> -->
